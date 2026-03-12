import glob
import yaml

for file in glob.glob('**/*.mdx', recursive=True):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            fm = content[3:end]
            try:
                yaml.safe_load(fm)
            except Exception as e:
                print(f"Error in {file}: {e}")
