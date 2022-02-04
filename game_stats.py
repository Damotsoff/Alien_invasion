class GameStats():

    def __init__(self, ai_setings):
        self.ai_setings = ai_setings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ship_left = self.ai_setings.ship_limit
        self.score=0
        self.level=1
