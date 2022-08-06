import React from 'react'

const GameInformation = ({gameState}) => {
  return (
    <div>
        <p>Current Round: {gameState.getCurrentRound()}</p>
        <p>Number of Spins in Round: {gameState.getSpinCounter()}</p>
        <p>Turn Points: {gameState.getTurnPoints()}</p>
        <p>Current Player: {gameState.getCurrentPlayer()}</p>
    </div>
  )
}

export default GameInformation