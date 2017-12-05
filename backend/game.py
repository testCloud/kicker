class Game:
    def __init__(self, event_publisher):
        self.event_publisher = event_publisher
        self.reset()

    def goal_for_black(self):
        self.score_black += 1
        self.event_publisher.publish({ 'black': self.score_black}, { 'yellow': self.score_yellow })
        if self.score_black == 6
            self.event_publisher.publish({ 'message': 'BLACK TEAM WINS', 'black': self.score_black, 'yellow': self.score_yellow })
            time.sleep(15)
            self.start()

    def goal_for_yellow(self):
        self.score_yellow += 1
        self.event_publisher.publish({ 'black': self.score_black, 'yellow': self.score_yellow })
        if self.score_yellow == 6
            self.event_publisher.publish({ 'message': 'YELLOW TEAM WINS', 'black': self.score_black, 'yellow': self.score_yellow })
            time.sleep(15)
            self.start()

    def start(self):
        self.score_black = 0
        self.score_yellow = 0
        self.event_publisher.publish({ 'message': '', 'black': self.score_black, 'yellow': self.score_yellow })
