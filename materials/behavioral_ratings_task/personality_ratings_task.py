#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.03), March 14, 2016, at 13:32
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'personality_ratings'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-0.569,-0.569,-0.569], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instruct = visual.TextStim(win=win, ori=0, name='instruct',
    text=u'For this task, you are going to be asked to rate yourself and your peers on a number of characteristics.\n\nWe ask you to be as honest as possible when making ratings of both yourself and your peers.\nFor some questions, you may not have a good idea how that characteristic applies to each of your peers. In these cases, we ask that you simply make your best guess as to how much that characteristic applies to that person.\n \nYour responses will remain confidential and will be detached from your name. \n\n\n\n\nTo continue, press the SPACE BAR.',    font=u'Arial',
    pos=[0, .2], height=0.05, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Instructions2"
Instructions2Clock = core.Clock()
instruct2 = visual.TextStim(win=win, ori=0, name='instruct2',
    text=u'You will be displayed with a question at the top of the screen and an array of ratings bars below them that look like the one below. For every name above the ratings bar, please use the mouse to click on the scale to rate that person on that characteristic. When the name above the ratings bar is your own name, please rate yourself on that characteristic.\n\nEach trial is self-paced and you may change your answers while the question is on the screen. However, you will not be allowed to move on to the next question until you have made a response for each person.\n\nWhen you are ready to begin, press SPACE BAR. ',    font=u'Arial',
    pos=[0, .2], height=.05, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
rating = visual.RatingScale(win=win, name='rating', marker=u'triangle', size=.5, pos=[0.0, -0.6], low=1, high=5, labels=[u'Disagree Strongly', u' Agree Strongly'], scale=u'John Doe', showAccept=False)

# Initialize components for Routine "others_ffi"
others_ffiClock = core.Clock()
question_text = visual.TextStim(win=win, ori=0, name='question_text',
    text='default text',    font='Arial',
    pos=[0, .8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
endtext = visual.TextStim(win=win, ori=0, name='endtext',
    text='Hit the space bar to continue',    font='Arial',
    pos=[0, -.9], height=0.05, wrapWidth=None,
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-1.0)
rating1 = visual.RatingScale(win=win, name='rating1', marker='triangle', size=.5, pos=[-0.6, 0.6], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'], showAccept=False)
rating2 = visual.RatingScale(win=win, name='rating2', marker='triangle', size=.5, pos=[-0.6, 0.4], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'], showAccept=False)
rating3 = visual.RatingScale(win=win, name='rating3', marker='triangle', size=.5, pos=[-0.6, 0.2], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'], showAccept=False)
rating4 = visual.RatingScale(win=win, name='rating4', marker='triangle', size=.5, pos=[-0.6, 0.0], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'], showAccept=False)
rating5 = visual.RatingScale(win=win, name='rating5', marker='triangle', size=.5, pos=[-0.6, -0.2], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating6 = visual.RatingScale(win=win, name='rating6', marker='triangle', size=.5, pos=[-0.6, -0.4], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating7 = visual.RatingScale(win=win, name='rating7', marker='triangle', size=.5, pos=[-0.6, -0.6], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'], showAccept=False)
rating8 = visual.RatingScale(win=win, name='rating8', marker='triangle', size=.5, pos=[-0.6, -0.8], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'], showAccept=False)
rating9 = visual.RatingScale(win=win, name='rating9', marker='triangle', size=.5, pos=[0.0, 0.6], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating10 = visual.RatingScale(win=win, name='rating10', marker='triangle', size=.5, pos=[0.0, 0.4], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating11 = visual.RatingScale(win=win, name='rating11', marker='triangle', size=.5, pos=[0.0, 0.2], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'], showAccept=False)
rating12 = visual.RatingScale(win=win, name='rating12', marker='triangle', size=.5, pos=[0.0, 0.0], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'], showAccept=False)
rating13 = visual.RatingScale(win=win, name='rating13', marker='triangle', size=.5, pos=[0.0, -0.2], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating14 = visual.RatingScale(win=win, name='rating14', marker='triangle', size=.5, pos=[0.0, -0.4], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating15 = visual.RatingScale(win=win, name='rating15', marker='triangle', size=.5, pos=[0.0, -0.6], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating16 = visual.RatingScale(win=win, name='rating16', marker='triangle', size=.5, pos=[0.0, -0.8], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating17 = visual.RatingScale(win=win, name='rating17', marker='triangle', size=.5, pos=[0.6, 0.6], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating18 = visual.RatingScale(win=win, name='rating18', marker='triangle', size=.5, pos=[0.6, 0.4], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating19 = visual.RatingScale(win=win, name='rating19', marker='triangle', size=.5, pos=[0.6, 0.2], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating20 = visual.RatingScale(win=win, name='rating20', marker='triangle', size=.5, pos=[0.6, 0.0], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating21 = visual.RatingScale(win=win, name='rating21', marker='triangle', size=.5, pos=[0.6, -0.2], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating22 = visual.RatingScale(win=win, name='rating22', marker='triangle', size=.5, pos=[0.6, -0.4], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating23 = visual.RatingScale(win=win, name='rating23', marker='triangle', size=.5, pos=[0.6, -0.6], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
rating24 = visual.RatingScale(win=win, name='rating24', marker='triangle', size=.5, pos=[0.6, -0.8], low=1, high=5, labels=['\nDisagree \nstrongly', ' \nAgree \nstrongly'],  showAccept=False)
# Initialize components for Routine "others_extras"
others_extrasClock = core.Clock()
question_text_other = visual.TextStim(win=win, ori=0, name='question_text_other',
    text='default text',    font='Arial',
    pos=[0, .8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
endtext_other = visual.TextStim(win=win, ori=0, name='endtext_other',
    text='Hit the space bar to continue',    font='Arial',
    pos=[0, -.9], height=0.05, wrapWidth=None,
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-1.0)
rating1_other = visual.RatingScale(win=win, name='rating1_other', marker='triangle', size=.5, pos=[-0.6, 0.6], low=1, high=5, labels=['\nNot at all', ' \nExtremely'], showAccept=False)
rating2_other = visual.RatingScale(win=win, name='rating2_other', marker='triangle', size=.5, pos=[-0.6, 0.4], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating3_other = visual.RatingScale(win=win, name='rating3_other', marker='triangle', size=.5, pos=[-0.6, 0.2], low=1, high=5, labels=['\nNot at all', ' \nExtremely'], showAccept=False)
rating4_other = visual.RatingScale(win=win, name='rating4_other', marker='triangle', size=.5, pos=[-0.6, 0.0], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating5_other = visual.RatingScale(win=win, name='rating5_other', marker='triangle', size=.5, pos=[-0.6, -0.2], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating6_other = visual.RatingScale(win=win, name='rating6_other', marker='triangle', size=.5, pos=[-0.6, -0.4], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating7_other = visual.RatingScale(win=win, name='rating7_other', marker='triangle', size=.5, pos=[-0.6, -0.6], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating8_other = visual.RatingScale(win=win, name='rating8_other', marker='triangle', size=.5, pos=[-0.6, -0.8], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating9_other = visual.RatingScale(win=win, name='rating9_other', marker='triangle', size=.5, pos=[0.0, 0.6], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating10_other = visual.RatingScale(win=win, name='rating10_other', marker='triangle', size=.5, pos=[0.0, 0.4], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating11_other = visual.RatingScale(win=win, name='rating11_other', marker='triangle', size=.5, pos=[0.0, 0.2], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating12_other = visual.RatingScale(win=win, name='rating12_other', marker='triangle', size=.5, pos=[0.0, 0.0], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating13_other = visual.RatingScale(win=win, name='rating13_other', marker='triangle', size=.5, pos=[0.0, -0.2], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating14_other = visual.RatingScale(win=win, name='rating14_other', marker='triangle', size=.5, pos=[0.0, -0.4], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating15_other = visual.RatingScale(win=win, name='rating15_other', marker='triangle', size=.5, pos=[0.0, -0.6], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating16_other = visual.RatingScale(win=win, name='rating16_other', marker='triangle', size=.5, pos=[0.0, -0.8], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating17_other = visual.RatingScale(win=win, name='rating17_other', marker='triangle', size=.5, pos=[0.6, 0.6], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating18_other = visual.RatingScale(win=win, name='rating18_other', marker='triangle', size=.5, pos=[0.6, 0.4], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating19_other = visual.RatingScale(win=win, name='rating19_other', marker='triangle', size=.5, pos=[0.6, 0.2], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating20_other = visual.RatingScale(win=win, name='rating20_other', marker='triangle', size=.5, pos=[0.6, 0.0], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating21_other = visual.RatingScale(win=win, name='rating21_other', marker='triangle', size=.5, pos=[0.6, -0.2], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating22_other = visual.RatingScale(win=win, name='rating22_other', marker='triangle', size=.5, pos=[0.6, -0.4], low=1, high=5, labels=['\nNot at all', ' \nExtremely'], showAccept=False)
rating23_other = visual.RatingScale(win=win, name='rating23_other', marker='triangle', size=.5, pos=[0.6, -0.6], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)
rating24_other = visual.RatingScale(win=win, name='rating24_other', marker='triangle', size=.5, pos=[0.6, -0.8], low=1, high=5, labels=['\nNot at all', ' \nExtremely'],  showAccept=False)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
start_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
start_resp.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(instruct)
InstructionsComponents.append(start_resp)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct* updates
    if t >= 0.0 and instruct.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct.tStart = t  # underestimates by a little under one frame
        instruct.frameNStart = frameN  # exact frame index
        instruct.setAutoDraw(True)
    
    # *start_resp* updates
    if t >= 2 and start_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        start_resp.tStart = t  # underestimates by a little under one frame
        start_resp.frameNStart = frameN  # exact frame index
        start_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(start_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if start_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            start_resp.keys = theseKeys[-1]  # just the last key pressed
            start_resp.rt = start_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start_resp.keys in ['', [], None]:  # No response was made
   start_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('start_resp.keys',start_resp.keys)
if start_resp.keys != None:  # we had a response
    thisExp.addData('start_resp.rt', start_resp.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Instructions2"-------
t = 0
Instructions2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
start_resp2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
start_resp2.status = NOT_STARTED
rating.reset()
# keep track of which components have finished
Instructions2Components = []
Instructions2Components.append(instruct2)
Instructions2Components.append(start_resp2)
Instructions2Components.append(rating)
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct2* updates
    if t >= 0.0 and instruct2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct2.tStart = t  # underestimates by a little under one frame
        instruct2.frameNStart = frameN  # exact frame index
        instruct2.setAutoDraw(True)
    
    # *start_resp2* updates
    if t >= 2 and start_resp2.status == NOT_STARTED:
        # keep track of start time/frame for later
        start_resp2.tStart = t  # underestimates by a little under one frame
        start_resp2.frameNStart = frameN  # exact frame index
        start_resp2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(start_resp2.clock.reset)  # t=0 on next screen flip
    if start_resp2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            start_resp2.keys = theseKeys[-1]  # just the last key pressed
            start_resp2.rt = start_resp2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # *rating* updates
    if t >= 0.0 and rating.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating.tStart = t  # underestimates by a little under one frame
        rating.frameNStart = frameN  # exact frame index
        rating.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions2"-------
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start_resp2.keys in ['', [], None]:  # No response was made
   start_resp2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('start_resp2.keys',start_resp2.keys)
if start_resp2.keys != None:  # we had a response
    thisExp.addData('start_resp2.rt', start_resp2.rt)
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating.response', rating.getRating())
thisExp.nextEntry()
# the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
others_ffi_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('list1_trials.xlsx'),
    seed=None, name='others_ffi_trials')
thisExp.addLoop(others_ffi_trials)  # add the loop to the experiment
thisOthers_ffi_trial = others_ffi_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisOthers_ffi_trial.rgb)
if thisOthers_ffi_trial != None:
    for paramName in thisOthers_ffi_trial.keys():
        exec(paramName + '= thisOthers_ffi_trial.' + paramName)

for thisOthers_ffi_trial in others_ffi_trials:
    currentLoop = others_ffi_trials
    # abbreviate parameter names if possible (e.g. rgb = thisOthers_ffi_trial.rgb)
    if thisOthers_ffi_trial != None:
        for paramName in thisOthers_ffi_trial.keys():
            exec(paramName + '= thisOthers_ffi_trial.' + paramName)
    
    #------Prepare to start Routine "others_ffi"-------
    t = 0
    others_ffiClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    question_text.setText(question)
    endtrial_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    endtrial_resp.status = NOT_STARTED
    rating1.reset()
    rating2.reset()
    rating3.reset()
    rating4.reset()
    rating5.reset()
    rating6.reset()
    rating7.reset()
    rating8.reset()
    rating9.reset()
    rating10.reset()
    rating11.reset()
    rating12.reset()
    rating13.reset()
    rating14.reset()
    rating15.reset()
    rating16.reset()
    rating17.reset()
    rating18.reset()
    rating19.reset()
    rating20.reset()
    rating21.reset()
    rating22.reset()
    rating23.reset()
    rating24.reset()
    
    rating1.setDescription(tar1)
    rating2.setDescription(tar2)
    rating3.setDescription(tar3)
    rating4.setDescription(tar4)
    rating5.setDescription(tar5)
    rating6.setDescription(tar6)
    rating7.setDescription(tar7)
    rating8.setDescription(tar8)
    rating9.setDescription(tar9)
    rating10.setDescription(tar10)
    rating11.setDescription(tar11)
    rating12.setDescription(tar12)
    rating13.setDescription(tar13)
    rating14.setDescription(tar14)
    rating15.setDescription(tar15)
    rating16.setDescription(tar16)
    rating17.setDescription(tar17)
    rating18.setDescription(tar18)
    rating19.setDescription(tar19)
    rating20.setDescription(tar20)
    rating21.setDescription(tar21)
    rating22.setDescription(tar22)
    rating23.setDescription(tar23)
    rating24.setDescription(tar24)
    
    # keep track of which components have finished
    others_ffiComponents = []
    others_ffiComponents.append(question_text)
    others_ffiComponents.append(endtext)
    others_ffiComponents.append(endtrial_resp)
    others_ffiComponents.append(rating1)
    others_ffiComponents.append(rating2)
    others_ffiComponents.append(rating3)
    others_ffiComponents.append(rating4)
    others_ffiComponents.append(rating5)
    others_ffiComponents.append(rating6)
    others_ffiComponents.append(rating7)
    others_ffiComponents.append(rating8)
    others_ffiComponents.append(rating9)
    others_ffiComponents.append(rating10)
    others_ffiComponents.append(rating11)
    others_ffiComponents.append(rating12)
    others_ffiComponents.append(rating13)
    others_ffiComponents.append(rating14)
    others_ffiComponents.append(rating15)
    others_ffiComponents.append(rating16)
    others_ffiComponents.append(rating17)
    others_ffiComponents.append(rating18)
    others_ffiComponents.append(rating19)
    others_ffiComponents.append(rating20)
    others_ffiComponents.append(rating21)
    others_ffiComponents.append(rating22)
    others_ffiComponents.append(rating23)
    others_ffiComponents.append(rating24)
    for thisComponent in others_ffiComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "others_ffi"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = others_ffiClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *question_text* updates
        if t >= 0.0 and question_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            question_text.tStart = t  # underestimates by a little under one frame
            question_text.frameNStart = frameN  # exact frame index
            question_text.setAutoDraw(True)
        
        # *endtext* updates
        if (rating1.getRating() > 0 and rating2.getRating() > 0 and rating3.getRating() > 0  and rating4.getRating() > 0  and rating5.getRating() > 0  and rating6.getRating() > 0   and rating7.getRating() > 0  and rating8.getRating() > 0  and rating9.getRating() > 0  and rating10.getRating() > 0  and rating11.getRating() > 0  and rating12.getRating() > 0  and rating13.getRating() > 0  and rating14.getRating() > 0  and rating15.getRating() > 0  and rating16.getRating() > 0  and rating17.getRating() > 0  and rating18.getRating() > 0  and rating19.getRating() > 0 and rating20.getRating() > 0 and rating21.getRating() > 0  and rating22.getRating() > 0  and rating23.getRating() > 0  and rating24.getRating() > 0   ) and endtext.status == NOT_STARTED:
            # keep track of start time/frame for later
            endtext.tStart = t  # underestimates by a little under one frame
            endtext.frameNStart = frameN  # exact frame index
            endtext.setAutoDraw(True)
        
        # *endtrial_resp* updates
        if (rating1.getRating() > 0 and rating2.getRating() > 0 and rating3.getRating() > 0  and rating4.getRating() > 0  and rating5.getRating() > 0  and rating6.getRating() > 0   and rating7.getRating() > 0  and rating8.getRating() > 0  and rating9.getRating() > 0  and rating10.getRating() > 0  and rating11.getRating() > 0  and rating12.getRating() > 0  and rating13.getRating() > 0  and rating14.getRating() > 0  and rating15.getRating() > 0  and rating16.getRating() > 0  and rating17.getRating() > 0  and rating18.getRating() > 0  and rating19.getRating() > 0 and rating20.getRating() > 0 and rating21.getRating() > 0  and rating22.getRating() > 0  and rating23.getRating() > 0  and rating24.getRating() > 0) and endtrial_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            endtrial_resp.tStart = t  # underestimates by a little under one frame
            endtrial_resp.frameNStart = frameN  # exact frame index
            endtrial_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(endtrial_resp.clock.reset)  # t=0 on next screen flip
        if endtrial_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                endtrial_resp.keys = theseKeys[-1]  # just the last key pressed
                endtrial_resp.rt = endtrial_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        # *rating1* updates
        if t >= 0.0 and rating1.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating1.tStart = t  # underestimates by a little under one frame
            rating1.frameNStart = frameN  # exact frame index
            rating1.setAutoDraw(True)
        # *rating2* updates
        if t >= 0.0 and rating2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating2.tStart = t  # underestimates by a little under one frame
            rating2.frameNStart = frameN  # exact frame index
            rating2.setAutoDraw(True)
        # *rating3* updates
        if t >= 0.0 and rating3.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating3.tStart = t  # underestimates by a little under one frame
            rating3.frameNStart = frameN  # exact frame index
            rating3.setAutoDraw(True)
        # *rating4* updates
        if t >= 0.0 and rating4.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating4.tStart = t  # underestimates by a little under one frame
            rating4.frameNStart = frameN  # exact frame index
            rating4.setAutoDraw(True)
        # *rating5* updates
        if t >= 0.0 and rating5.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating5.tStart = t  # underestimates by a little under one frame
            rating5.frameNStart = frameN  # exact frame index
            rating5.setAutoDraw(True)
        # *rating6* updates
        if t >= 0.0 and rating6.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating6.tStart = t  # underestimates by a little under one frame
            rating6.frameNStart = frameN  # exact frame index
            rating6.setAutoDraw(True)
        # *rating7* updates
        if t >= 0.0 and rating7.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating7.tStart = t  # underestimates by a little under one frame
            rating7.frameNStart = frameN  # exact frame index
            rating7.setAutoDraw(True)
        # *rating8* updates
        if t >= 0.0 and rating8.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating8.tStart = t  # underestimates by a little under one frame
            rating8.frameNStart = frameN  # exact frame index
            rating8.setAutoDraw(True)
        # *rating9* updates
        if t >= 0.0 and rating9.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating9.tStart = t  # underestimates by a little under one frame
            rating9.frameNStart = frameN  # exact frame index
            rating9.setAutoDraw(True)
        # *rating10* updates
        if t >= 0.0 and rating10.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating10.tStart = t  # underestimates by a little under one frame
            rating10.frameNStart = frameN  # exact frame index
            rating10.setAutoDraw(True)
        # *rating11* updates
        if t >= 0.0 and rating11.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating11.tStart = t  # underestimates by a little under one frame
            rating11.frameNStart = frameN  # exact frame index
            rating11.setAutoDraw(True)
        # *rating12* updates
        if t >= 0.0 and rating12.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating12.tStart = t  # underestimates by a little under one frame
            rating12.frameNStart = frameN  # exact frame index
            rating12.setAutoDraw(True)
        # *rating13* updates
        if t >= 0.0 and rating13.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating13.tStart = t  # underestimates by a little under one frame
            rating13.frameNStart = frameN  # exact frame index
            rating13.setAutoDraw(True)
        # *rating14* updates
        if t >= 0.0 and rating14.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating14.tStart = t  # underestimates by a little under one frame
            rating14.frameNStart = frameN  # exact frame index
            rating14.setAutoDraw(True)
        # *rating15* updates
        if t >= 0.0 and rating15.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating15.tStart = t  # underestimates by a little under one frame
            rating15.frameNStart = frameN  # exact frame index
            rating15.setAutoDraw(True)
        # *rating16* updates
        if t >= 0.0 and rating16.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating16.tStart = t  # underestimates by a little under one frame
            rating16.frameNStart = frameN  # exact frame index
            rating16.setAutoDraw(True)
        # *rating17* updates
        if t >= 0.0 and rating17.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating17.tStart = t  # underestimates by a little under one frame
            rating17.frameNStart = frameN  # exact frame index
            rating17.setAutoDraw(True)
        # *rating18* updates
        if t >= 0.0 and rating18.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating18.tStart = t  # underestimates by a little under one frame
            rating18.frameNStart = frameN  # exact frame index
            rating18.setAutoDraw(True)
        # *rating19* updates
        if t >= 0.0 and rating19.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating19.tStart = t  # underestimates by a little under one frame
            rating19.frameNStart = frameN  # exact frame index
            rating19.setAutoDraw(True)
        # *rating20* updates
        if t >= 0.0 and rating20.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating20.tStart = t  # underestimates by a little under one frame
            rating20.frameNStart = frameN  # exact frame index
            rating20.setAutoDraw(True)
        # *rating21* updates
        if t >= 0.0 and rating21.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating21.tStart = t  # underestimates by a little under one frame
            rating21.frameNStart = frameN  # exact frame index
            rating21.setAutoDraw(True)
        # *rating22* updates
        if t >= 0.0 and rating22.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating22.tStart = t  # underestimates by a little under one frame
            rating22.frameNStart = frameN  # exact frame index
            rating22.setAutoDraw(True)
        # *rating23* updates
        if t >= 0.0 and rating23.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating23.tStart = t  # underestimates by a little under one frame
            rating23.frameNStart = frameN  # exact frame index
            rating23.setAutoDraw(True)
        # *rating24* updates
        if t >= 0.0 and rating24.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating24.tStart = t  # underestimates by a little under one frame
            rating24.frameNStart = frameN  # exact frame index
            rating24.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in others_ffiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            
    ################################
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating1.response', rating1.getRating())
    others_ffi_trials.addData('rating1.rt', rating1.getRT())
    #others_ffi_trials.addData('rating1.history', rating1.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating2.response', rating2.getRating())
    others_ffi_trials.addData('rating2.rt', rating2.getRT())
    #others_ffi_trials.addData('rating2.history', rating2.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating3.response', rating3.getRating())
    others_ffi_trials.addData('rating3.rt', rating3.getRT())
    #others_ffi_trials.addData('rating3.history', rating3.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating4.response', rating4.getRating())
    others_ffi_trials.addData('rating4.rt', rating4.getRT())
    #others_ffi_trials.addData('rating4.history', rating4.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating5.response', rating5.getRating())
    others_ffi_trials.addData('rating5.rt', rating5.getRT())
    #others_ffi_trials.addData('rating5.history', rating5.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating6.response', rating6.getRating())
    others_ffi_trials.addData('rating6.rt', rating6.getRT())
    #others_ffi_trials.addData('rating6.history', rating6.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating7.response', rating7.getRating())
    others_ffi_trials.addData('rating7.rt', rating7.getRT())
    #others_ffi_trials.addData('rating7.history', rating7.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating8.response', rating8.getRating())
    others_ffi_trials.addData('rating8.rt', rating8.getRT())
    #others_ffi_trials.addData('rating8.history', rating8.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating9.response', rating9.getRating())
    others_ffi_trials.addData('rating9.rt', rating9.getRT())
    #others_ffi_trials.addData('rating9.history', rating9.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating10.response', rating10.getRating())
    others_ffi_trials.addData('rating10.rt', rating10.getRT())
    #others_ffi_trials.addData('rating10.history', rating10.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating11.response', rating11.getRating())
    others_ffi_trials.addData('rating11.rt', rating11.getRT())
    #others_ffi_trials.addData('rating11.history', rating11.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating12.response', rating12.getRating())
    others_ffi_trials.addData('rating12.rt', rating12.getRT())
    #others_ffi_trials.addData('rating12.history', rating12.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating13.response', rating13.getRating())
    others_ffi_trials.addData('rating13.rt', rating13.getRT())
    #others_ffi_trials.addData('rating13.history', rating13.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating14.response', rating14.getRating())
    others_ffi_trials.addData('rating14.rt', rating14.getRT())
    #others_ffi_trials.addData('rating14.history', rating14.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating15.response', rating15.getRating())
    others_ffi_trials.addData('rating15.rt', rating15.getRT())
    #others_ffi_trials.addData('rating15.history', rating15.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating16.response', rating16.getRating())
    others_ffi_trials.addData('rating16.rt', rating16.getRT())
    #others_ffi_trials.addData('rating16.history', rating16.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating17.response', rating17.getRating())
    others_ffi_trials.addData('rating17.rt', rating17.getRT())
    #others_ffi_trials.addData('rating17.history', rating17.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating18.response', rating18.getRating())
    others_ffi_trials.addData('rating18.rt', rating18.getRT())
    #others_ffi_trials.addData('rating18.history', rating18.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating19.response', rating19.getRating())
    others_ffi_trials.addData('rating19.rt', rating19.getRT())
    #others_ffi_trials.addData('rating19.history', rating19.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating20.response', rating20.getRating())
    others_ffi_trials.addData('rating20.rt', rating20.getRT())
    #others_ffi_trials.addData('rating20.history', rating20.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating21.response', rating21.getRating())
    others_ffi_trials.addData('rating21.rt', rating21.getRT())
    #others_ffi_trials.addData('rating21.history', rating21.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating22.response', rating22.getRating())
    others_ffi_trials.addData('rating22.rt', rating22.getRT())
    #others_ffi_trials.addData('rating22.history', rating22.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating23.response', rating23.getRating())
    others_ffi_trials.addData('rating23.rt', rating23.getRT())
    #others_ffi_trials.addData('rating23.history', rating23.getHistory())
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('rating24.response', rating24.getRating())
    others_ffi_trials.addData('rating24.rt', rating24.getRT())
    #others_ffi_trials.addData('rating24.history', rating24.getHistory())
  ###########################################################################################################
  
    #-------Ending Routine "others_ffi"-------
    for thisComponent in others_ffiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if endtrial_resp.keys in ['', [], None]:  # No response was made
       endtrial_resp.keys=None
    # store data for others_ffi_trials (TrialHandler)
    others_ffi_trials.addData('endtrial_resp.keys',endtrial_resp.keys)
    if endtrial_resp.keys != None:  # we had a response
        others_ffi_trials.addData('endtrial_resp.rt', endtrial_resp.rt)

    others_ffi_trials.addData('rating1.history', rating1.getHistory())				
    others_ffi_trials.addData('rating2.history', rating2.getHistory())				
    others_ffi_trials.addData('rating3.history', rating3.getHistory())				
    others_ffi_trials.addData('rating4.history', rating4.getHistory())				
    others_ffi_trials.addData('rating5.history', rating5.getHistory())				
    others_ffi_trials.addData('rating6.history', rating6.getHistory())				
    others_ffi_trials.addData('rating7.history', rating7.getHistory())				
    others_ffi_trials.addData('rating8.history', rating8.getHistory())				
    others_ffi_trials.addData('rating9.history', rating9.getHistory())				
    others_ffi_trials.addData('rating10.history', rating10.getHistory())				
    others_ffi_trials.addData('rating11.history', rating11.getHistory())				
    others_ffi_trials.addData('rating12.history', rating12.getHistory())				
    others_ffi_trials.addData('rating13.history', rating13.getHistory())				
    others_ffi_trials.addData('rating14.history', rating14.getHistory())				
    others_ffi_trials.addData('rating15.history', rating15.getHistory())				
    others_ffi_trials.addData('rating16.history', rating16.getHistory())				
    others_ffi_trials.addData('rating17.history', rating17.getHistory())				
    others_ffi_trials.addData('rating18.history', rating18.getHistory())				
    others_ffi_trials.addData('rating19.history', rating19.getHistory())				
    others_ffi_trials.addData('rating20.history', rating20.getHistory())				
    others_ffi_trials.addData('rating21.history', rating21.getHistory())				
    others_ffi_trials.addData('rating22.history', rating22.getHistory())				
    others_ffi_trials.addData('rating23.history', rating23.getHistory())				
    others_ffi_trials.addData('rating24.history', rating24.getHistory())
    
    # the Routine "others_ffi" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'others_ffi_trials'


# set up handler to look after randomisation of conditions etc
others_extras_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('list2_trials.xlsx'),
    seed=None, name='others_extras_trials')
thisExp.addLoop(others_extras_trials)  # add the loop to the experiment
thisOthers_extras_trial = others_extras_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisOthers_extras_trial.rgb)
if thisOthers_extras_trial != None:
    for paramName in thisOthers_extras_trial.keys():
        exec(paramName + '= thisOthers_extras_trial.' + paramName)

for thisOthers_extras_trial in others_extras_trials:
    currentLoop = others_extras_trials
    # abbreviate parameter names if possible (e.g. rgb = thisOthers_extras_trial.rgb)
    if thisOthers_extras_trial != None:
        for paramName in thisOthers_extras_trial.keys():
            exec(paramName + '= thisOthers_extras_trial.' + paramName)
    
    #------Prepare to start Routine "others_extras"-------
    t = 0
    others_extrasClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    question_text_other.setText(question)
    endtrial_resp_other = event.BuilderKeyResponse()  # create an object of type KeyResponse
    endtrial_resp_other.status = NOT_STARTED
    rating1_other.reset()
    rating2_other.reset()
    rating3_other.reset()
    rating4_other.reset()
    rating5_other.reset()
    rating6_other.reset()
    rating7_other.reset()
    rating8_other.reset()
    rating9_other.reset()
    rating10_other.reset()
    rating11_other.reset()
    rating12_other.reset()
    rating13_other.reset()
    rating14_other.reset()
    rating15_other.reset()
    rating16_other.reset()
    rating17_other.reset()
    rating18_other.reset()
    rating19_other.reset()
    rating20_other.reset()
    rating21_other.reset()
    rating22_other.reset()
    rating23_other.reset()
    rating24_other.reset()
    
    rating1_other.setDescription(tar1)
    rating2_other.setDescription(tar2)
    rating3_other.setDescription(tar3)
    rating4_other.setDescription(tar4)
    rating5_other.setDescription(tar5)
    rating6_other.setDescription(tar6)
    rating7_other.setDescription(tar7)
    rating8_other.setDescription(tar8)
    rating9_other.setDescription(tar9)
    rating10_other.setDescription(tar10)
    rating11_other.setDescription(tar11)
    rating12_other.setDescription(tar12)
    rating13_other.setDescription(tar13)
    rating14_other.setDescription(tar14)
    rating15_other.setDescription(tar15)
    rating16_other.setDescription(tar16)
    rating17_other.setDescription(tar17)
    rating18_other.setDescription(tar18)
    rating19_other.setDescription(tar19)
    rating20_other.setDescription(tar20)
    rating21_other.setDescription(tar21)
    rating22_other.setDescription(tar22)
    rating23_other.setDescription(tar23)
    rating24_other.setDescription(tar24)    
    
    # keep track of which components have finished
    others_extrasComponents = []
    others_extrasComponents.append(question_text_other)
    others_extrasComponents.append(endtext_other)
    others_extrasComponents.append(endtrial_resp_other)
    others_extrasComponents.append(rating1_other)
    others_extrasComponents.append(rating2_other)
    others_extrasComponents.append(rating3_other)
    others_extrasComponents.append(rating4_other)
    others_extrasComponents.append(rating5_other)
    others_extrasComponents.append(rating6_other)
    others_extrasComponents.append(rating7_other)
    others_extrasComponents.append(rating8_other)
    others_extrasComponents.append(rating9_other)
    others_extrasComponents.append(rating10_other)
    others_extrasComponents.append(rating11_other)
    others_extrasComponents.append(rating12_other)
    others_extrasComponents.append(rating13_other)
    others_extrasComponents.append(rating14_other)
    others_extrasComponents.append(rating15_other)
    others_extrasComponents.append(rating16_other)
    others_extrasComponents.append(rating17_other)
    others_extrasComponents.append(rating18_other)
    others_extrasComponents.append(rating19_other)
    others_extrasComponents.append(rating20_other)
    others_extrasComponents.append(rating21_other)
    others_extrasComponents.append(rating22_other)
    others_extrasComponents.append(rating23_other)
    others_extrasComponents.append(rating24_other)
    for thisComponent in others_extrasComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "others_extras"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = others_extrasClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *question_text_other* updates
        if t >= 0.0 and question_text_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            question_text_other.tStart = t  # underestimates by a little under one frame
            question_text_other.frameNStart = frameN  # exact frame index
            question_text_other.setAutoDraw(True)
        
        # *endtext_other* updates
        if (rating1_other.getRating() > 0 and rating2_other.getRating() > 0 and rating3_other.getRating() > 0  and rating4_other.getRating() > 0  and rating5_other.getRating() > 0  and rating6_other.getRating() > 0   and rating7_other.getRating() > 0  and rating8_other.getRating() > 0  and rating9_other.getRating() > 0  and rating10_other.getRating() > 0  and rating11_other.getRating() > 0  and rating12_other.getRating() > 0  and rating13_other.getRating() > 0  and rating14_other.getRating() > 0  and rating15_other.getRating() > 0  and rating16_other.getRating() > 0  and rating17_other.getRating() > 0  and rating18_other.getRating() > 0  and rating19_other.getRating() > 0 and rating20_other.getRating() > 0 and rating21_other.getRating() > 0  and rating22_other.getRating() > 0  and rating23_other.getRating() > 0  and rating24_other.getRating() > 0   ) and endtext_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            endtext_other.tStart = t  # underestimates by a little under one frame
            endtext_other.frameNStart = frameN  # exact frame index
            endtext_other.setAutoDraw(True)
        
        # *endtrial_resp_other* updates
        if (rating1_other.getRating() > 0 and rating2_other.getRating() > 0 and rating3_other.getRating() > 0  and rating4_other.getRating() > 0  and rating5_other.getRating() > 0  and rating6_other.getRating() > 0   and rating7_other.getRating() > 0  and rating8_other.getRating() > 0  and rating9_other.getRating() > 0  and rating10_other.getRating() > 0  and rating11_other.getRating() > 0  and rating12_other.getRating() > 0  and rating13_other.getRating() > 0  and rating14_other.getRating() > 0  and rating15_other.getRating() > 0  and rating16_other.getRating() > 0  and rating17_other.getRating() > 0  and rating18_other.getRating() > 0  and rating19_other.getRating() > 0 and rating20_other.getRating() > 0 and rating21_other.getRating() > 0  and rating22_other.getRating() > 0  and rating23_other.getRating() > 0  and rating24_other.getRating() > 0   ) and endtrial_resp_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            endtrial_resp_other.tStart = t  # underestimates by a little under one frame
            endtrial_resp_other.frameNStart = frameN  # exact frame index
            endtrial_resp_other.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(endtrial_resp_other.clock.reset)  # t=0 on next screen flip
        if endtrial_resp_other.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                endtrial_resp_other.keys = theseKeys[-1]  # just the last key pressed
                endtrial_resp_other.rt = endtrial_resp_other.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        # *rating1_other* updates
        if t >= 0.0 and rating1_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating1_other.tStart = t  # underestimates by a little under one frame
            rating1_other.frameNStart = frameN  # exact frame index
            rating1_other.setAutoDraw(True)
        # *rating2_other* updates
        if t >= 0.0 and rating2_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating2_other.tStart = t  # underestimates by a little under one frame
            rating2_other.frameNStart = frameN  # exact frame index
            rating2_other.setAutoDraw(True)
        # *rating3_other* updates
        if t >= 0.0 and rating3_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating3_other.tStart = t  # underestimates by a little under one frame
            rating3_other.frameNStart = frameN  # exact frame index
            rating3_other.setAutoDraw(True)
        # *rating4_other* updates
        if t >= 0.0 and rating4_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating4_other.tStart = t  # underestimates by a little under one frame
            rating4_other.frameNStart = frameN  # exact frame index
            rating4_other.setAutoDraw(True)
        # *rating5_other* updates
        if t >= 0.0 and rating5_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating5_other.tStart = t  # underestimates by a little under one frame
            rating5_other.frameNStart = frameN  # exact frame index
            rating5_other.setAutoDraw(True)
        # *rating6_other* updates
        if t >= 0.0 and rating6_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating6_other.tStart = t  # underestimates by a little under one frame
            rating6_other.frameNStart = frameN  # exact frame index
            rating6_other.setAutoDraw(True)
        # *rating7_other* updates
        if t >= 0.0 and rating7_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating7_other.tStart = t  # underestimates by a little under one frame
            rating7_other.frameNStart = frameN  # exact frame index
            rating7_other.setAutoDraw(True)
        # *rating8_other* updates
        if t >= 0.0 and rating8_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating8_other.tStart = t  # underestimates by a little under one frame
            rating8_other.frameNStart = frameN  # exact frame index
            rating8_other.setAutoDraw(True)
        # *rating9_other* updates
        if t >= 0.0 and rating9_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating9_other.tStart = t  # underestimates by a little under one frame
            rating9_other.frameNStart = frameN  # exact frame index
            rating9_other.setAutoDraw(True)
        # *rating10_other* updates
        if t >= 0.0 and rating10_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating10_other.tStart = t  # underestimates by a little under one frame
            rating10_other.frameNStart = frameN  # exact frame index
            rating10_other.setAutoDraw(True)
        # *rating11_other* updates
        if t >= 0.0 and rating11_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating11_other.tStart = t  # underestimates by a little under one frame
            rating11_other.frameNStart = frameN  # exact frame index
            rating11_other.setAutoDraw(True)
        # *rating12_other* updates
        if t >= 0.0 and rating12_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating12_other.tStart = t  # underestimates by a little under one frame
            rating12_other.frameNStart = frameN  # exact frame index
            rating12_other.setAutoDraw(True)
        # *rating13_other* updates
        if t >= 0.0 and rating13_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating13_other.tStart = t  # underestimates by a little under one frame
            rating13_other.frameNStart = frameN  # exact frame index
            rating13_other.setAutoDraw(True)
        # *rating14_other* updates
        if t >= 0.0 and rating14_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating14_other.tStart = t  # underestimates by a little under one frame
            rating14_other.frameNStart = frameN  # exact frame index
            rating14_other.setAutoDraw(True)
        # *rating15_other* updates
        if t >= 0.0 and rating15_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating15_other.tStart = t  # underestimates by a little under one frame
            rating15_other.frameNStart = frameN  # exact frame index
            rating15_other.setAutoDraw(True)
        # *rating16_other* updates
        if t >= 0.0 and rating16_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating16_other.tStart = t  # underestimates by a little under one frame
            rating16_other.frameNStart = frameN  # exact frame index
            rating16_other.setAutoDraw(True)
        # *rating17_other* updates
        if t >= 0.0 and rating17_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating17_other.tStart = t  # underestimates by a little under one frame
            rating17_other.frameNStart = frameN  # exact frame index
            rating17_other.setAutoDraw(True)
        # *rating18_other* updates
        if t >= 0.0 and rating18_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating18_other.tStart = t  # underestimates by a little under one frame
            rating18_other.frameNStart = frameN  # exact frame index
            rating18_other.setAutoDraw(True)
        # *rating19_other* updates
        if t >= 0.0 and rating19_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating19_other.tStart = t  # underestimates by a little under one frame
            rating19_other.frameNStart = frameN  # exact frame index
            rating19_other.setAutoDraw(True)
        # *rating20_other* updates
        if t >= 0.0 and rating20_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating20_other.tStart = t  # underestimates by a little under one frame
            rating20_other.frameNStart = frameN  # exact frame index
            rating20_other.setAutoDraw(True)
        # *rating21_other* updates
        if t >= 0.0 and rating21_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating21_other.tStart = t  # underestimates by a little under one frame
            rating21_other.frameNStart = frameN  # exact frame index
            rating21_other.setAutoDraw(True)
        # *rating22_other* updates
        if t >= 0.0 and rating22_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating22_other.tStart = t  # underestimates by a little under one frame
            rating22_other.frameNStart = frameN  # exact frame index
            rating22_other.setAutoDraw(True)
        # *rating23_other* updates
        if t >= 0.0 and rating23_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating23_other.tStart = t  # underestimates by a little under one frame
            rating23_other.frameNStart = frameN  # exact frame index
            rating23_other.setAutoDraw(True)
        # *rating24_other* updates
        if t >= 0.0 and rating24_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating24_other.tStart = t  # underestimates by a little under one frame
            rating24_other.frameNStart = frameN  # exact frame index
            rating24_other.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in others_extrasComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    ################################
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating1_other.response', rating1_other.getRating())
    others_extras_trials.addData('rating1_other.rt', rating1_other.getRT())
    #others_extras_trials.addData('rating1_other.history', rating1_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating2_other.response', rating2_other.getRating())
    others_extras_trials.addData('rating2_other.rt', rating2_other.getRT())
    #others_extras_trials.addData('rating2_other.history', rating2_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating3_other.response', rating3_other.getRating())
    others_extras_trials.addData('rating3_other.rt', rating3_other.getRT())
    #others_extras_trials.addData('rating3_other.history', rating3_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating4_other.response', rating4_other.getRating())
    others_extras_trials.addData('rating4_other.rt', rating4_other.getRT())
    #others_extras_trials.addData('rating4_other.history', rating4_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating5_other.response', rating5_other.getRating())
    others_extras_trials.addData('rating5_other.rt', rating5_other.getRT())
    #others_extras_trials.addData('rating5_other.history', rating5_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating6_other.response', rating6_other.getRating())
    others_extras_trials.addData('rating6_other.rt', rating6_other.getRT())
    #others_extras_trials.addData('rating6_other.history', rating6_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating7_other.response', rating7_other.getRating())
    others_extras_trials.addData('rating7_other.rt', rating7_other.getRT())
    #others_extras_trials.addData('rating7_other.history', rating7_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating8_other.response', rating8_other.getRating())
    others_extras_trials.addData('rating8_other.rt', rating8_other.getRT())
    #others_extras_trials.addData('rating8_other.history', rating8_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating9_other.response', rating9_other.getRating())
    others_extras_trials.addData('rating9_other.rt', rating9_other.getRT())
    #others_extras_trials.addData('rating9_other.history', rating9_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating10_other.response', rating10_other.getRating())
    others_extras_trials.addData('rating10_other.rt', rating10_other.getRT())
    #others_extras_trials.addData('rating10_other.history', rating10_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating11_other.response', rating11_other.getRating())
    others_extras_trials.addData('rating11_other.rt', rating11_other.getRT())
    #others_extras_trials.addData('rating11_other.history', rating11_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating12_other.response', rating12_other.getRating())
    others_extras_trials.addData('rating12_other.rt', rating12_other.getRT())
    #others_extras_trials.addData('rating12_other.history', rating12_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating13_other.response', rating13_other.getRating())
    others_extras_trials.addData('rating13_other.rt', rating13_other.getRT())
    #others_extras_trials.addData('rating13_other.history', rating13_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating14_other.response', rating14_other.getRating())
    others_extras_trials.addData('rating14_other.rt', rating14_other.getRT())
    #others_extras_trials.addData('rating14_other.history', rating14_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating15_other.response', rating15_other.getRating())
    others_extras_trials.addData('rating15_other.rt', rating15_other.getRT())
    #others_extras_trials.addData('rating15_other.history', rating15_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating16_other.response', rating16_other.getRating())
    others_extras_trials.addData('rating16_other.rt', rating16_other.getRT())
    #others_extras_trials.addData('rating16_other.history', rating16_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating17_other.response', rating17_other.getRating())
    others_extras_trials.addData('rating17_other.rt', rating17_other.getRT())
    #others_extras_trials.addData('rating17_other.history', rating17_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating18_other.response', rating18_other.getRating())
    others_extras_trials.addData('rating18_other.rt', rating18_other.getRT())
    #others_extras_trials.addData('rating18_other.history', rating18_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating19_other.response', rating19_other.getRating())
    others_extras_trials.addData('rating19_other.rt', rating19_other.getRT())
    #others_extras_trials.addData('rating19_other.history', rating19_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating20_other.response', rating20_other.getRating())
    others_extras_trials.addData('rating20_other.rt', rating20_other.getRT())
    #others_extras_trials.addData('rating20_other.history', rating20_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating21_other.response', rating21_other.getRating())
    others_extras_trials.addData('rating21_other.rt', rating21_other.getRT())
    #others_extras_trials.addData('rating21_other.history', rating21_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating22_other.response', rating22_other.getRating())
    others_extras_trials.addData('rating22_other.rt', rating22_other.getRT())
    #others_extras_trials.addData('rating22_other.history', rating22_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating23_other.response', rating23_other.getRating())
    others_extras_trials.addData('rating23_other.rt', rating23_other.getRT())
    #others_extras_trials.addData('rating23_other.history', rating23_other.getHistory())
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('rating24_other.response', rating24_other.getRating())
    others_extras_trials.addData('rating24_other.rt', rating24_other.getRT())
    #others_extras_trials.addData('rating24_other.history', rating24_other.getHistory())
    ###########################################################################################################
    
    
    #-------Ending Routine "others_extras"-------
    for thisComponent in others_extrasComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if endtrial_resp_other.keys in ['', [], None]:  # No response was made
       endtrial_resp_other.keys=None
    # store data for others_extras_trials (TrialHandler)
    others_extras_trials.addData('endtrial_resp_other.keys',endtrial_resp_other.keys)
    if endtrial_resp_other.keys != None:  # we had a response
        others_extras_trials.addData('endtrial_resp_other.rt', endtrial_resp_other.rt)
    others_extras_trials.addData('rating1_other.history', rating1_other.getHistory())
    others_extras_trials.addData('rating2_other.history', rating2_other.getHistory())
    others_extras_trials.addData('rating3_other.history', rating3_other.getHistory())
    others_extras_trials.addData('rating4_other.history', rating4_other.getHistory())
    others_extras_trials.addData('rating5_other.history', rating5_other.getHistory())
    others_extras_trials.addData('rating6_other.history', rating6_other.getHistory())
    others_extras_trials.addData('rating7_other.history', rating7_other.getHistory())
    others_extras_trials.addData('rating8_other.history', rating8_other.getHistory())
    others_extras_trials.addData('rating9_other.history', rating9_other.getHistory())
    others_extras_trials.addData('rating10_other.history', rating10_other.getHistory())
    others_extras_trials.addData('rating11_other.history', rating11_other.getHistory())
    others_extras_trials.addData('rating12_other.history', rating12_other.getHistory())
    others_extras_trials.addData('rating13_other.history', rating13_other.getHistory())
    others_extras_trials.addData('rating14_other.history', rating14_other.getHistory())
    others_extras_trials.addData('rating15_other.history', rating15_other.getHistory())
    others_extras_trials.addData('rating16_other.history', rating16_other.getHistory())
    others_extras_trials.addData('rating17_other.history', rating17_other.getHistory())
    others_extras_trials.addData('rating18_other.history', rating18_other.getHistory())
    others_extras_trials.addData('rating19_other.history', rating19_other.getHistory())
    others_extras_trials.addData('rating20_other.history', rating20_other.getHistory())
    others_extras_trials.addData('rating21_other.history', rating21_other.getHistory())
    others_extras_trials.addData('rating22_other.history', rating22_other.getHistory())
    others_extras_trials.addData('rating23_other.history', rating23_other.getHistory())
    others_extras_trials.addData('rating24_other.history', rating24_other.getHistory())
    
    # the Routine "others_extras" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'others_extras_trials'

win.close()
core.quit()
