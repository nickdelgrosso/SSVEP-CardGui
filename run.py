from psychopy import visual, core, data
from psychopy.hardware.keyboard import Keyboard

from blinking_image import BlinkingImage

keyboard = Keyboard()

win = visual.Window(size=(1024, 768), fullscr=True, screen=0, winType='pyglet', units='height')

trials = data.TrialHandler(
    trialList=[
        {'freqLeft': 5, 'freqMiddle': 10, 'freqRight': 20}
    ],
    nReps=1
)

images = [
    BlinkingImage(win=win, blink_frequency=trials.trialList[0]['freqLeft'], image='imgs/card5.png', pos=(-0.5, 0), size=(0.25, 0.25)),
    BlinkingImage(win=win, blink_frequency=trials.trialList[0]['freqMiddle'], image='imgs/card5.png', pos=(0.0, 0), size=(0.25, 0.25)),
    BlinkingImage(win=win, blink_frequency=trials.trialList[0]['freqRight'], image='imgs/card5.png', pos=(0.5, 0), size=(0.25, 0.25)),
]

while True:
    
    for image in images:
        image.update()
    if keyboard.getKeys(keyList=["escape"]):  # escape key to quit
        core.quit()
    
    win.flip()  # refresh the screen
    

# make sure everything is closed down
win.flip()
win.close()
core.quit()
