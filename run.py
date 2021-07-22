from psychopy import visual, core, data, logging
from psychopy.hardware.keyboard import Keyboard

from blinking_image import BlinkingImage

keyboard = Keyboard()


win = visual.Window(size=(1024, 768), fullscr=True, screen=0, winType='pyglet', units='height')

title = visual.TextStim(win, text="Pick a Card!", pos = (0, 0.25))

trials = data.TrialHandler(
    trialList=[
        # {'freqLeft': 3, 'freqMiddle': 5, 'freqRight': 8},
        # {'freqLeft': 7.5, 'freqMiddle': 4.3, 'freqRight': 6},
        {'freqLeft': 6, 'freqMiddle': 6, 'freqRight': 6},
    ],
    nReps=1,
    extraInfo={'duration': 40},
)

# experiment = data.ExperimentHandler(
#     name="Card SSVEP",
#     version="0.1",
#     dataFileName="myrun"
# )
logger = logging.LogFile(f="stimlog.txt", level=logging.EXP, filemode='w')

images = [
    BlinkingImage(win=win, image='imgs/card2.png', pos=(-0.5, -0.20), size=(0.25, 0.341), name="leftCard"),
    BlinkingImage(win=win, image='imgs/card7.png', pos=(0.0, -0.2), size=(0.25, 0.341), name="middleCard"),
    BlinkingImage(win=win, image='imgs/cardA.png', pos=(0.5, -0.2), size=(0.25, 0.341), name="rightCard"),
]

for trial in trials:
    print("Starting Trial", trials.thisN)
    
    trial_clock = core.MonotonicClock()
    images[0].blink_frequency = trial['freqLeft']
    images[1].blink_frequency = trial['freqMiddle']
    images[2].blink_frequency = trial['freqRight']
    
    while trial_clock.getTime() < trials.extraInfo['duration']:
        for image in images:
            image.draw()
            
        win.flip()  # refresh the screen
        
        if keyboard.getKeys(keyList=["escape"]):  # escape key to quit
            core.quit()
    
        
    

# make sure everything is closed down
win.flip()
win.close()
core.quit()
