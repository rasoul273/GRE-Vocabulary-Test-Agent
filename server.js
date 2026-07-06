const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

const wordsFile = path.join(__dirname, 'resources', 'WRDS.txt');
const correctFile = path.join(__dirname, 'resources', 'correct-answers.txt');
const incorrectFile = path.join(__dirname, 'resources', 'incorrect-answers.txt');

// API: GET /api/words
app.get('/api/words', (req, res) => {
    if (!fs.existsSync(wordsFile)) {
        return res.status(404).json({ error: 'WRDS.txt not found' });
    }

    try {
        const content = fs.readFileSync(wordsFile, 'utf-8');
        const lines = content.split('\n');
        const wordsList = [];

        for (let line of lines) {
            line = line.trim();
            if (!line || !line.includes(':')) continue;
            const [word, definition] = line.split(':', 2);
            wordsList.push({
                word: word.trim(),
                definition: definition.trim()
            });
        }

        if (wordsList.length < 4) {
            return res.status(400).json({ error: 'Need at least 4 words in database' });
        }

        res.json(wordsList);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// API: POST /api/reset
app.post('/api/reset', (req, res) => {
    try {
        // Delete if exists and recreate
        [correctFile, incorrectFile].forEach(filePath => {
            if (fs.existsSync(filePath)) {
                fs.unlinkSync(filePath);
            }
            fs.mkdirSync(path.dirname(filePath), { recursive: true });
            fs.writeFileSync(filePath, '', 'utf-8');
        });
        res.json({ success: true });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// API: POST /api/answer
app.post('/api/answer', (req, res) => {
    const { word, definition, isCorrect } = req.body;
    if (!word || !definition) {
        return res.status(400).json({ error: 'Missing word or definition' });
    }

    const targetFile = isCorrect ? correctFile : incorrectFile;

    try {
        fs.mkdirSync(path.dirname(targetFile), { recursive: true });
        fs.appendFileSync(targetFile, `${word}: ${definition}\n`, 'utf-8');
        res.json({ success: true });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Start Server
app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
