#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.0),
    on June 04, 2019, at 21:45
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.0'
expName = 'Probabilistic Learning'  # from the Builder filename that created this script
expInfo = {'Participant ID*': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\uni\\PhD\\Tasks\\Probabilistic Learning Pavlovia\\Probabilistic Learning_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='\nPlease follow the instructions on the following screens.\n\n\nTo select a symbol on a given side of the screen, use the keys below:\n\nLeft  side =  C          Right side = M\n\n\nPress any key to continue. \n',
    font='Calibri',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Prep_Instruction"
Prep_InstructionClock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text='Short Preparation session. \n\nYou will be collecting points.\n\nChoose one symbol either on the left (C) or the right (M). \n\nOne symbol is more likely to give you 10 points.\nThe other symbol is more likely to take away 10 points. \n\nChoose the symbol that is the most likely to give you points and avoid the symbol that makes you lose points.\n\n\nPress any key to continue.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "prep"
prepClock = core.Clock()
fixation0 = visual.TextStim(win=win, name='fixation0',
    text='+',
    font='Calibri',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
letterpic0_1 = visual.ImageStim(
    win=win,
    name='letterpic0_1', 
    image='sin', mask=None,
    ori=0, pos=(-0.1, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
letterpic0_2 = visual.ImageStim(
    win=win,
    name='letterpic0_2', 
    image='sin', mask=None,
    ori=0, pos=(0.1, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "prep_feedback"
prep_feedbackClock = core.Clock()
prep_feedb = visual.TextStim(win=win, name='prep_feedb',
    text='default text',
    font='Calibri',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Prep_over"
Prep_overClock = core.Clock()
prep_outro = visual.TextStim(win=win, name='prep_outro',
    text='The practice session is now finished.\n\nYou may have noticed that one of the symbols was more likely to give you points. \n\nThis was not always the case. \n\nIt was more PROBABLE that one symbol gave you points. \n\n\nPress any key to continue. ',
    font='Calibri',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Practice_Instruction"
Practice_InstructionClock = core.Clock()
myCount = 0


pract_intr = visual.TextStim(win=win, name='pract_intr',
    text='Training Session\n\nYou will see 3 pairs of symbols. \n\nIn each pair, one symbol is more PROBABLE to give you points. \n\nIdentify those symbols and choose them.\nAvoid symbols that make you lose points. \n\nUse buttons:\nleft(C)            right(M)\nto make your choices. \n\n\nPress any key to begin.\n',
    font='Calibri',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
from numpy.random import random

#create empty variables

myCount1 = 0
myCount2 = 0
myCount3 = 0

#create emoty lists

resp1 = []
resp2 = []
resp3 = []

resplist1 = []
resplist2 = []
resplist3 = []

Corr1 = []
Corr2 = []
Corr3 = []



fixation1 = visual.TextStim(win=win, name='fixation1',
    text='+',
    font='Calibri',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
letter1_1 = visual.TextStim(win=win, name='letter1_1',
    text='default text',
    font='hiragana tfb',
    pos=[-0.1,0], height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
letter1_2 = visual.TextStim(win=win, name='letter1_2',
    text='default text',
    font='hiragana tfb',
    pos=[0.1,0], height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
blank_feed = visual.TextStim(win=win, name='blank_feed',
    text=None,
    font='Calibri',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feedb = visual.TextStim(win=win, name='feedb',
    text='default text',
    font='Calibri',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Practice_over"
Practice_overClock = core.Clock()
instr2 = visual.TextStim(win=win, name='instr2',
    text='The training session is now finished. \n\nPress any key to continue onto the next section.\n',
    font='Calibri',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Test_Instr"
Test_InstrClock = core.Clock()
instr3 = visual.TextStim(win=win, name='instr3',
    text='Test Session\n\nYou will see the same symbols again. \n\nNow, in different order and combination. \n\nPick the symbol that is the most PROBABLE to give you points.\nAvoid the symbol that makes you lose points.\n\nUse buttons:\nleft(C)            right(M)\n\nMake your decision as quickly as you can.\nIf you are unsure go with your gut feeling.\n\n\nPress any key to begin.\n',
    font='Calibri',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "test_trial"
test_trialClock = core.Clock()
posLB = []
negLV = []
fixation2 = visual.TextStim(win=win, name='fixation2',
    text='+',
    font='Calibri',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
letter2_1 = visual.TextStim(win=win, name='letter2_1',
    text='default text',
    font='hiragana tfb',
    pos=(-0.1, 0), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
letter2_2 = visual.TextStim(win=win, name='letter2_2',
    text='default text',
    font='hiragana tfb',
    pos=(0.1, 0), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "check_instr"
check_instrClock = core.Clock()
check = visual.TextStim(win=win, name='check',
    text='Well done!\n\nNow think about the symbols you saw. \n\nWhich symbol was the MOST likely to give you ponts? \n\nWhich symbol was the LEAST likely to give you points? \n\nOn the next screen, use numbers:\n1  2  3  4  5  or  6 on top of the keyboard.\n\nIdentify the symbols of your choice. \n\n\nPress any key to continue.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Learning_Check"
Learning_CheckClock = core.Clock()
quest = visual.TextStim(win=win, name='quest',
    text='default text',
    font='Arial',
    pos=(0, 0.15), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
letter_string = visual.TextStim(win=win, name='letter_string',
    text='default text',
    font='hiragana tfb',
    pos=(0, 0.0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
number_string = visual.TextStim(win=win, name='number_string',
    text='default text',
    font='Arial',
    pos=(0, -0.1), height=0.08, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "test_over"
test_overClock = core.Clock()
t_outro = visual.TextStim(win=win, name='t_outro',
    text='The test phase is now finished. \nYou can take a break before continuing. \n\nOtherwise press any key to continue.',
    font='Calibri',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "task_over"
task_overClock = core.Clock()
task_outro = visual.TextStim(win=win, name='task_outro',
    text='Thank you, the learning task is now finished.\n\nYou can press Esc to exit the full screen. \n\nYou can then close this window. ',
    font='Calibri',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
t = 0
WelcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
welc_resp = keyboard.Keyboard()
# keep track of which components have finished
WelcomeComponents = [text, welc_resp]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # not accounting for scr refresh
        text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *welc_resp* updates
    if t >= 0.0 and welc_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        welc_resp.tStart = t  # not accounting for scr refresh
        welc_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(welc_resp, 'tStartRefresh')  # time at next scr refresh
        welc_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(welc_resp.clock.reset)  # t=0 on next screen flip
        welc_resp.clearEvents(eventType='keyboard')
    if welc_resp.status == STARTED:
        theseKeys = welc_resp.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            welc_resp.keys = theseKeys.name  # just the last key pressed
            welc_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if welc_resp.keys in ['', [], None]:  # No response was made
    welc_resp.keys = None
thisExp.addData('welc_resp.keys',welc_resp.keys)
if welc_resp.keys != None:  # we had a response
    thisExp.addData('welc_resp.rt', welc_resp.rt)
thisExp.addData('welc_resp.started', welc_resp.tStartRefresh)
thisExp.addData('welc_resp.stopped', welc_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Prep_Instruction"-------
t = 0
Prep_InstructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
intr0_resp = keyboard.Keyboard()
# keep track of which components have finished
Prep_InstructionComponents = [instr1, intr0_resp]
for thisComponent in Prep_InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Prep_Instruction"-------
while continueRoutine:
    # get current time
    t = Prep_InstructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if t >= 0.0 and instr1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr1.tStart = t  # not accounting for scr refresh
        instr1.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        instr1.setAutoDraw(True)
    
    # *intr0_resp* updates
    if t >= 0.0 and intr0_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        intr0_resp.tStart = t  # not accounting for scr refresh
        intr0_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(intr0_resp, 'tStartRefresh')  # time at next scr refresh
        intr0_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(intr0_resp.clock.reset)  # t=0 on next screen flip
        intr0_resp.clearEvents(eventType='keyboard')
    if intr0_resp.status == STARTED:
        theseKeys = intr0_resp.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            intr0_resp.keys = theseKeys.name  # just the last key pressed
            intr0_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Prep_InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Prep_Instruction"-------
for thisComponent in Prep_InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr1.started', instr1.tStartRefresh)
thisExp.addData('instr1.stopped', instr1.tStopRefresh)
# check responses
if intr0_resp.keys in ['', [], None]:  # No response was made
    intr0_resp.keys = None
thisExp.addData('intr0_resp.keys',intr0_resp.keys)
if intr0_resp.keys != None:  # we had a response
    thisExp.addData('intr0_resp.rt', intr0_resp.rt)
thisExp.addData('intr0_resp.started', intr0_resp.tStartRefresh)
thisExp.addData('intr0_resp.stopped', intr0_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Prep_Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
preparation = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('hiragana7.xlsx'),
    seed=None, name='preparation')
thisExp.addLoop(preparation)  # add the loop to the experiment
thisPreparation = preparation.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPreparation.rgb)
if thisPreparation != None:
    for paramName in thisPreparation:
        exec('{} = thisPreparation[paramName]'.format(paramName))

for thisPreparation in preparation:
    currentLoop = preparation
    # abbreviate parameter names if possible (e.g. rgb = thisPreparation.rgb)
    if thisPreparation != None:
        for paramName in thisPreparation:
            exec('{} = thisPreparation[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "prep"-------
    t = 0
    prepClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    letterpic0_1.setImage(letter10)
    letterpic0_2.setImage(letter20)
    prep_resp = keyboard.Keyboard()
    # keep track of which components have finished
    prepComponents = [fixation0, letterpic0_1, letterpic0_2, prep_resp]
    for thisComponent in prepComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "prep"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prepClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation0* updates
        if t >= 0.0 and fixation0.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation0.tStart = t  # not accounting for scr refresh
            fixation0.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fixation0, 'tStartRefresh')  # time at next scr refresh
            fixation0.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation0.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fixation0.tStop = t  # not accounting for scr refresh
            fixation0.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation0, 'tStopRefresh')  # time at next scr refresh
            fixation0.setAutoDraw(False)
        
        # *letterpic0_1* updates
        if t >= 0.5 and letterpic0_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            letterpic0_1.tStart = t  # not accounting for scr refresh
            letterpic0_1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(letterpic0_1, 'tStartRefresh')  # time at next scr refresh
            letterpic0_1.setAutoDraw(True)
        frameRemains = 0.5 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if letterpic0_1.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            letterpic0_1.tStop = t  # not accounting for scr refresh
            letterpic0_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(letterpic0_1, 'tStopRefresh')  # time at next scr refresh
            letterpic0_1.setAutoDraw(False)
        
        # *letterpic0_2* updates
        if t >= 0.5 and letterpic0_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            letterpic0_2.tStart = t  # not accounting for scr refresh
            letterpic0_2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(letterpic0_2, 'tStartRefresh')  # time at next scr refresh
            letterpic0_2.setAutoDraw(True)
        frameRemains = 0.5 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if letterpic0_2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            letterpic0_2.tStop = t  # not accounting for scr refresh
            letterpic0_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(letterpic0_2, 'tStopRefresh')  # time at next scr refresh
            letterpic0_2.setAutoDraw(False)
        
        # *prep_resp* updates
        if t >= 0.5 and prep_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            prep_resp.tStart = t  # not accounting for scr refresh
            prep_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prep_resp, 'tStartRefresh')  # time at next scr refresh
            prep_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(prep_resp.clock.reset)  # t=0 on next screen flip
            prep_resp.clearEvents(eventType='keyboard')
        frameRemains = 0.5 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if prep_resp.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            prep_resp.tStop = t  # not accounting for scr refresh
            prep_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prep_resp, 'tStopRefresh')  # time at next scr refresh
            prep_resp.status = FINISHED
        if prep_resp.status == STARTED:
            theseKeys = prep_resp.getKeys(keyList=['c', 'm'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if prep_resp.keys == []:  # then this was the first keypress
                    prep_resp.keys = theseKeys.name  # just the first key pressed
                    prep_resp.rt = theseKeys.rt
                    # was this 'correct'?
                    if (prep_resp.keys == str(corrAns0)) or (prep_resp.keys == corrAns0):
                        prep_resp.corr = 1
                    else:
                        prep_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prep"-------
    for thisComponent in prepComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    preparation.addData('fixation0.started', fixation0.tStartRefresh)
    preparation.addData('fixation0.stopped', fixation0.tStopRefresh)
    preparation.addData('letterpic0_1.started', letterpic0_1.tStartRefresh)
    preparation.addData('letterpic0_1.stopped', letterpic0_1.tStopRefresh)
    preparation.addData('letterpic0_2.started', letterpic0_2.tStartRefresh)
    preparation.addData('letterpic0_2.stopped', letterpic0_2.tStopRefresh)
    # check responses
    if prep_resp.keys in ['', [], None]:  # No response was made
        prep_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns0).lower() == 'none':
           prep_resp.corr = 1;  # correct non-response
        else:
           prep_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for preparation (TrialHandler)
    preparation.addData('prep_resp.keys',prep_resp.keys)
    preparation.addData('prep_resp.corr', prep_resp.corr)
    if prep_resp.keys != None:  # we had a response
        preparation.addData('prep_resp.rt', prep_resp.rt)
    preparation.addData('prep_resp.started', prep_resp.tStartRefresh)
    preparation.addData('prep_resp.stopped', prep_resp.tStopRefresh)
    
    # ------Prepare to start Routine "prep_feedback"-------
    t = 0
    prep_feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.600000)
    # update component parameters for each repeat
    if prep_resp.corr:
        msg0='+10'
        msgColor='green'
    
    if not prep_resp.corr:
        msg0='-10'
        msgColor='red'
    
    if not prep_resp.keys:
        msg0='No response detected'
    prep_feedb.setColor(msgColor, colorSpace='rgb')
    prep_feedb.setText(msg0)
    # keep track of which components have finished
    prep_feedbackComponents = [prep_feedb]
    for thisComponent in prep_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "prep_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prep_feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prep_feedb* updates
        if t >= 0.0 and prep_feedb.status == NOT_STARTED:
            # keep track of start time/frame for later
            prep_feedb.tStart = t  # not accounting for scr refresh
            prep_feedb.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prep_feedb, 'tStartRefresh')  # time at next scr refresh
            prep_feedb.setAutoDraw(True)
        frameRemains = 0.0 + 0.6- win.monitorFramePeriod * 0.75  # most of one frame period left
        if prep_feedb.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            prep_feedb.tStop = t  # not accounting for scr refresh
            prep_feedb.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prep_feedb, 'tStopRefresh')  # time at next scr refresh
            prep_feedb.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prep_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prep_feedback"-------
    for thisComponent in prep_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    preparation.addData('prep_feedb.started', prep_feedb.tStartRefresh)
    preparation.addData('prep_feedb.stopped', prep_feedb.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'preparation'


# ------Prepare to start Routine "Prep_over"-------
t = 0
Prep_overClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
outro_resp = keyboard.Keyboard()
# keep track of which components have finished
Prep_overComponents = [prep_outro, outro_resp]
for thisComponent in Prep_overComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Prep_over"-------
while continueRoutine:
    # get current time
    t = Prep_overClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prep_outro* updates
    if t >= 0.0 and prep_outro.status == NOT_STARTED:
        # keep track of start time/frame for later
        prep_outro.tStart = t  # not accounting for scr refresh
        prep_outro.frameNStart = frameN  # exact frame index
        win.timeOnFlip(prep_outro, 'tStartRefresh')  # time at next scr refresh
        prep_outro.setAutoDraw(True)
    
    # *outro_resp* updates
    if t >= 0.0 and outro_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        outro_resp.tStart = t  # not accounting for scr refresh
        outro_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(outro_resp, 'tStartRefresh')  # time at next scr refresh
        outro_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(outro_resp.clock.reset)  # t=0 on next screen flip
        outro_resp.clearEvents(eventType='keyboard')
    if outro_resp.status == STARTED:
        theseKeys = outro_resp.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            outro_resp.keys = theseKeys.name  # just the last key pressed
            outro_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Prep_overComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Prep_over"-------
for thisComponent in Prep_overComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('prep_outro.started', prep_outro.tStartRefresh)
thisExp.addData('prep_outro.stopped', prep_outro.tStopRefresh)
# check responses
if outro_resp.keys in ['', [], None]:  # No response was made
    outro_resp.keys = None
thisExp.addData('outro_resp.keys',outro_resp.keys)
if outro_resp.keys != None:  # we had a response
    thisExp.addData('outro_resp.rt', outro_resp.rt)
thisExp.addData('outro_resp.started', outro_resp.tStartRefresh)
thisExp.addData('outro_resp.stopped', outro_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Prep_over" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
letterMaster = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('letterchoice.xlsx'),
    seed=None, name='letterMaster')
thisExp.addLoop(letterMaster)  # add the loop to the experiment
thisLetterMaster = letterMaster.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLetterMaster.rgb)
if thisLetterMaster != None:
    for paramName in thisLetterMaster:
        exec('{} = thisLetterMaster[paramName]'.format(paramName))

for thisLetterMaster in letterMaster:
    currentLoop = letterMaster
    # abbreviate parameter names if possible (e.g. rgb = thisLetterMaster.rgb)
    if thisLetterMaster != None:
        for paramName in thisLetterMaster:
            exec('{} = thisLetterMaster[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Practice_Instruction"-------
    t = 0
    Practice_InstructionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    myCount = myCount + 1
    
    if myCount == 3:
        letterMaster.finished = True
    
    
    
    instr1_resp = keyboard.Keyboard()
    # keep track of which components have finished
    Practice_InstructionComponents = [pract_intr, instr1_resp]
    for thisComponent in Practice_InstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Practice_Instruction"-------
    while continueRoutine:
        # get current time
        t = Practice_InstructionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pract_intr* updates
        if t >= 0.0 and pract_intr.status == NOT_STARTED:
            # keep track of start time/frame for later
            pract_intr.tStart = t  # not accounting for scr refresh
            pract_intr.frameNStart = frameN  # exact frame index
            win.timeOnFlip(pract_intr, 'tStartRefresh')  # time at next scr refresh
            pract_intr.setAutoDraw(True)
        
        # *instr1_resp* updates
        if t >= 0.0 and instr1_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr1_resp.tStart = t  # not accounting for scr refresh
            instr1_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(instr1_resp, 'tStartRefresh')  # time at next scr refresh
            instr1_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(instr1_resp.clock.reset)  # t=0 on next screen flip
            instr1_resp.clearEvents(eventType='keyboard')
        if instr1_resp.status == STARTED:
            theseKeys = instr1_resp.getKeys(keyList=None, waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if instr1_resp.keys == []:  # then this was the first keypress
                    instr1_resp.keys = theseKeys.name  # just the first key pressed
                    instr1_resp.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_InstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_Instruction"-------
    for thisComponent in Practice_InstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    letterMaster.addData('pract_intr.started', pract_intr.tStartRefresh)
    letterMaster.addData('pract_intr.stopped', pract_intr.tStopRefresh)
    # check responses
    if instr1_resp.keys in ['', [], None]:  # No response was made
        instr1_resp.keys = None
    letterMaster.addData('instr1_resp.keys',instr1_resp.keys)
    if instr1_resp.keys != None:  # we had a response
        letterMaster.addData('instr1_resp.rt', instr1_resp.rt)
    letterMaster.addData('instr1_resp.started', instr1_resp.tStartRefresh)
    letterMaster.addData('instr1_resp.stopped', instr1_resp.tStopRefresh)
    # the Routine "Practice_Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice = data.TrialHandler(nReps=6, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(letterset),
        seed=None, name='practice')
    thisExp.addLoop(practice)  # add the loop to the experiment
    thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    for thisPractice in practice:
        currentLoop = practice
        # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
        if thisPractice != None:
            for paramName in thisPractice:
                exec('{} = thisPractice[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # make a count of trials for each pair of letters (A&B, C&D, E&F)
        if (myCount == 1):
            myCount1 = myCount1 + 1
        else:
            myCount1 = myCount1 + 0
        
        if (myCount == 2):
            myCount2 = myCount2 + 1
        else:
            myCount2 = myCount2 + 0
        
        if (myCount == 3):
            myCount3 = myCount3 + 1
        else:
            myCount3 = myCount3 + 0
        
        #Monitor the number of A, C and E responses in the last 60 trials
        #Separate for all three runs of the procedure
        
        if myCount == 1 and (sum(resplist1[-60:]) > 13 and sum(resplist2[-60:]) > 11 and sum(resplist3[-60:]) > 9 and myCount1 > 59):
            practice.finished = True
        
        if myCount == 2 and (sum(resplist1[-60:]) > 13 and sum(resplist2[-60:]) > 11 and sum(resplist3[-60:]) > 9 and myCount2 > 59):
            practice.finished = True
        
        if myCount == 3 and (sum(resplist1[-60:]) > 13 and sum(resplist2[-60:]) > 11 and sum(resplist3[-60:]) > 9 and myCount3 > 59):
            practice.finished = True
        
        
        jitter = random() * (0.8 - 0.3) + 0.3
        jitter = round(jitter, 1) # round to 1 decimal place
        jitter2 = random() * (1.0-0.5) + 0.5
        letter1_1.setText(letter1)
        letter1_2.setText(letter2)
        resp = keyboard.Keyboard()
        # keep track of which components have finished
        trialComponents = [fixation1, letter1_1, letter1_2, resp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            
            
            # *fixation1* updates
            if t >= 0.0 and fixation1.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation1.tStart = t  # not accounting for scr refresh
                fixation1.frameNStart = frameN  # exact frame index
                win.timeOnFlip(fixation1, 'tStartRefresh')  # time at next scr refresh
                fixation1.setAutoDraw(True)
            frameRemains = 0.0 + jitter- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation1.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                fixation1.tStop = t  # not accounting for scr refresh
                fixation1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation1, 'tStopRefresh')  # time at next scr refresh
                fixation1.setAutoDraw(False)
            
            # *letter1_1* updates
            if t >= jitter and letter1_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                letter1_1.tStart = t  # not accounting for scr refresh
                letter1_1.frameNStart = frameN  # exact frame index
                win.timeOnFlip(letter1_1, 'tStartRefresh')  # time at next scr refresh
                letter1_1.setAutoDraw(True)
            frameRemains = jitter + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if letter1_1.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                letter1_1.tStop = t  # not accounting for scr refresh
                letter1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter1_1, 'tStopRefresh')  # time at next scr refresh
                letter1_1.setAutoDraw(False)
            
            # *letter1_2* updates
            if t >= jitter and letter1_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                letter1_2.tStart = t  # not accounting for scr refresh
                letter1_2.frameNStart = frameN  # exact frame index
                win.timeOnFlip(letter1_2, 'tStartRefresh')  # time at next scr refresh
                letter1_2.setAutoDraw(True)
            frameRemains = jitter + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if letter1_2.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                letter1_2.tStop = t  # not accounting for scr refresh
                letter1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter1_2, 'tStopRefresh')  # time at next scr refresh
                letter1_2.setAutoDraw(False)
            
            # *resp* updates
            if t >= jitter and resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp.tStart = t  # not accounting for scr refresh
                resp.frameNStart = frameN  # exact frame index
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                resp.clearEvents(eventType='keyboard')
            frameRemains = jitter + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if resp.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                resp.tStop = t  # not accounting for scr refresh
                resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                resp.status = FINISHED
            if resp.status == STARTED:
                theseKeys = resp.getKeys(keyList=['c', 'm'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if resp.keys == []:  # then this was the first keypress
                        resp.keys = theseKeys.name  # just the first key pressed
                        resp.rt = theseKeys.rt
                        # was this 'correct'?
                        if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                            resp.corr = 1
                        else:
                            resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #count how many times participants chose letters A, C and E
        if (resp.keys == letterA):
            resp1 = 1
        else:
            resp1 = 0
        
        if (resp.keys == letterC):
            resp2 = 1
        else:
            resp2 = 0
        
        if (resp.keys == letterE):
            resp3 = 1
        else:
            resp3 = 0
        
        resplist1.append(resp1)
        resplist2.append(resp2)
        resplist3.append(resp3)
        
        Corr1 = sum(resplist1[-60:])
        Corr2 = sum(resplist2[-60:])
        Corr3 = sum(resplist3[-60:])
        
        
        #add a variable in the output that will record when participants
        #respond with A C or E in the learning phase
        practice.addData('resp1', resp1)
        
        practice.addData('resp2', resp2)
        
        practice.addData('resp3', resp3)
        
        
        practice.addData('response1', resplist1[0:10])
        
        practice.addData('response2', resplist2[0:10])
        
        practice.addData('response3', resplist3[0:10])
        
        #add a variable in the output that will count the 
        # performance on different letter pairs
        practice.addData('Corr1', Corr1)
        
        practice.addData('Corr2', Corr2)
        
        practice.addData('Corr3', Corr3)
        
        practice.addData('jitter', jitter)
        
        #add a variable that will count in the output
        # how many times the learning phase and the testing
        # phase occur
        
        practice.addData('myCount1', myCount1)
        practice.addData('myCount2', myCount2)
        practice.addData('myCount3', myCount3)
        
        practice.addData('myCount', myCount)
        practice.addData('fixation1.started', fixation1.tStartRefresh)
        practice.addData('fixation1.stopped', fixation1.tStopRefresh)
        practice.addData('letter1_1.started', letter1_1.tStartRefresh)
        practice.addData('letter1_1.stopped', letter1_1.tStopRefresh)
        practice.addData('letter1_2.started', letter1_2.tStartRefresh)
        practice.addData('letter1_2.stopped', letter1_2.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for practice (TrialHandler)
        practice.addData('resp.keys',resp.keys)
        practice.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            practice.addData('resp.rt', resp.rt)
        practice.addData('resp.started', resp.tStartRefresh)
        practice.addData('resp.stopped', resp.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.950000)
        # update component parameters for each repeat
        if resp.corr:
            msg='+10'
            msgColor='green'
        
        if not resp.corr:
            msg='-10'
            msgColor='red'
        
        if not resp.keys:
            msg='No response detected'
        feedb.setColor(msgColor, colorSpace='rgb')
        feedb.setText(msg)
        # keep track of which components have finished
        feedbackComponents = [blank_feed, feedb]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank_feed* updates
            if t >= 0.0 and blank_feed.status == NOT_STARTED:
                # keep track of start time/frame for later
                blank_feed.tStart = t  # not accounting for scr refresh
                blank_feed.frameNStart = frameN  # exact frame index
                win.timeOnFlip(blank_feed, 'tStartRefresh')  # time at next scr refresh
                blank_feed.setAutoDraw(True)
            frameRemains = 0.0 + 0.35- win.monitorFramePeriod * 0.75  # most of one frame period left
            if blank_feed.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                blank_feed.tStop = t  # not accounting for scr refresh
                blank_feed.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_feed, 'tStopRefresh')  # time at next scr refresh
                blank_feed.setAutoDraw(False)
            
            # *feedb* updates
            if t >= 0.35 and feedb.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedb.tStart = t  # not accounting for scr refresh
                feedb.frameNStart = frameN  # exact frame index
                win.timeOnFlip(feedb, 'tStartRefresh')  # time at next scr refresh
                feedb.setAutoDraw(True)
            frameRemains = 0.35 + 0.6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedb.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                feedb.tStop = t  # not accounting for scr refresh
                feedb.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedb, 'tStopRefresh')  # time at next scr refresh
                feedb.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice.addData('blank_feed.started', blank_feed.tStartRefresh)
        practice.addData('blank_feed.stopped', blank_feed.tStopRefresh)
        practice.addData('feedb.started', feedb.tStartRefresh)
        practice.addData('feedb.stopped', feedb.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 6 repeats of 'practice'
    
    
    # ------Prepare to start Routine "Practice_over"-------
    t = 0
    Practice_overClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    instr2_resp = keyboard.Keyboard()
    # keep track of which components have finished
    Practice_overComponents = [instr2, instr2_resp]
    for thisComponent in Practice_overComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Practice_over"-------
    while continueRoutine:
        # get current time
        t = Practice_overClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr2* updates
        if t >= 0.0 and instr2.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr2.tStart = t  # not accounting for scr refresh
            instr2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(instr2, 'tStartRefresh')  # time at next scr refresh
            instr2.setAutoDraw(True)
        
        # *instr2_resp* updates
        if t >= 0.0 and instr2_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr2_resp.tStart = t  # not accounting for scr refresh
            instr2_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(instr2_resp, 'tStartRefresh')  # time at next scr refresh
            instr2_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(instr2_resp.clock.reset)  # t=0 on next screen flip
            instr2_resp.clearEvents(eventType='keyboard')
        if instr2_resp.status == STARTED:
            theseKeys = instr2_resp.getKeys(keyList=None, waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if instr2_resp.keys == []:  # then this was the first keypress
                    instr2_resp.keys = theseKeys.name  # just the first key pressed
                    instr2_resp.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_overComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_over"-------
    for thisComponent in Practice_overComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    letterMaster.addData('instr2.started', instr2.tStartRefresh)
    letterMaster.addData('instr2.stopped', instr2.tStopRefresh)
    # check responses
    if instr2_resp.keys in ['', [], None]:  # No response was made
        instr2_resp.keys = None
    letterMaster.addData('instr2_resp.keys',instr2_resp.keys)
    if instr2_resp.keys != None:  # we had a response
        letterMaster.addData('instr2_resp.rt', instr2_resp.rt)
    letterMaster.addData('instr2_resp.started', instr2_resp.tStartRefresh)
    letterMaster.addData('instr2_resp.stopped', instr2_resp.tStopRefresh)
    # the Routine "Practice_over" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Test_Instr"-------
    t = 0
    Test_InstrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    instr3_resp = keyboard.Keyboard()
    # keep track of which components have finished
    Test_InstrComponents = [instr3, instr3_resp]
    for thisComponent in Test_InstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Test_Instr"-------
    while continueRoutine:
        # get current time
        t = Test_InstrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr3* updates
        if t >= 0.0 and instr3.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr3.tStart = t  # not accounting for scr refresh
            instr3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(instr3, 'tStartRefresh')  # time at next scr refresh
            instr3.setAutoDraw(True)
        
        # *instr3_resp* updates
        if t >= 0.0 and instr3_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr3_resp.tStart = t  # not accounting for scr refresh
            instr3_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(instr3_resp, 'tStartRefresh')  # time at next scr refresh
            instr3_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(instr3_resp.clock.reset)  # t=0 on next screen flip
            instr3_resp.clearEvents(eventType='keyboard')
        if instr3_resp.status == STARTED:
            theseKeys = instr3_resp.getKeys(keyList=None, waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                instr3_resp.keys = theseKeys.name  # just the last key pressed
                instr3_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_InstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_Instr"-------
    for thisComponent in Test_InstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    letterMaster.addData('instr3.started', instr3.tStartRefresh)
    letterMaster.addData('instr3.stopped', instr3.tStopRefresh)
    # check responses
    if instr3_resp.keys in ['', [], None]:  # No response was made
        instr3_resp.keys = None
    letterMaster.addData('instr3_resp.keys',instr3_resp.keys)
    if instr3_resp.keys != None:  # we had a response
        letterMaster.addData('instr3_resp.rt', instr3_resp.rt)
    letterMaster.addData('instr3_resp.started', instr3_resp.tStartRefresh)
    letterMaster.addData('instr3_resp.stopped', instr3_resp.tStopRefresh)
    # the Routine "Test_Instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    test = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(letterset2),
        seed=None, name='test')
    thisExp.addLoop(test)  # add the loop to the experiment
    thisTest = test.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest:
            exec('{} = thisTest[paramName]'.format(paramName))
    
    for thisTest in test:
        currentLoop = test
        # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
        if thisTest != None:
            for paramName in thisTest:
                exec('{} = thisTest[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "test_trial"-------
        t = 0
        test_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        jitter = random() * (0.8 - 0.3) + 0.3
        jitter = round(jitter, 1) # round to 1 decimal place
        jitter2 = random() * (1.0-0.5) + 0.5
        letter2_1.setText(letter3)
        letter2_2.setText(letter4)
        test_resp = keyboard.Keyboard()
        # keep track of which components have finished
        test_trialComponents = [fixation2, letter2_1, letter2_2, test_resp]
        for thisComponent in test_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "test_trial"-------
        while continueRoutine:
            # get current time
            t = test_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation2* updates
            if t >= 0.0 and fixation2.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation2.tStart = t  # not accounting for scr refresh
                fixation2.frameNStart = frameN  # exact frame index
                win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
                fixation2.setAutoDraw(True)
            frameRemains = 0.0 + jitter2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation2.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation2, 'tStopRefresh')  # time at next scr refresh
                fixation2.setAutoDraw(False)
            
            # *letter2_1* updates
            if t >= jitter2 and letter2_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                letter2_1.tStart = t  # not accounting for scr refresh
                letter2_1.frameNStart = frameN  # exact frame index
                win.timeOnFlip(letter2_1, 'tStartRefresh')  # time at next scr refresh
                letter2_1.setAutoDraw(True)
            frameRemains = jitter2 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if letter2_1.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                letter2_1.tStop = t  # not accounting for scr refresh
                letter2_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter2_1, 'tStopRefresh')  # time at next scr refresh
                letter2_1.setAutoDraw(False)
            
            # *letter2_2* updates
            if t >= jitter2 and letter2_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                letter2_2.tStart = t  # not accounting for scr refresh
                letter2_2.frameNStart = frameN  # exact frame index
                win.timeOnFlip(letter2_2, 'tStartRefresh')  # time at next scr refresh
                letter2_2.setAutoDraw(True)
            frameRemains = jitter2 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if letter2_2.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                letter2_2.tStop = t  # not accounting for scr refresh
                letter2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter2_2, 'tStopRefresh')  # time at next scr refresh
                letter2_2.setAutoDraw(False)
            
            # *test_resp* updates
            if t >= jitter2 and test_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                test_resp.tStart = t  # not accounting for scr refresh
                test_resp.frameNStart = frameN  # exact frame index
                win.timeOnFlip(test_resp, 'tStartRefresh')  # time at next scr refresh
                test_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(test_resp.clock.reset)  # t=0 on next screen flip
                test_resp.clearEvents(eventType='keyboard')
            frameRemains = jitter2 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if test_resp.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                test_resp.tStop = t  # not accounting for scr refresh
                test_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test_resp, 'tStopRefresh')  # time at next scr refresh
                test_resp.status = FINISHED
            if test_resp.status == STARTED:
                theseKeys = test_resp.getKeys(keyList=['c', 'm'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if test_resp.keys == []:  # then this was the first keypress
                        test_resp.keys = theseKeys.name  # just the first key pressed
                        test_resp.rt = theseKeys.rt
                        # a response ends the routine
                        continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "test_trial"-------
        for thisComponent in test_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        if (test_resp.keys == pickA):
            posLB = 1
        else:
            posLB = 0
        
        if (test_resp.keys == avoidB):
            negLB = 1
        else:
            negLB = 0
        
        
        test.addData('jitter', jitter)
        
        
        test.addData('posLB', posLB)
        test.addData('negLB', negLB)
        
        if myCount > 3:
            letterMaster.finished = True
        test.addData('fixation2.started', fixation2.tStartRefresh)
        test.addData('fixation2.stopped', fixation2.tStopRefresh)
        test.addData('letter2_1.started', letter2_1.tStartRefresh)
        test.addData('letter2_1.stopped', letter2_1.tStopRefresh)
        test.addData('letter2_2.started', letter2_2.tStartRefresh)
        test.addData('letter2_2.stopped', letter2_2.tStopRefresh)
        # check responses
        if test_resp.keys in ['', [], None]:  # No response was made
            test_resp.keys = None
        test.addData('test_resp.keys',test_resp.keys)
        if test_resp.keys != None:  # we had a response
            test.addData('test_resp.rt', test_resp.rt)
        test.addData('test_resp.started', test_resp.tStartRefresh)
        test.addData('test_resp.stopped', test_resp.tStopRefresh)
        # the Routine "test_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2 repeats of 'test'
    
    
    # ------Prepare to start Routine "check_instr"-------
    t = 0
    check_instrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    check_resp = keyboard.Keyboard()
    # keep track of which components have finished
    check_instrComponents = [check, check_resp]
    for thisComponent in check_instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "check_instr"-------
    while continueRoutine:
        # get current time
        t = check_instrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *check* updates
        if t >= 0.0 and check.status == NOT_STARTED:
            # keep track of start time/frame for later
            check.tStart = t  # not accounting for scr refresh
            check.frameNStart = frameN  # exact frame index
            win.timeOnFlip(check, 'tStartRefresh')  # time at next scr refresh
            check.setAutoDraw(True)
        
        # *check_resp* updates
        if t >= 0.0 and check_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            check_resp.tStart = t  # not accounting for scr refresh
            check_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(check_resp, 'tStartRefresh')  # time at next scr refresh
            check_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(check_resp.clock.reset)  # t=0 on next screen flip
            check_resp.clearEvents(eventType='keyboard')
        if check_resp.status == STARTED:
            theseKeys = check_resp.getKeys(keyList=None, waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                check_resp.keys = theseKeys.name  # just the last key pressed
                check_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in check_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "check_instr"-------
    for thisComponent in check_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    letterMaster.addData('check.started', check.tStartRefresh)
    letterMaster.addData('check.stopped', check.tStopRefresh)
    # check responses
    if check_resp.keys in ['', [], None]:  # No response was made
        check_resp.keys = None
    letterMaster.addData('check_resp.keys',check_resp.keys)
    if check_resp.keys != None:  # we had a response
        letterMaster.addData('check_resp.rt', check_resp.rt)
    letterMaster.addData('check_resp.started', check_resp.tStartRefresh)
    letterMaster.addData('check_resp.stopped', check_resp.tStopRefresh)
    # the Routine "check_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    checks = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(letterset3),
        seed=None, name='checks')
    thisExp.addLoop(checks)  # add the loop to the experiment
    thisCheck = checks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCheck.rgb)
    if thisCheck != None:
        for paramName in thisCheck:
            exec('{} = thisCheck[paramName]'.format(paramName))
    
    for thisCheck in checks:
        currentLoop = checks
        # abbreviate parameter names if possible (e.g. rgb = thisCheck.rgb)
        if thisCheck != None:
            for paramName in thisCheck:
                exec('{} = thisCheck[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Learning_Check"-------
        t = 0
        Learning_CheckClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        quest.setText(question)
        letter_string.setText(learnt_letters)
        number_string.setText('1    2    3    4    5    6')
        learnt_resp = keyboard.Keyboard()
        # keep track of which components have finished
        Learning_CheckComponents = [quest, letter_string, number_string, learnt_resp]
        for thisComponent in Learning_CheckComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Learning_Check"-------
        while continueRoutine:
            # get current time
            t = Learning_CheckClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *quest* updates
            if t >= 0.0 and quest.status == NOT_STARTED:
                # keep track of start time/frame for later
                quest.tStart = t  # not accounting for scr refresh
                quest.frameNStart = frameN  # exact frame index
                win.timeOnFlip(quest, 'tStartRefresh')  # time at next scr refresh
                quest.setAutoDraw(True)
            
            # *letter_string* updates
            if t >= 0.0 and letter_string.status == NOT_STARTED:
                # keep track of start time/frame for later
                letter_string.tStart = t  # not accounting for scr refresh
                letter_string.frameNStart = frameN  # exact frame index
                win.timeOnFlip(letter_string, 'tStartRefresh')  # time at next scr refresh
                letter_string.setAutoDraw(True)
            
            # *number_string* updates
            if t >= 0.0 and number_string.status == NOT_STARTED:
                # keep track of start time/frame for later
                number_string.tStart = t  # not accounting for scr refresh
                number_string.frameNStart = frameN  # exact frame index
                win.timeOnFlip(number_string, 'tStartRefresh')  # time at next scr refresh
                number_string.setAutoDraw(True)
            
            # *learnt_resp* updates
            if t >= 0.0 and learnt_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                learnt_resp.tStart = t  # not accounting for scr refresh
                learnt_resp.frameNStart = frameN  # exact frame index
                win.timeOnFlip(learnt_resp, 'tStartRefresh')  # time at next scr refresh
                learnt_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(learnt_resp.clock.reset)  # t=0 on next screen flip
                learnt_resp.clearEvents(eventType='keyboard')
            if learnt_resp.status == STARTED:
                theseKeys = learnt_resp.getKeys(keyList=['1', '2', '3', '4', '5', '6'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    learnt_resp.keys = theseKeys.name  # just the last key pressed
                    learnt_resp.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Learning_CheckComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Learning_Check"-------
        for thisComponent in Learning_CheckComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        checks.addData('quest.started', quest.tStartRefresh)
        checks.addData('quest.stopped', quest.tStopRefresh)
        checks.addData('letter_string.started', letter_string.tStartRefresh)
        checks.addData('letter_string.stopped', letter_string.tStopRefresh)
        checks.addData('number_string.started', number_string.tStartRefresh)
        checks.addData('number_string.stopped', number_string.tStopRefresh)
        # check responses
        if learnt_resp.keys in ['', [], None]:  # No response was made
            learnt_resp.keys = None
        checks.addData('learnt_resp.keys',learnt_resp.keys)
        if learnt_resp.keys != None:  # we had a response
            checks.addData('learnt_resp.rt', learnt_resp.rt)
        checks.addData('learnt_resp.started', learnt_resp.tStartRefresh)
        checks.addData('learnt_resp.stopped', learnt_resp.tStopRefresh)
        # the Routine "Learning_Check" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'checks'
    
    
    # ------Prepare to start Routine "test_over"-------
    t = 0
    test_overClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    outro_resp2 = keyboard.Keyboard()
    # keep track of which components have finished
    test_overComponents = [t_outro, outro_resp2]
    for thisComponent in test_overComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "test_over"-------
    while continueRoutine:
        # get current time
        t = test_overClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *t_outro* updates
        if t >= 0.0 and t_outro.status == NOT_STARTED:
            # keep track of start time/frame for later
            t_outro.tStart = t  # not accounting for scr refresh
            t_outro.frameNStart = frameN  # exact frame index
            win.timeOnFlip(t_outro, 'tStartRefresh')  # time at next scr refresh
            t_outro.setAutoDraw(True)
        
        # *outro_resp2* updates
        if t >= 0.0 and outro_resp2.status == NOT_STARTED:
            # keep track of start time/frame for later
            outro_resp2.tStart = t  # not accounting for scr refresh
            outro_resp2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(outro_resp2, 'tStartRefresh')  # time at next scr refresh
            outro_resp2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(outro_resp2.clock.reset)  # t=0 on next screen flip
            outro_resp2.clearEvents(eventType='keyboard')
        if outro_resp2.status == STARTED:
            theseKeys = outro_resp2.getKeys(keyList=None, waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                outro_resp2.keys = theseKeys.name  # just the last key pressed
                outro_resp2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_overComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test_over"-------
    for thisComponent in test_overComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    letterMaster.addData('t_outro.started', t_outro.tStartRefresh)
    letterMaster.addData('t_outro.stopped', t_outro.tStopRefresh)
    # check responses
    if outro_resp2.keys in ['', [], None]:  # No response was made
        outro_resp2.keys = None
    letterMaster.addData('outro_resp2.keys',outro_resp2.keys)
    if outro_resp2.keys != None:  # we had a response
        letterMaster.addData('outro_resp2.rt', outro_resp2.rt)
    letterMaster.addData('outro_resp2.started', outro_resp2.tStartRefresh)
    letterMaster.addData('outro_resp2.stopped', outro_resp2.tStopRefresh)
    # the Routine "test_over" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'letterMaster'


# ------Prepare to start Routine "task_over"-------
t = 0
task_overClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
outro2_resp = keyboard.Keyboard()
# keep track of which components have finished
task_overComponents = [task_outro, outro2_resp]
for thisComponent in task_overComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "task_over"-------
while continueRoutine:
    # get current time
    t = task_overClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *task_outro* updates
    if t >= 0.0 and task_outro.status == NOT_STARTED:
        # keep track of start time/frame for later
        task_outro.tStart = t  # not accounting for scr refresh
        task_outro.frameNStart = frameN  # exact frame index
        win.timeOnFlip(task_outro, 'tStartRefresh')  # time at next scr refresh
        task_outro.setAutoDraw(True)
    
    # *outro2_resp* updates
    if t >= 0.0 and outro2_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        outro2_resp.tStart = t  # not accounting for scr refresh
        outro2_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(outro2_resp, 'tStartRefresh')  # time at next scr refresh
        outro2_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(outro2_resp.clock.reset)  # t=0 on next screen flip
        outro2_resp.clearEvents(eventType='keyboard')
    if outro2_resp.status == STARTED:
        theseKeys = outro2_resp.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            if outro2_resp.keys == []:  # then this was the first keypress
                outro2_resp.keys = theseKeys.name  # just the first key pressed
                outro2_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in task_overComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "task_over"-------
for thisComponent in task_overComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('task_outro.started', task_outro.tStartRefresh)
thisExp.addData('task_outro.stopped', task_outro.tStopRefresh)
# check responses
if outro2_resp.keys in ['', [], None]:  # No response was made
    outro2_resp.keys = None
thisExp.addData('outro2_resp.keys',outro2_resp.keys)
if outro2_resp.keys != None:  # we had a response
    thisExp.addData('outro2_resp.rt', outro2_resp.rt)
thisExp.addData('outro2_resp.started', outro2_resp.tStartRefresh)
thisExp.addData('outro2_resp.stopped', outro2_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "task_over" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
