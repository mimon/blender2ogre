# Copyright (C) 2010 Brett Hartshorn
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import os, sys, logging

bl_info = {
    "name": "OGRE Exporter (.scene, .mesh, .skeleton) and RealXtend (.txml)",
    "author": "Brett, S.Rombauts, F00bar, Waruck, Mind Calamity, Mr.Magne, Jonne Nauha, vax456, Richard Plangger, Pavel Rojtberg",
    "version": (0, 8, 0),
    "blender": (2, 80, 0),
    "location": "File > Export...",
    "description": "Export to Ogre xml and binary formats",
    "wiki_url": "https://github.com/OGRECave/blender2ogre",
    "tracker_url": "https://github.com/OGRECave/blender2ogre/issues",
    "category": "Import-Export"
}

from pprint import pprint

# import the plugin directory and setup the plugin
import bpy

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

from . import config

import sys


def register():
    pass

def unregister():
    logging.info('Unloading io_ogre %s', bl_info["version"])
    for clazz in ui.auto_register(False):
        bpy.utils.unregister_class(clazz)

    bpy.utils.unregister_class(Blender2OgreAddonPreferences)

if __name__ == "__main__":
    register()
