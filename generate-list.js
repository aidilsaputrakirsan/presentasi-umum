const fs = require('fs');
const path = require('path');

const rootPath = __dirname;
const items = fs.readdirSync(rootPath, { withFileTypes: true });
const presentations = items
    .filter(item => item.isDirectory() && item.name !== 'node_modules' && item.name !== 'public' && !item.name.startsWith('.'))
    .filter(item => fs.existsSync(path.join(rootPath, item.name, 'slides.md')))
    .map(item => ({
        id: item.name,
        name: item.name.replace(/-/g, ' ')
    }));

fs.writeFileSync(path.join(rootPath, 'public', 'presentations.json'), JSON.stringify(presentations, null, 2));
console.log('Presentations list updated in public/presentations.json');
