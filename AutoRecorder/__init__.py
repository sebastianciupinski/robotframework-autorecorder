#!/usr/bin/env python

from robot.running import context
from .listener import AutoRecorderListener

class AutoRecorder(AutoRecorderListener):
    '''
    AutoRecorder for Robot Framework
RobotFramework library allowing to automatically start video recording of desktop when test or (and) suite starts. Based on [ScreenCapLibrary](https://github.com/mihaiparvu/ScreenCapLibrary)
Requirements
------------
* Robot Framework
Installation
------------
#### Using pip ####
The recommended installation tool is [pip](http://pip-installer.org).
Install pip.
Enter the following:
    pip install robotframework-autorecorder
Usage
------------
To work with library only importing it is needed. By default video for each test case is created, by it is possible to create video per whole suite or create videos for test cases and for whole suite.
Import arguments can be also used for tuning underlaying ScreenCapLibrary.
TestRecorder.robot
    | *** Settings ***
    | Documentation     This example demonstrates how to use current library
    | Library      AutoRecorder
    | Library      SeleniumLibrary
    | 
    | *** Test Cases ***
    | Example Test
    |     Open Browser    http://example.local    gc
    |     Sleep    5s
        
        
SuiteRecorder.robot
    | *** Settings ***
    | Documentation     This example demonstrates how to use current library
    | Library      AutoRecorder      mode=suite
    | Library      SeleniumLibrary
    | 
    | *** Test Cases ***
    | Example Test
    |     Open Browser    http://example.local    gc
    |     Sleep    5s
SuiteAndTestRecorder.robot
    | *** Settings ***
    | Documentation     This example demonstrates how to use current library
    | Library      AutoRecorder      mode=suite,test
    | Library      SeleniumLibrary
    | 
    | *** Test Cases ***
    | Example Test
    |     Open Browser    http://example.local    gc
    |     Sleep    5s
    '''
    def __init__(self, mode="test", monitor=0, name="recording", fps=None, size_percentage=1, embed=True, embed_width="800px", screenshot_directory=None):
        '''
        Import Arguments:
        
        mode:
        
            test - for recording opne video per test
            
            suite -  for one video per whole suite
            
            suite,test - for both
            
            
        monitor, name, fps, size_percentage, embed, embed_with, screenshot_directory - configuration of underlaying ScreenCapLibrary - see documentation - 
        https://mihaiparvu.github.io/ScreenCapLibrary/ScreenCapLibrary.html#Start%20Video%20Recording
        '''
        if context.EXECUTION_CONTEXTS.current:
            if context.EXECUTION_CONTEXTS.current.dry_run is False:
                super().__init__(mode, monitor, fps, size_percentage, embed, embed_width, screenshot_directory)
