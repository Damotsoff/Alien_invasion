class Setings():
    def __init__(self):
        # параметры экрана
        self.screen_width = 1200
        self.screen_heigth = 700
        self.bg_color = (2, 231, 231)
        self.ship_speed_factor = 1.5
        self.ship_limit = 1

        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.score_scale=1.5
        self.initialize_dynamic_setings()

    def initialize_dynamic_setings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points=50
    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
        print(self.alien_points)
