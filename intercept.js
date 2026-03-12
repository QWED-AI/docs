const { spawn } = require('child_process');
const fs = require('fs');

const logStream = fs.createWriteStream('mint_intercept.log');
const cmd = spawn('npx.cmd', ['-y', '@mintlify/cli@latest', 'validate'], {
    env: { ...process.env, FORCE_COLOR: '0', TERM: 'dumb' },
    shell: true
});

cmd.stdout.on('data', (data) => {
    const text = data.toString();
    logStream.write(text);
    process.stdout.write(text);
});

cmd.stderr.on('data', (data) => {
    const text = data.toString();
    logStream.write(text);
    process.stderr.write(text);
});

cmd.on('close', (code) => {
    console.log(`Child exited with code ${code}`);
    logStream.end();
});
