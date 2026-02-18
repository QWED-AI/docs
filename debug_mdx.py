import os
import re
import yaml

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    if not lines:
        return []

    errors = []

    # Check if starts with ---
    if lines[0].strip() != '---':
        errors.append("Does not start with '---'")
        return errors # Stop here if no frontmatter

    # Find end of frontmatter
    try:
        end_idx = lines.index('---', 1)
    except ValueError:
        errors.append("No closing '---' for frontmatter")
        return errors

    frontmatter_content = '\n'.join(lines[1:end_idx])
    
    # Check for valid YAML
    try:
        data = yaml.safe_load(frontmatter_content)
        if not isinstance(data, dict):
             errors.append("Frontmatter is not a dictionary")
    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML in frontmatter: {e}")

    # Check for duplicate title (simple string check in raw content)
    if frontmatter_content.count('title:') > 1:
        errors.append("Duplicate 'title:' in frontmatter")

    # Check for suspicious H1s
    body = '\n'.join(lines[end_idx+1:])
    if re.search(r'^#\s+', body, re.MULTILINE):
         # This is allowed but we want to know if I missed any
         pass 

    # Remove code blocks
    content_no_code = re.sub(r'```[\s\S]*?```', '', content)
    content_no_code = re.sub(r'`[^`\n]*`', '', content_no_code)

    # Check for <Tag> that might be interpreted as component
    # We allow some known ones or just flag all to review
    matches = re.finditer(r'<([a-zA-Z][a-zA-Z0-9\-]*)', content_no_code)
    for m in matches:
        tag = m.group(1)
        # component names usually start with Uppercase in Mintlify if custom, but HTML tags like <div> are also valid if closed.
        # However, <EMAIL_ADDRESS> is definitely invalid if not in code.
        # Also <Note> is valid.
        
        lineno = content[:m.start()].count('\n') + 1
        # Get context
        line = lines[lineno-1]
        errors.append(f"Potential unescaped tag or component usage: <{tag} at line {lineno}: {line.strip()[:50]}...")

    return errors

root_dir = 'c:/Users/rahul/.gemini/antigravity/playground/vector-meteoroid/qwed-docs-mintlify'
log_file = 'debug_log.txt'
print(f"Scanning {root_dir}...")

with open(log_file, 'w', encoding='utf-8') as log:
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.mdx'):
                path = os.path.join(subdir, file)
                try:
                    errs = check_file(path)
                    if errs:
                        log.write(f"File: {path}\n")
                        for e in errs:
                            log.write(f"  - {e}\n")
                except Exception as e:
                    log.write(f"File: {path}\n  - CRASH: {e}\n")

print("Scan complete. Check debug_log.txt")
