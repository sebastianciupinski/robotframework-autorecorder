*** Settings ***
Documentation     This example demonstrates how to use current library
Library      ../AutoRecorder/
Library      SeleniumLibrary

*** Test Cases ***
Example Test
    Open Browser    https://www.google.com/    chrome
    Close Browser