AutoRecorder for Robot Framework
==================================================

_____________________________________________________________________________________________________________________________________


**!!! This repository is not actively maintained, but I am open to help and fixing issues, just let me know by submitting issue !!!**


_____________________________________________________________________________________________________________________________________

[![AutoRecorder](https://github.com/SanthoshS20/robotframework-autorecorder/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/SanthoshS20/robotframework-autorecorder/actions/workflows/python-app.yml)

Introduction
------------

RobotFramework library allowing to automatically start video recording of desktop when test or (and) suite starts. Based on [ScreenCapLibrary](https://github.com/mihaiparvu/ScreenCapLibrary)

- Information about keywords can be found on the [Keyword Documentation](https://raw.githack.com/sebastianciupinski/robotframework-autorecorder/master/docs/AutoRecorder.html) page.


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

    *** Settings ***
    Documentation     This example demonstrates how to use current library
    Library      AutoRecorder
    Library      SeleniumLibrary

    *** Test Cases ***
    Example Test
        Open Browser    http://example.local    gc
        Sleep    5s
        
        
SuiteRecorder.robot

    *** Settings ***
    Documentation     This example demonstrates how to use current library
    Library      AutoRecorder      mode=suite
    Library      SeleniumLibrary
    
    *** Test Cases ***
    Example Test
        Open Browser    http://example.local    gc
        Sleep    5s


SuiteAndTestRecorder.robot

    *** Settings ***
    Documentation     This example demonstrates how to use current library
    Library      AutoRecorder      mode=suite,test
    Library      SeleniumLibrary
    
    *** Test Cases ***
    Example Test
        Open Browser    http://example.local    gc
        Sleep    5s



