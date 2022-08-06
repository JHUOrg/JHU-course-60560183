import './css/App.css';
import Game from './objects/Game.js'
import React, { Fragment, useState } from "react";
import AnswerQuestion from './components/AnswerQuestion';
import PlayerInformation from './components/PlayerInformation';
import GameInformation from "./components/GameInformation"
import FreeTurnChooser from './components/FreeTurnChooser';
import SelectCategory from './components/SelectCategory';

function App() {
  const [gameState, setGameState] = useState(new Game())
  const [update, callUpdate] = useState(0)

  const spinWheelClick = () => {
    if (gameState.getMode() === -99){
      gameState.setMessage("Please add at least one player before starting the game")
    }else{
      gameState.generateRandomSector()
    }
    setGameState(gameState)
    console.log(update)
    callUpdate("Spin Complete")
    callUpdate("TESt")
  }

  const addPlayerClick = () => {
    const playerList = gameState.getPlayers()
    gameState.addPlayer("Joe");
    gameState.addPlayer("Alice")
    gameState.setMode(-1)
    gameState.setMessage(`New Player Added! Welcome ${playerList[playerList.length -1].getName()}`)
    setGameState(gameState);
    callUpdate("Player Added")
  }

  return (
    <Fragment>
      <GameInformation gameState={gameState}/>
      <h3>{gameState.getMessage()}</h3>
      {gameState.getMode() < 0 && <button onClick={() => spinWheelClick()}>Spin Wheel</button>}
      <PlayerInformation players={gameState.getPlayers()}/>
      {gameState.getSpinCounter() === 0 && <button onClick={() => addPlayerClick()}>Add Player</button>}
      {gameState.getMode() === 0 && <AnswerQuestion  gameState={gameState} setGameState={setGameState} callUpdate={callUpdate}/>}
      {gameState.getMode() === 1 && <FreeTurnChooser gameState={gameState} setGameState={setGameState} callUpdate={callUpdate}/>}
      {gameState.getMode() > 1 && <SelectCategory gameState={gameState} setGameState={setGameState} callUpdate={callUpdate}/>}
    </Fragment>
  )
}

export default App;
