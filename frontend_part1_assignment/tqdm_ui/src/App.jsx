import React, { useState, useEffect } from 'react';

function App() {
  const [progress, setProgress] = useState(null);
  const task_id = 'task_1';

  useEffect(() => {
    const fetchProgress = async () => {
      try {
        const response = await fetch(`http://localhost:5000/getProgress?task_id=${task_id}`);
        const data = await response.json();
        setProgress(data.progress);
        console.log('fetch progess');
        console.log(data.progress);
      } catch (error) {
        console.error('Error fetching progress:', error);
      }
    };

    const intervalId = setInterval(fetchProgress, 1000);

    return () => clearInterval(intervalId);
  }, [task_id]);

  const startProcess = async () => {
    try {
      const response = await fetch('http://localhost:5000/startProcess');
      const result = await response.text();
      console.log(result);
    } catch (error) {
      console.error('Error starting process:', error);
    }
  };

  return (
    <div>
      <h1>Progress Display</h1>
      {progress !== null ? (
        <progress value={progress} max="100"></progress>
      ) : (
        'Fetching progress...'
      )}
      <br />
      <button onClick={startProcess}>Start Process</button>
    </div>
  );
}

export default App;
