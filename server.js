const express = require('express');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const app = express();
const PORT = 3000;

app.use(express.static('public'));

let currentSlidevProcess = null;

// API untuk mendapatkan daftar folder presentasi
app.get('/api/presentations', (req, res) => {
    const rootPath = __dirname;
    try {
        const items = fs.readdirSync(rootPath, { withFileTypes: true });
        const presentations = items
            // Filter hanya directory dan exclude folder tertentu
            .filter(item => item.isDirectory() && item.name !== 'node_modules' && item.name !== 'public' && !item.name.startsWith('.'))
            // Pastikan di dalamnya ada slides.md
            .filter(item => fs.existsSync(path.join(rootPath, item.name, 'slides.md')))
            .map(item => ({
                id: item.name,
                name: item.name.replace(/-/g, ' ')
            }));
        res.json(presentations);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// API untuk menjalankan Slidev di folder tertentu
app.post('/api/run/:id', (req, res) => {
    const presentationId = req.params.id;
    const slidesPath = path.join(__dirname, presentationId, 'slides.md');

    if (!fs.existsSync(slidesPath)) {
        return res.status(404).json({ error: 'Presentasi tidak ditemukan.' });
    }

    // Matikan proses Slidev sebelumnya jika ada biar port 3030 tidak bentrok
    if (currentSlidevProcess) {
        console.log('Menghentikan presentasi sebelumnya...');
        currentSlidevProcess.kill('SIGINT');
    }

    console.log(`Menyiapkan materi untuk: ${presentationId}`);

    // Spawn Mesin Presentasi
    currentSlidevProcess = spawn('npx', ['slidev', slidesPath, '--port', '3030'], {
        cwd: __dirname,
        shell: true
    });

    currentSlidevProcess.stdout.on('data', (data) => console.log(`Sistem: ${data}`));
    currentSlidevProcess.stderr.on('data', (data) => console.error(`Sistem Error: ${data}`));

    // Beri jeda 3 detik agar Mesin Vite server siap (biasanya cukup)
    setTimeout(() => {
        res.json({ success: true, url: 'http://localhost:3030' });
    }, 3500);
});

app.listen(PORT, () => {
    console.log(`
=============================================
🌟 SISTEM MATERI INTERAKTIF BERJALAN 🌟
Akses melalui browser: http://localhost:${PORT}
=============================================
`);
});
