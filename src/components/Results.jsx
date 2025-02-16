import React from "react";

const Results = () => {
    const lastResult = JSON.parse(localStorage.getItem("quizResult"));

    return (
        <div className="results-container">
            <h2>Dernier Résultat :</h2>
            {lastResult ? (
                <p>Score : {lastResult.correct} / {lastResult.total}</p>
            ) : (
                <p>Aucun score enregistré.</p>
            )}
        </div>
    );
};

export default Results;
