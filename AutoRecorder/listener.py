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

        

    def __init__(self, mode, monitor, fps, size_percentage, embed, embed_width, screenshot_directory):
        self.mode = mode
        self.monitor = monitor
        self.fps = fps
        self.size_percentage = size_percentage
        self.embed = embed
        self.embed_width = embed_width
        self.screenshot_directory = screenshot_directory
        self.ROBOT_LIBRARY_LISTENER = self

    def _start_test(self, name, attrs):
        if "test" in self.mode:
            id = BuiltIn().get_variable_value("${TEST_NAME}")
            #BuiltIn().run_keyword_and_ignore_error('ScreenCapLibrary.Start Video Recording',
            #    "alias=" + str(id), "fps=" + str(self.fps), "monitor=" + str(self.monitor),
            #    "size_percentage=" + str(self.size_percentage), "embed=" + str(self.embed),
            #    "embed_width=" + str(self.embed_width))
            self.autostart_recording(alias=id, monitor=self.monitor, fps=self.fps,
                size_percentage=self.size_percentage, embed=self.embed, embed_width=self.embed_width)


    def _end_test(self, name, attrs):
        if "test" in self.mode:
            id = BuiltIn().get_variable_value("${TEST_NAME}")
            #BuiltIn().run_keyword_and_ignore_error('ScreenCapLibrary.Stop Video Recording', "alias=" + id)
            BuiltIn().run_keyword("Stop Recording Test", id)

    def _start_suite(self, name, attrs):
        if(self.screenshot_directory):
            if not os.path.exists(self.screenshot_directory):
                os.makedirs(self.screenshot_directory)
            self.screenshot_directory=self.screenshot_directory.replace("\\", "/")
            BuiltIn().import_library("ScreenCapLibrary", "screenshot_directory=" + self.screenshot_directory)
        else:
            BuiltIn().import_library("ScreenCapLibrary")
        if "suite" in self.mode:
            id = BuiltIn().get_variable_value("${SUITE_NAME}")
            #BuiltIn().run_keyword_and_ignore_error('ScreenCapLibrary.Start Video Recording',
            #    "alias=" + str(id), "fps=" + str(self.fps), "monitor=" + str(self.monitor),
            #    "size_percentage=" + str(self.size_percentage), "embed=" + str(self.embed),
            #    "embed_width=" + str(self.embed_width))
            self.autostart_recording(alias=id, monitor=self.monitor, fps=self.fps,
                size_percentage=self.size_percentage, embed=self.embed, embed_width=self.embed_width)

    def _end_suite(self, name, attrs):
        if "suite" in self.mode:
            id = BuiltIn().get_variable_value("${SUITE_NAME}")
            #BuiltIn().run_keyword_and_ignore_error('ScreenCapLibrary.Stop Video Recording', "alias=" + id)
            #self.stop_autorecording(id)
            BuiltIn().run_keyword("Stop Recording Suite", id)
        
    def autostart_recording(self, alias=None, name="recording", fps=None, size_percentage=1, embed=True, embed_width='800px', monitor=0):
        '''
        Autostart of recording
        
        There is no need to execute this keyword manually.
        Basically - alias for https://mihaiparvu.github.io/ScreenCapLibrary/ScreenCapLibrary.html#Start%20Video%20Recording
        '''
        lib = BuiltIn().get_library_instance("ScreenCapLibrary")
        lib.start_video_recording(alias, name, fps, size_percentage, embed, embed_width, monitor)
        pass
        
    def stop_autorecording(self, alias):
        '''
        End of autorecording
        
        There is no need to execute this keyword manually.
        Basically - alias for https://mihaiparvu.github.io/ScreenCapLibrary/ScreenCapLibrary.html#Stop%20Video%20Recording
        '''
        lib = BuiltIn().get_library_instance("ScreenCapLibrary")
        lib.stop_video_recording(alias)
        
    def stop_recording_test(self, alias):
        '''
        End of autorecording
        
        There is no need to execute this keyword manually.
        Basically - alias for https://mihaiparvu.github.io/ScreenCapLibrary/ScreenCapLibrary.html#Stop%20Video%20Recording
        '''
        lib = BuiltIn().get_library_instance("ScreenCapLibrary")
        lib.stop_video_recording(alias)
        
    def stop_recording_suite(self, alias):
        '''
        End of autorecording
        
        There is no need to execute this keyword manually.
        Basically - alias for https://mihaiparvu.github.io/ScreenCapLibrary/ScreenCapLibrary.html#Stop%20Video%20Recording
        '''
        lib = BuiltIn().get_library_instance("ScreenCapLibrary")
        lib.stop_video_recording(alias)
