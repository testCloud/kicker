import time

class Game:
    def __init__(self, socket_publisher, event_publisher):
        self.socket_publisher = socket_publisher
        self.event_publisher = event_publisher
        self.start()

    def goal_for_black(self):
        self.score_black += 1
        self.event_publisher.publish('goal', { 'team': 'black' })
        if self.score_black == 6:
            self.socket_publisher.publish({ 'message': 'BLACK TEAM WINS', 'score_black': self.score_black, 'score_yellow': self.score_yellow })
            self.event_publisher.publish('game_ended', { 'winner': 'black', 'score_black': self.score_black, 'score_yellow': self.score_yellow })
            time.sleep(15)
            self.start()
        else:
            self.socket_publisher.publish({ 'message': '', 'score_black': self.score_black, 'score_yellow': self.score_yellow })

    def goal_for_yellow(self):
        self.score_yellow += 1
        self.event_publisher.publish('goal', { 'team': 'yellow' })
        if self.score_yellow == 6:
            self.socket_publisher.publish({ 'message': 'YELLOW TEAM WINS', 'score_black': self.score_black, 'score_yellow': self.score_yellow })
            self.event_publisher.publish('game_ended', { 'winner': 'yellow', 'score_black': self.score_black, 'score_yellow': self.score_yellow })
            time.sleep(15)
            self.start()
        else:
            self.socket_publisher.publish({ 'message': '', 'score_black': self.score_black, 'score_yellow': self.score_yellow })

    def start(self):
        self.score_black = 0
        self.score_yellow = 0
        self.socket_publisher.publish({ 'message': "Let's play!", 'score_black': self.score_black, 'score_yellow': self.score_yellow })
