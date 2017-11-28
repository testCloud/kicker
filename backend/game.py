class Game:
    def __init__(self, event_publisher):
        self.event_publisher = event_publisher
        self.reset()

    def goal_for_black(self):
        self.event_publisher.publish('goal', { 'team': 'black' })
        self.score_black += 1

    def goal_for_yellow(self):
        self.event_publisher.publish('goal', { 'team': 'yellow' })
        self.score_yellow += 1

    def reset(self):
        self.score_black = 0
        self.score_yellow = 0
