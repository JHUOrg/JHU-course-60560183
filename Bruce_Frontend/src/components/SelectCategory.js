import React from 'react'

const SelectCategory = ({gameState, setGameState, callUpdate}) => {
  const categories = gameState.getAvailableCategories()

  const categoryClick = (selection) =>{
    gameState.answerQuestion(selection)
    gameState.setMode(0)
    setGameState(gameState)
    callUpdate(gameState.getMode())
  }
  
  return (
    <div>
      {(gameState.getMode() === 2) ? <h1>Player's Choice</h1> : <h1>Opponents Choice</h1>}
      {categories[0] !== "" && <button onClick={()=>categoryClick(0)}>{categories[0]}</button>}
      {categories[1] !== "" && <button onClick={()=>categoryClick(1)}>{categories[1]}</button>}
      {categories[2] !== "" && <button onClick={()=>categoryClick(2)}>{categories[2]}</button>}
      {categories[3] !== "" && <button onClick={()=>categoryClick(3)}>{categories[3]}</button>}
      {categories[4] !== "" && <button onClick={()=>categoryClick(4)}>{categories[4]}</button>}
      {categories[5] !== "" && <button onClick={()=>categoryClick(5)}>{categories[5]}</button>}
    </div>
  )
}
export default SelectCategory