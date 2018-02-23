#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), May 24, 2016, at 15:33
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
expName = 'runA'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Documents and Settings\\fmri\\Desktop\\PsychNet\\random_order\\ANDY\\runA.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "wait_for_trig"
wait_for_trigClock = core.Clock()
wait_crosshair = visual.TextStim(win=win, ori=0, name='wait_crosshair',
    text='+',    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color=[0.004,0.004,0.004], colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
name = visual.TextStim(win=win, ori=0, name='name',
    text='default text',    font='Arial',
    pos=[0, .2], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
trait = visual.TextStim(win=win, ori=0, name='trait',
    text='default text',    font='Arial',
    pos=[0, -.2], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
stim_crosshair = visual.TextStim(win=win, ori=0, name='stim_crosshair',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
poststim_fix = visual.TextStim(win=win, ori=0, name='poststim_fix',
    text='+',    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "wait_for_trig"-------
t = 0
wait_for_trigClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
start_trigger = event.BuilderKeyResponse()  # create an object of type KeyResponse
start_trigger.status = NOT_STARTED
# keep track of which components have finished
wait_for_trigComponents = []
wait_for_trigComponents.append(wait_crosshair)
wait_for_trigComponents.append(start_trigger)
for thisComponent in wait_for_trigComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "wait_for_trig"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = wait_for_trigClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_crosshair* updates
    if t >= 0.0 and wait_crosshair.status == NOT_STARTED:
        # keep track of start time/frame for later
        wait_crosshair.tStart = t  # underestimates by a little under one frame
        wait_crosshair.frameNStart = frameN  # exact frame index
        wait_crosshair.setAutoDraw(True)
    
    # *start_trigger* updates
    if t >= 0.0 and start_trigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        start_trigger.tStart = t  # underestimates by a little under one frame
        start_trigger.frameNStart = frameN  # exact frame index
        start_trigger.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(start_trigger.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if start_trigger.status == STARTED:
        theseKeys = event.getKeys(keyList=['5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            start_trigger.keys = theseKeys[-1]  # just the last key pressed
            start_trigger.rt = start_trigger.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_for_trigComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "wait_for_trig"-------
for thisComponent in wait_for_trigComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start_trigger.keys in ['', [], None]:  # No response was made
   start_trigger.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('start_trigger.keys',start_trigger.keys)
if start_trigger.keys != None:  # we had a response
    thisExp.addData('start_trigger.rt', start_trigger.rt)
thisExp.nextEntry()
# the Routine "wait_for_trig" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('runA.csv'),
    seed=None, name='loop_trials')
thisExp.addLoop(loop_trials)  # add the loop to the experiment
thisLoop_trial = loop_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLoop_trial.rgb)
if thisLoop_trial != None:
    for paramName in thisLoop_trial.keys():
        exec(paramName + '= thisLoop_trial.' + paramName)

for thisLoop_trial in loop_trials:
    currentLoop = loop_trials
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
    if thisLoop_trial != None:
        for paramName in thisLoop_trial.keys():
            exec(paramName + '= thisLoop_trial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    name.setText(target)
    trait.setText(word)
    stim_crosshair.setText(fix_sign)
    trigger = event.BuilderKeyResponse()  # create an object of type KeyResponse
    trigger.status = NOT_STARTED
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(name)
    trialComponents.append(trait)
    trialComponents.append(stim_crosshair)
    trialComponents.append(poststim_fix)
    trialComponents.append(trigger)
    trialComponents.append(response)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *name* updates
        if t >= 0 and name.status == NOT_STARTED:
            # keep track of start time/frame for later
            name.tStart = t  # underestimates by a little under one frame
            name.frameNStart = frameN  # exact frame index
            name.setAutoDraw(True)
        if name.status == STARTED and t >= (0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            name.setAutoDraw(False)
        
        # *trait* updates
        if t >= 0 and trait.status == NOT_STARTED:
            # keep track of start time/frame for later
            trait.tStart = t  # underestimates by a little under one frame
            trait.frameNStart = frameN  # exact frame index
            trait.setAutoDraw(True)
        if trait.status == STARTED and t >= (0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            trait.setAutoDraw(False)
        
        # *stim_crosshair* updates
        if t >= 0 and stim_crosshair.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_crosshair.tStart = t  # underestimates by a little under one frame
            stim_crosshair.frameNStart = frameN  # exact frame index
            stim_crosshair.setAutoDraw(True)
        if stim_crosshair.status == STARTED and t >= (0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            stim_crosshair.setAutoDraw(False)
        
        # *poststim_fix* updates
        if t >= 2 and poststim_fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            poststim_fix.tStart = t  # underestimates by a little under one frame
            poststim_fix.frameNStart = frameN  # exact frame index
            poststim_fix.setAutoDraw(True)
        
        # *trigger* updates
        if t >= 0 and trigger.status == NOT_STARTED:
            # keep track of start time/frame for later
            trigger.tStart = t  # underestimates by a little under one frame
            trigger.frameNStart = frameN  # exact frame index
            trigger.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(trigger.clock.reset)  # t=0 on next screen flip
        if trigger.status == STARTED:
            theseKeys = event.getKeys(keyList=['5', '6'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if trigger.keys == []:  # then this was the first keypress
                    trigger.keys = theseKeys[0]  # just the first key pressed
                    trigger.rt = trigger.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *response* updates
        if t >= 0.0 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys = theseKeys[-1]  # just the last key pressed
                response.rt = response.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if trigger.keys in ['', [], None]:  # No response was made
       trigger.keys=None
    # store data for loop_trials (TrialHandler)
    loop_trials.addData('trigger.keys',trigger.keys)
    if trigger.keys != None:  # we had a response
        loop_trials.addData('trigger.rt', trigger.rt)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
       response.keys=None
    # store data for loop_trials (TrialHandler)
    loop_trials.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        loop_trials.addData('response.rt', response.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_trials'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
