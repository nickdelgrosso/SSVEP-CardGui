from psychopy import visual, core

class BlinkingImage:
    
    def __init__(self, win, blink_frequency = 10., **kwargs):
        self.win = win
        self.image = visual.ImageStim(win=win, **kwargs)
        self.blink_frequency = blink_frequency
        self.clock = core.CountdownTimer(1. / blink_frequency)

    def update(self):
        # Turn on or off automatically
        time = self.win.getFutureFlipTime(clock=self.clock)
        if time >= 0:
            self.clock.add(self.clock._countdown_duration)
        self.image.setAutoDraw(time < -self.clock._countdown_duration / 2.)
    