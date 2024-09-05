
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='robotframework-autorecorder',  
     version='0.1.6',
     author="Sebastian Ciupinski",
     author_email="sebastian.ciupinski+robotframework-autorecorder@gmail.com",
     description="Robot Framework AutoRecorder Library",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/sebastianciupinski/robotframework-autorecorder",
     packages=setuptools.find_packages(),
	 install_requires=[
          'robotframework-screencaplibrary'
      ],
     classifiers=[
         "Programming Language :: Python",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
