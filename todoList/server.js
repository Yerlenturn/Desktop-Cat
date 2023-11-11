const express = require('express');
const fs = require('fs').promises;
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Directory where notes are stored
const notesDir = path.join(__dirname, 'notes');

// Enable CORS middleware
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*'); // Allow requests from any origin
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});

// Create the notes directory if it doesn't exist
fs.mkdir(notesDir, { recursive: true })
    .catch(err => console.error('Error creating notes directory:', err));

// Endpoint to get a list of all notes
app.get('/todoList/notes', async (req, res) => {
    try {
        const noteFiles = await fs.readdir(notesDir);
        const notes = await Promise.all(noteFiles.map(async file => {
            const content = await fs.readFile(path.join(notesDir, file), 'utf-8');
            return { filename: file, content };
        }));
        res.json(notes);
    } catch (err) {
        console.error('Error reading notes:', err);
        res.status(500).send('Internal Server Error');
    }
});

// Endpoint to create a new note
// Create or edit a note
app.post('/todoList/notes', async (req, res) => {
    try {
        const { title, maxKey, tasks, cookies, reminder } = req.body.content;
        console.log(title)

        const filename = `${title.replace(/\s/g)}.json`
        const notePath = path.join(notesDir, filename);
        await fs.writeFile(notePath, JSON.stringify({ title, maxKey, tasks, cookies, reminder }));
        res.json({ message: 'Note updated successfully' });
    } catch (err) {
        console.error('Error creating or editing note:', err);
        res.status(500).send('Internal Server Error');
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
