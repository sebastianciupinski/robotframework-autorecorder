from robot.libraries.BuiltIn import BuiltIn
from ScreenCapLibrary import ScreenCapLibrary
import os

def _start_test_implementation():
    pass

def _end_test_implementation():
    pass

def _start_suite_implementation():
    pass

def _end_suite_implementation():
    pass

class AutoRecorderListener(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LISTENER_API_VERSION = 2

        

    def __init__(self, mode, name, monitor, fps, display_cursor, size_percentage, embed, embed_width, screenshot_directory, included_tags, excluded_tags):
        self.mode = mode
        self.name = name
        self.monitor = monitor
        self.fps = fps
        self.display_cursor = display_cursor
        self.size_percentage = size_percentage
        self.embed = embed
        self.embed_width = embed_width
        self.screenshot_directory = screenshot_directory
        self.included_tags = included_tags
        self.excluded_tags = excluded_tags
        self.test_recording_in_progress = False
        self.ROBOT_LIBRARY_LISTENER = self

        if self.included_tags is not None and self.excluded_tags is not None and "test" not in self.mode:
            raise ImportError("When include_tags or exclude_tags is set to other options than None, mode needs to be set as test or test,suite")

    def _start_test(self, name, attrs):
        if ("test" in self.mode 
                and ((self.included_tags is None) or
                    any(tag in attrs["tags"] for tag in map(str.strip, self.included_tags.split(',')))
                and not (self.excluded_tags is None or
                    any(tag in attrs["tags"] for tag in map(str.strip, self.excluded_tags.split(',')))
                    ))):


            id = BuiltIn().get_variable_value("${TEST_NAME}")

            self.autostart_recording(alias=id, name=self.name, monitor=self.monitor, fps=self.fps,
                size_percentage=self.size_percentage, embed=self.embed, embed_width=self.embed_width)
            self.test_recording_in_progress=True


    def _end_test(self, name, attrs):
        if "test" in self.mode and self.test_recording_in_progress == True:

            id = BuiltIn().get_variable_value("${TEST_NAME}")
            BuiltIn().run_keyword("Stop Recording Test", id)
            self.test_recording_in_progress=False

            

    def _start_suite(self, name, attrs):
        if(self.screenshot_directory):
            if not os.path.exists(self.screenshot_directory):
                os.makedirs(self.screenshot_directory)
            self.screenshot_directory=self.screenshot_directory.replace("\\", "/")
            BuiltIn().import_library("ScreenCapLibrary", "screenshot_directory=" + self.screenshot_directory, "display_cursor=" + str(self.display_cursor))
        else:
            BuiltIn().import_library("ScreenCapLibrary", "display_cursor=" + str(self.display_cursor))

        if "suite" in self.mode:
            id = BuiltIn().get_variable_value("${SUITE_NAME}")

            self.autostart_recording(alias=id, name=self.name, monitor=self.monitor, fps=self.fps,
                size_percentage=self.size_percentage, embed=self.embed, embed_width=self.embed_width)

    def _end_suite(self, name, attrs):
        if "suite" in self.mode:
            id = BuiltIn().get_variable_value("${SUITE_NAME}")

            BuiltIn().run_keyword("Stop Recording Suite", id)
        
    def autostart_recording(self, alias=None, name=None, fps=None, size_percentage=1, embed=True, embed_width='800px', monitor=0):
        '''
        There is no need to execute this keyword manually.


        Basically - alias for https://mihaiparvu.github.io/ScreenCapLibrary/ScreenCapLibrary.html#Start%20Video%20Recording
        '''
        lib = BuiltIn().get_library_instance("ScreenCapLibrary")
        lib.start_video_recording(alias, name, fps, size_percentage, embed, embed_width, monitor)
        pass
        
    def stop_autorecording(self, alias):
        '''
        There is no need to execute this keyword manually.


        Basically - alias for https://mihaiparvu.github.io/ScreenCapLibrary/ScreenCapLibrary.html#Stop%20Video%20Recording
        '''
        lib = BuiltIn().get_library_instance("ScreenCapLibrary")
        lib.stop_video_recording(alias)
        
    def stop_recording_test(self, alias):
        '''
        There is no need to execute this keyword manually.


        Basically - alias for https://mihaiparvu.github.io/ScreenCapLibrary/ScreenCapLibrary.html#Stop%20Video%20Recording
        '''
        lib = BuiltIn().get_library_instance("ScreenCapLibrary")
        lib.stop_video_recording(alias)
        
    def stop_recording_suite(self, alias):
        '''
        There is no need to execute this keyword manually.


        Basically - alias for https://mihaiparvu.github.io/ScreenCapLibrary/ScreenCapLibrary.html#Stop%20Video%20Recording
        '''
        lib = BuiltIn().get_library_instance("ScreenCapLibrary")
        lib.stop_video_recording(alias)
