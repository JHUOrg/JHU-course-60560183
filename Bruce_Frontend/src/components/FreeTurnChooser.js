import React from 'react'

const FreeTurnChooser = ({gameState, setGameState, callUpdate}) => {

    const onClick = (selector) => {
        if(selector === 0){
            gameState.decreaseFreeTurns()
            gameState.setMessage(`Free Token Redeemed`)
        }else{
            gameState.nextPlayer()
            gameState.setMessage(`Next Player`)
        }
        gameState.setMode(-1)
        setGameState(gameState)
        callUpdate(gameState.getMode())
    }

    return (
    <div>
        <h2>Do you want to use a Free Turn Token?</h2>
        <button onClick={() => onClick(0)}>Yes</button><button onClick={() => onClick(1)}>No</button>
    </div>
    )
}

export default FreeTurnChooser