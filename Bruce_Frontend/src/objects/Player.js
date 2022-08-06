class Player{
    freeTurns = 0;
    name = "";
    score = 0;

    constructor(name) {this.name = name;}

    decreaseFreeTurns() {this.freeTurns -=1;} //DONE
    getFreeTurns() {return this.freeTurns;} //Done
    getName() {return this.name;} //Done
    getScore() {return this.score} //Done
    increaseFreeTurns() {this.freeTurns +=1;} //Done
    resetScore() {this.score = 0;} //Done
    updateScore(amount) {this.score += amount} //Done
}

export default Player