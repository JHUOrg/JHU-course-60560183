import React from 'react'

const PlayerInformation = ({players}) => {

  return (
    <div>
    <h1>Player Information</h1>
    {players.map((player) => (
      <div id={player}>
      <p>Name: {player.getName()}</p>
      <p>Score: {player.getScore()}</p>
      <p>Free Turns: {player.getFreeTurns()}</p>
      </div>
    ))}
    </div>
  )
}

export default PlayerInformation