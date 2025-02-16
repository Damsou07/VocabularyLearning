import React, { useState } from "react";
import { words } from "../data/words";

const VocabularyForm = ({ onStart }) => {
    const [wordCount, setWordCount] = useState(5);
    console.log(words); // -test

    return (
        <div className="form-container">
            <h2>Choisissez le nombre de mots :</h2>
            <input
                type="number"
                min="1"
                max={words.lenght}
                value={wordCount}
                onChange={(e) => setWordCount(Number(e.target.value))}
            />
            <button onClick={() => onStart(wordCount)}>Commencer</button>
        </div>
    );
};

export default VocabularyForm;
