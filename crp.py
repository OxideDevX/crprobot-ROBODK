# -*- coding: UTF-8 -*-
# Copyright 2015-2022 - RoboDK Inc. - https://robodk.com/ and OxideDevX
#
# This file loads the compiled version of the RoboDK post processor for:
#   CRP robot controllers
# 
# More information about RoboDK Post Processors and Offline Programming:
#     https://robodk.com/help#PostProcessor
#     https://robodk.com/doc/en/PythonAPI/postprocessor.html
# ----------------------------------------------------

import sys
import os

#Needed to make the robodk generated code work
import math
from robodk import *

# Detect Python version and post processor
print("Using Python version: " + str(sys.version_info))
path_app = os.path.dirname(__file__).replace(os.sep,"/")
print("RoboDK Post Processor: " + path_app)

# Check if the post is compatible with the Python version
version_str = str(sys.version_info[0]) + str(sys.version_info[1])
path_library = path_app + '/v' + version_str
if not os.path.isdir(path_library):
    msg = "Invalid Python version or post processor not found. Make sure you are using a supported Python version: " + path_library
    msg += "\nSelect Tools-Options-Python and select a supported Python version"
    print(msg)
    raise Exception(msg)

# Load the post processor
exec("from v" + version_str + ".CRP import RobotPost as BasePost")

class RobotPost(BasePost):
    """Robot post object"""
    PROG_EXT = "PRL"    # set the program extension

    MAX_LINES_X_PROG = 999    # maximum number of lines per program. It will then generate multiple "pages (files)"

    PULSES_X_DEG = [1, 1, 1, 1, 1, 1]    

    INCLUDE_SUB_PROGRAMS = False    

    pass

if __name__== "__main__":
    exec("from v" + version_str + ".CRP import test_post")
    test_post()
