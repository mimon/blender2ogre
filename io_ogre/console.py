"""Naval Fate.

Usage:
    naval_fate.py mesh <blendfile> [options] <outfile>
    naval_fate.py scene

Options:
    -h --help               Show this screen.
    -c --collection=<name>     Filter collection.
    -o --outdir=<dir>
    -n --outname=<name>        Filename
    -x --swap-axes=<axes>      Convert from Blender's axes [default: xz-y]
"""
import bpy
import sys
import os, logging
import re
from io_ogre import util

from os.path import join, split

log = logging.getLogger(__name__)

if __name__ == "__main__":
    import io_ogre.docopt.docopt
    try:
        idx = sys.argv.index('--')
        argv = sys.argv[idx+1:]
    except ValueError:
        argv = None
    print(argv)

    cliargs = io_ogre.docopt.docopt.docopt(__doc__, argv, version='Naval Fate 2.0')


    from io_ogre import config
    from io_ogre.ogre2 import texture
    from io_ogre.ogre import mesh, skeleton

    # Update config
    config.CONFIG['SWAP_AXIS'] = cliargs['--swap-axes']

    bpy.ops.wm.open_mainfile(filepath=cliargs['<blendfile>'])

    dir = os.path.dirname(os.path.realpath(__file__))
    path = cliargs['--outdir'] if cliargs['--outdir'] else dir 
    name = cliargs['--outname'] if cliargs['--outname'] else None
    path = cliargs['<outfile>']

    print(cliargs)

    objs = [x for x in bpy.context.scene.objects if x.type == 'MESH']
    if cliargs['--collection']:
        objs = [x for x in objs if util.is_in_collection(x.users_collection, cliargs['--collection'])]

        count = len(objs)
        if count == 0:
            log.info(f"No mesh(es) found in collection '{cliargs['--collection']}'")
            exit()

        log.info(f"Found {count} mesh(es) in collection '{cliargs['--collection']}'")

    mesh.dot_mesh_xml(
        objs,
        path,
        cliargs
    )

    for obj in objs:
        skeleton.dot_skeleton(obj, path)
        texture.export_textures(obj, path)

    exit()
    objs = [x for x in bpy.context.scene.objects if x.type == 'MESH']
    if cliargs['--collection']:
        objs = [x for x in objs if is_in_collection(x.users_collection, cliargs['--collection'])]

        count = len(objs)
        if count == 0:
            print(f"No mesh(es) found in collection '{cliargs['--collection']}'")

        log.info(f"Found {count} mesh(es) in collection '{cliargs['--collection']}'")

        for ob in objs:
            if 'mesh' in cliargs:
                skeleton.dot_skeleton(
                    ob,
                    path,
                    force_name=name
                )

                for obj in objs:
                    texture.export_textures(obj, path)

    # path = sys.argv[idx+1]

    # # cut off file name
    # io_ogre = os.path.split(__file__)[0]
    # # cut off io_ogre dir
    # io_ogre = os.path.split(io_ogre)[0]
    # sys.path.append(io_ogre)

    # os.makedirs(path, exist_ok=True, mode=0o775)

    # from io_ogre import config
    # from io_ogre.ogre.scene import dot_scene
    # from io_ogre.ogre.mesh  import dot_mesh
    # from io_ogre.ogre.skeleton import dot_skeleton

    # match = re.compile("scene (.*)").match(argv[0])
    # if match:
    #     scene_name = match.group(1)
    #     dot_scene(path, scene_name=scene_name)

