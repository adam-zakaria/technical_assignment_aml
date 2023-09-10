const express = require('express');
const { MongoClient } = require('mongodb');
const { exec } = require('child_process');

const app = express();
const cors = require('cors');

// Configure CORS
app.use(cors());

const port = 5000;

const uri = 'mongodb://localhost:27017/';
const client = new MongoClient(uri);

app.get('/getProgress', async (req, res) => {
  try {
    await client.connect();
    const db = client.db('progress_database');
    const collection = db.collection('progress_collection');
    const task_id = req.query.task_id;

    const doc = await collection.findOne({ task_id });
    res.json(doc);
  } catch (error) {
    console.error('Error getting progress:', error);
    res.status(500).send('Server Error');
  }
});

app.get('/startProcess', (req, res) => {
  exec('python process_with_progress.py', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing script: ${error}`);
      return res.status(500).send('Server Error');
    }
    console.log(`STDOUT: ${stdout}`);
    console.log(`STDERR: ${stderr}`);
    res.send('Process started');
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
