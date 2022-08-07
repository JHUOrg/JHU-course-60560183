'import json'
import numpy
import player
'import QuestionBank'

class game:
    def __init__(self):
        self.player_list = []
        self.current_player = 0
        self.spin_counter = 50
        self.current_round = 1
        self.turnPoints = 0
        self.question_bank

    'Add a player to the list'
    def addPlayer(self, name):
        Player = player(name)
        self.player_list.append(Player)
        return

    'Remove a player from the list'
    def deletePlayer(self, player):
        self.player_list.remove(player)
        return

    'Get the next player in the list'
    def nextPlayer(self):
        len = self.player_list.count
        current = self.current_player

        if (current+1 >= len):
            self.current_player = 0
        else:
            self.current_player = current+1

        self.resetTurnPoints()
        return

    'Get the current player'
    def getCurrentPlayer(self):
        current = self.current_player
        return self.player_list(current)

    'Reset the points for current turn'
    def resetTurnPoints(self):
        self.turnPoints = 0
        return

    """
    Update the points for the current turn
    based on the point value and question result.
    If the answer was correct (true) add points, else subtract
    """
    def updateTurnPoints(self, points, result):
        turnPoints = self.calculateRoundPoints(points)

        if (result):
            self.turnPoints += turnPoints
        else:
            self.turnPoints -= turnPoints
        return

    'Calculate points based on the round'
    def calculateRoundPoints(self, points):
        return (points * self.current_round)

    'Update the current player score'
    def updatePlayerScore(self):
        player = self.getCurrentPlayer()
        points = self.calculatePoints()
        player.set_player_score(points)
        return

    'Return the current number of wheel spins'
    def getWheelSpins(self):
        return self.spin_counter

    """
    Check the spins remaining on the wheel. 
    If zero return true to indicate out of spins.
    """
    def verifyWheelSpins(self):
        if (self.getWheelSpins <= 0):
            return True
        else:
            return False
    
    'Reset the wheel spins back to 50'
    def resetWheelSpins(self):
        self.spin_counter = 50
        return

    'Decrease the wheel spins by 1'
    def decreaseWheelSpins(self):
        self.spin_counter -= 1
        return

    """
    Check the number of unanswered questions.
    If all questions have been answered return true.
    """
    def verifyQuestionCount(self):
        'if (question_bank.count <= 0)'
        return False

    """
    Check if the current round is over.
    Verify wheel spins left and questions left.
    """
    def verifyEndRound(self):
        spinsLeft = self.verifyWheelSpins()
        questionsLeft = self.verifyQuestionCount()

        if (spinsLeft or questionsLeft):
            self.nextRound()
        
        return

    'Update to round 2 or end the game'
    def nextRound(self):
        round = self.current_round

        if (round == 1):
            self.current_round = 2
            return
        else:
            self.endGame()
        
    def endGame(self):
        exit()

    'Generate a random number for the 12 sectors (6 static/6 question)'
    def generateRandomSector():
        return numpy.random.uniform(1, 12)
