# -*- coding: utf-8 -*-


import os

from fabric.api import *
from cabric.api import *


##############################################
# demo
######################################################
@task
def hello_world():
    run("echo 'hello world'")
    pass


