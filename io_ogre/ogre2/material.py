from datetime import datetime
import os
from os.path import join, split, splitext
from ..util import *
from .. import util
from .. import config
from .. import shader
from ..report import Report
import tempfile
import shutil
import logging
from itertools import chain

from bpy.props import EnumProperty
from .program import OgreProgram

def json_material(obj):
    pass