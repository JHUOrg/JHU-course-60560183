# import os
# import sys
# import json

class Player:
    def __init__(self, player_name=None):
        self.player_name = player_name
        self.player_score = 0
        self.player_turns_taken = 0

    def get_player_name(self):
        if self.player_name is not None:
            print(f'Player Name: {self.player_name}')
            return
        print(f'Player name not set')
        return 
    
    def get_player_score(self):
        print(f'{self.player_name} score: {self.player_score}')
        return

    def increase_player_turn(self):
        #TODO: This method is probably not required given there is no player specific turns.
        # Its total 50 spins for the game.
        self.player_turns_taken += 1
        return

    def set_player_score(self, value_increase):
        self.player_score += value_increase
        return
        
    def update_player(self, player_name):
        """
        This method will persist the player details in /dynamicconfigurations/playersinsession.json
        based on the player_name
        pseudo-code:
        1. Get player attributes from the constructor
        2. Set the player values in the file by updating the contents of the file
        :param player_name: Name of the player
        :return: None
        """