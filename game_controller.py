class Run:
    def __init__(self, playing_state, stopped_state):
        self.states = ["PLAYING", "STOPPED", "EXIT"]
        self.state = "PLAYING"
        self.running = True
        self.playing_state = playing_state
        self.stopper_state = stopped_state
    def run(self):
        while self.running:

            if self.state == "PLAYING":
                play = self.playing_state.play()

                if play in self.states:
                    self.state = play

            elif self.state == "EXIT":
                self.running = False

            elif self.state == "STOPPED":
                stopped = self.stopper_state.stop()
                if stopped in self.states:
                    self.state = stopped
