from psychopy import visual, core

class BlinkingImage:
    
    def __init__(self, win, blink_frequency = 10., **kwargs):
        self.win = win
        self.image = visual.ImageStim(win=win, **kwargs)
        self.clock = core.CountdownTimer(1. / blink_frequency)
        self.blink_frequency = blink_frequency

    @property
    def blink_frequency(self):
        return self._blink_frequency
    
    @blink_frequency.setter
    def blink_frequency(self, value: float):
        self._blink_frequency = value
        self.clock.reset(.5 / value)

    def update_draw(self):
        # Turn on or off automatically
        time_to_flip = -self.win.getFutureFlipTime(clock=self.clock)
        if time_to_flip <= 0:
            self.clock.reset()
            self.clock.add(time_to_flip)
            self.image.opacity = not self.image.opacity
            
    def draw(self):
        self.image.draw()
    