
class Player:
    def __init__(self, player_name = None):
        self.player_name = player_name
        self.player_score = 0
        self.player_turns_taken = 0
        self.player_lost_turn = False

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
        self.player_turns_taken += 1
        return

    def set_player_score(self, value_increase):
        self.player_score += value_increase
        return

    def get_player_lost_turn(self):
        return self.player_lost_turn 
        
