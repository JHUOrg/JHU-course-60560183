import Player from "./Player";
import QuestionBank from "./QuestionBank"

class Game {
    currentPlayer = 0;
    currentRound = 1;
    players;
    questionBank;
    spinCounter = 0;
    turnPoints = 0;
    currentCategory;
    currentQuestion;
    mode = -99;
    message = "Please Add Players To Begin Game"

    constructor(){
        this.questionBank = new QuestionBank()
        this.players = []
        this.currentCategory = []
        this.currentQuestion = null
    }

    addPlayer(name){this.players.push(new Player(name));}

    answerQuestion(category){
        this.currentCategory = [category, this.questionBank.getCategoryName(category)]
        this.currentQuestion = this.questionBank.answerQuestion(category)
    }

    calculatePoints(y){return (y) * 100 * this.currentRound}

    deletePlayer(index){this.players.splice(index, 1)}

    decreaseFreeTurns(){this.players[this.currentPlayer].decreaseFreeTurns()}

    endGame(){
        return null;
    }

    generateRandomSector(){
        this.increaseSpinCounter()

        const rNum = Math.floor(Math.random() * 18)
        const playerName = this.players[this.currentPlayer].getName()
        
        if (rNum < 12){
            const category = Math.floor(rNum/2)
            this.setMessage(`CATEGORY SELECTED: ${this.questionBank.getCategoryName(category)}`)
            if (this.questionBank.verifyQuestionsInCategory(category)){
                this.answerQuestion(category)
                this.setMode(0)
            } else {
                this.setMode(-1)
                this.setMessage(`There are no question remaining in ${this.questionBank.getCategoryName(category)}, Spin Again!`)
            }
        }  
        else if (rNum < 13) {
            // Lose Turn
            if (this.players[this.currentPlayer].getFreeTurns() === 0){
                this.setMode(-1)
                this.setMessage('LOSE TURN: You have no Free Turn Tokens Remaining, Next Player')
                this.nextPlayer()
            }else{
                this.setMode(1)
                this.setMessage(`LOSE TURN: ${playerName}, Would you like to use a Free Turn Token?`)
            }
        } 
        else if (rNum< 14) {
            this.players[this.currentPlayer].increaseFreeTurns()
            this.setMode(-1)
            this.setMessage(`FREE TURN: ${playerName} has been awarded a Free Turn Token, Spin Again`)
        } 
        else if (rNum < 15) {
            this.setMessage(`BANKRUPT: ${playerName} you have earned no points, next player`)
            this.resetTurnPoints()
            this.nextPlayer()
            this.setMode(-1)
        } 
        else if (rNum < 16) {
            this.setMode(-1)
            this.setMessage('SPIN AGAIN')
        } 
        else if (rNum < 17) {
            this.setMode(2)
            this.setMessage(`PLAYER CHOICE: ${playerName} please choose a category`)
        } 
        else {
            this.setMode(3)
            this.setMessage(`OPPONENT CHOICE: Everyone but ${playerName} please choose a category`)
        }
        this.verifyEndRound()
    }
    
    getAvailableCategories(){return this.questionBank.getAvailableCategories()}
    getCurrentCategory(){return this.currentCategory}
    getCurrentPlayer(){return this.currentPlayer}
    getCurrentPlayerName(){return this.players[this.currentPlayer].getName()}
    getCurrentQuestion(){return this.currentQuestion}
    getCurrentQuestionOfCateogry(category){return this.questionBank.getCurrentQuestion(category)}
    getMessage(){return this.message}
    getMode(){return this.mode}
    getCurrentRound(){return this.currentRound}
    getPlayers(){return this.players;}
    getSpinCounter(){return this.spinCounter;}
    getTurnPoints(){return this.turnPoints;}

    increaseSpinCounter(){this.spinCounter += 1;}

    nextPlayer(){
        this.players[this.currentPlayer].updateScore(this.turnPoints)
        this.resetTurnPoints()
        if (this.currentPlayer < (this.players.length - 1)){
            this.currentPlayer += 1
        } else {
            this.currentPlayer = 0
        }
    }

    nextRound(){
        return null;
    }

    resetSpinCounter(){this.spinCounter = 0;}
    resetTurnPoints(){this.turnPoints = 0;}

    setMessage(newMessage){this.message = newMessage}
    setMode(newMode){this.mode = newMode}

    updateTurnPoints(amount){this.turnPoints += amount;}

    verifyEndRound(){
        if (!this.verifySpinsRemaining()){
            this.currentRound += 1
        }

        if (!this.questionBank.verifyQuestionsRemaining()){
            this.currenRound += 1
        }
    }

    verifySpinsRemaining(){
        return this.spinCounter < 50;
    }
}
export default Game;