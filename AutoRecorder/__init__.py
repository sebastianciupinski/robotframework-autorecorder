#!/usr/bin/env python

from robot.running import context
from .listener import AutoRecorderListener

class AutoRecorder(AutoRecorderListener):
    '''
    AutoRecorder for Robot Framework

RobotFramework library allowing to automatically start video recording of desktop when test or (and) suite starts. Based on [ScreenCapLibrary](https://github.com/mihaiparvu/ScreenCapLibrary)

Usage
------------
To work with the library only importing it is needed. By default video for each test case is created, but it is possible to create video per whole suite or create videos for test cases and for whole suite.

SRAKA

Import arguments can be also used for tuning underlaying ScreenCapLibrary.

------------

TestRecorder.robot

    | *** Settings ***
    | Documentation     This example demonstrates how to use current library. Basic use-case
    | Library      AutoRecorder
    | Library      SeleniumLibrary
    | 
    | *** Test Cases ***
    | Example Test
    |     Open Browser    http://example.local    gc
    |     Sleep    5s
        
        
SuiteRecorder.robot

    | *** Settings ***
    | Documentation     One recording is going to be created for suite
    | Library      AutoRecorder      mode=suite
    | Library      SeleniumLibrary
    | 
    | *** Test Cases ***
    | Example Test
    |     Open Browser    http://example.local    gc
    |     Sleep    5s


SuiteAndTestRecorder.robot

    | *** Settings ***
    | Documentation     One recording will span whole suite, also recordings are going to be created per test
    | Library      AutoRecorder      mode=suite,test
    | Library      SeleniumLibrary
    | 
    | *** Test Cases ***
    | Example Test
    |     Open Browser    http://example.local    gc
    |     Sleep    5s
    |
    | Example Test 2
    |     Open Browser    http://example.local    gc
    |     Sleep    5s

Choose Tags.robot

    | *** Settings ***
    | Documentation     Only Example Test is going to be recorded, while Example Test 2 not
    | Library      AutoRecorder      mode=test    include_tags=record
    | Library      SeleniumLibrary
    | 
    | *** Test Cases ***
    | Example Test
    |     [Tags]    record
    |     Open Browser    http://example.local    gc
    |     Sleep    5s
    |
    | Example Test 2
    |     Open Browser    http://example.local    gc
    |     Sleep    5s


Exclude Tags.robot

    | *** Settings ***
    | Documentation     Example Test 2 will not be recorded
    | Library      AutoRecorder      mode=test    exclude_tags=dont
    | Library      SeleniumLibrary
    | 
    | *** Test Cases ***
    | Example Test
    |     [Tags]    record
    |     Open Browser    http://example.local    gc
    |     Sleep    5s
    |
    | Example Test 2
    |     [Tags]    dont
    |     Open Browser    http://example.local    gc
    |     Sleep    5s


Set Location.robot

    | *** Settings ***
    | Documentation     Recordings will be located in /tmp directory (built in variables like ${CURDIR}, ${TEST_NAME}, etc can be used here)
    | Library      AutoRecorder      mode=suite    screenshot_directory=/tmp
    | Library      SeleniumLibrary
    | 
    | *** Test Cases ***
    | Example Test
    |     [Tags]    record
    |     Open Browser    http://example.local    gc
    |     Sleep    5s
    |
    | Example Test 2
    |     [Tags]    dont
    |     Open Browser    http://example.local    gc
    |     Sleep    5s



    '''
    def __init__(self, mode="test", monitor=0, name="recording",
            fps=None, size_percentage=1, embed=True, embed_width="800px", screenshot_directory=None,
            included_tags=None, excluded_tags=None, display_cursor=True):

        '''
        Import Arguments:
        
        mode:
        
            test - for recording opne video per test
            
            suite -  for one video per whole suite
            
            suite,test - for both

        screenshot_directory - where to put recordings

        included_tags - choose tags to record

        excluded_tags - choose tags to not to record

        display_cursor - choose to add cursor to recording (default True)

        monitor, name, fps, size_percentage, embed, embed_with - configuration of underlaying ScreenCapLibrary - see documentation - 
        https://mihaiparvu.github.io/ScreenCapLibrary/ScreenCapLibrary.html#Start%20Video%20Recording
        '''

        if context.EXECUTION_CONTEXTS.current:
            if context.EXECUTION_CONTEXTS.current.dry_run is False:
                super().__init__(mode, name, monitor, fps, display_cursor, size_percentage, embed, embed_width, screenshot_directory, included_tags, excluded_tags)
