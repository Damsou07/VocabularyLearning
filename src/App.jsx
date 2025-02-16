import React, { useState } from "react";
import VocabularyForm from "./components/VocabularyForm";
import WordQuiz from "./components/WordQuiz";
import Results from "./components/Results";
import "./global.css";

const App = () => {
    const [wordCount, setWordCount] = useState(null);

    return (
        <div className="app-container">
            <h1>Entraînement Vocabulaire</h1>
            {wordCount === null ? (
                <>
                    <Results />
                    <VocabularyForm onStart={setWordCount} />
                </>
            ) : (
                <WordQuiz wordCount={wordCount} onFinish={() => window.location.reload()} />
            )}
        </div>
    );
};

export default App;
