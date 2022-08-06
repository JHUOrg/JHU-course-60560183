class Question {
    answers;
    correctAnswer;
    questionText;

    constructor(jo) {
        this.answers = jo.answers;
        this.correctAnswer = jo.correctAnswer;
        this.questionText = jo.questionText;
    }

    getAnswers(){return this.answers;} //DONE
    getCorrectAnswer(){return this.correctAnswer;} //DONE
    getQuestionText(){return this.questionText;} //DONE
}

export default Question