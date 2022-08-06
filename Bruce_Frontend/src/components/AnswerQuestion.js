import React from "react";

const AnswerQuestion = ({gameState, setGameState, callUpdate}) => {
  const category = gameState.getCurrentCategory()
  const question = gameState.getCurrentQuestion()

  let answers = question.getAnswers()

  const answerSelected = (selection) => {
    if (selection === question.correctAnswer){
      let points = gameState.calculatePoints(gameState.getCurrentQuestionOfCateogry(category[0]));
      gameState.updateTurnPoints(points);
      gameState.setMessage(`${answers[selection]} is right! Spin Again`)
      gameState.setMode(-1)
    } else {
      const players = gameState.getPlayers()
      if (players[gameState.getCurrentPlayer()].getFreeTurns() === 0){
        gameState.setMode(-1)
        gameState.setMessage(`Wrong Answer: You choose ${answers[selection]}, 
        the correct answer was ${answers[question.correctAnswer]}, Next Player`)
        gameState.nextPlayer()
      }else{
        gameState.setMode(1)
        gameState.setMessage(`Wrong Answer: You choose ${answers[selection]}, 
        the correct answer was ${answers[question.correctAnswer]}, Would you like to use a FreeTurn Token?`)
      }
    }
    setGameState(gameState)
    callUpdate(gameState.getMode())
  }

  return (
    <div>
      <h2>{category[1]}</h2>
      <p>{question.getQuestionText()}</p>
      <button onClick={() => answerSelected(0)}>{answers[0]}</button>
      <button onClick={() => answerSelected(1)}>{answers[1]}</button>
      <button onClick={() => answerSelected(2)}>{answers[2]}</button>
    </div>
  )
}

export default AnswerQuestion


