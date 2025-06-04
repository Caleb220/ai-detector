import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    try {
      const res = await axios.post('http://127.0.0.1:8000/analyse', { text });
      setResult(res.data);
    } catch (err) {
      console.error('Error analyzing text:', err);
    }
  };

  return (
    <div className="App">
      <h1>AI Detection Tool</h1>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={10}
        cols={50}
        placeholder="Paste your text here..."
      />
      <br />
      <button onClick={handleAnalyze}>Analyze</button>
      {result && (
        <div className="result">
          <h2>Results</h2>
          <p><strong>AI Likelihood:</strong> {result.ai_score}</p>
          <p><strong>Explanation:</strong> {result.explanation}</p>
        </div>
      )}
    </div>
  );
}

export default App;
