import React, { useState, useEffect } from "react";
import { words } from "../../data/words";
import "./WordQuizStyles.css";

const WordQuiz = ({ wordCount, onFinish }) => {
    const [selectedWords, setSelectedWords] = useState([]);
    const [answers, setAnswers] = useState({});
    const [score, setScore] = useState(null);
    const [feedback, setFeedback] = useState({});

    useEffect(() => {
        // Mélange les mots et prend les "wordCount" premiers
        const shuffled = [...words].sort(() => 0.5 - Math.random()).slice(0, wordCount);
        setSelectedWords(shuffled);
    }, [wordCount]);

    const handleChange = (index, value) => {
        setAnswers({ ...answers, [index]: value });
    };

    const handleSubmit = () => {
        let correct = 0;
        let newFeedback = {};

        selectedWords.forEach((word, index) => {
            const userAnswer = answers[index]?.toLowerCase().trim();
            const correctAnswers = word.fr.map((frWord) => frWord.toLowerCase().trim());

            if (correctAnswers.includes(userAnswer)) {
                correct++;
                newFeedback[index] = { correct: true, answer: userAnswer };
            } else {
                newFeedback[index] = { correct: false, correctAnswers: word.fr };
            }
        });

        setScore(correct);
        setFeedback(newFeedback);
        localStorage.setItem("quizResult", JSON.stringify({ correct, total: wordCount }));
    };

    return (
        <div className="quiz-container">
            <h2>Traduisez ces mots :</h2>
            <div className="answer-container">
                {selectedWords.map((word, index) => (
                    <div key={index} className="word-container">
                        <span className="word">{word.en[0]} :</span>
                        <div className="input-container">
                            <input 
                                type="text" 
                                onChange={(e) => handleChange(index, e.target.value)} 
                                className={feedback[index] && !feedback[index].correct ? "incorrect" : ""}
                            />
                            {feedback[index] && !feedback[index].correct && (
                                <p className="correction">Bonne réponse : {feedback[index].correctAnswers.join(", ")}</p>
                            )}
                        </div>
                    </div>
                ))}
            </div>
            <button onClick={handleSubmit}>Valider</button>
            {score !== null && <p>Score : {score} / {wordCount}</p>}
            {score !== null && <button onClick={onFinish}>Terminer la session</button>}
        </div>
    );
    
};

export default WordQuiz;
