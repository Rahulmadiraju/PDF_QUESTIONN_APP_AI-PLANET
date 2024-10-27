// // frontend/src/App.js

import React, { useState } from 'react';
import Upload from './components/Upload';
import Question from './components/Question';
import './App.css';

function App() {
    const [questions, setQuestions] = useState([]);

    const handleQuestions = (questionsData) => {
        setQuestions(questionsData);
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>PDF Question Extractor</h1>
                <Upload onQuestions={handleQuestions} />
                {questions.length > 0 && (
                    <div className="questions-container">
                        {questions.map((q, index) => (
                            <div className="question" key={index}>
                                <Question question={q} />
                            </div>
                        ))}
                    </div>
                )}
            </header>
        </div>
    );
}

export default App;
