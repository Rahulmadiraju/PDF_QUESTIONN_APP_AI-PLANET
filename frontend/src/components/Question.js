// frontend/src/components/Question.js

import React from 'react';

function Question({ question }) {
    return <div>{question.question_text}</div>;
}

export default Question;
