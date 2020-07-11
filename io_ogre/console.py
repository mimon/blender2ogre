"""Naval Fate.

Usage:
    naval_fate.py mesh <blendfile> [options] <outdir>
    naval_fate.py skeleton <blendfile> [options] <outfile>

Options:
    -h --help               Show this screen.
    -c --collection=<name>     Filter collection.
    -o --outdir=<dir>
    -n --outname=<name>        Filename
    -x --swap-axes=<axes>      Convert from Blender's axes [default: xz-y]
    -v                         Verbose mode, i.e. log everything
"""
import bpy
import sys
import os, logging
import re
from io_ogre import util

from os.path import join, split

log = logging.getLogger()

if __name__ == "__main__":
    import io_ogre.docopt.docopt
    try:
        idx = sys.argv.index('--')
        argv = sys.argv[idx+1:]
    except ValueError:
        argv = None

    cliargs = io_ogre.docopt.docopt.docopt(__doc__, argv, version='Naval Fate 2.0')

    if not cliargs['-v']:
        log.handlers = []
        log.addHandler(logging.NullHandler())


    from io_ogre import config
    from io_ogre.ogre2 import texture
    from io_ogre.ogre import mesh, skeleton

    # Update config
    config.CONFIG['SWAP_AXIS'] = cliargs['--swap-axes']


    dir = os.path.dirname(os.path.realpath(__file__))
    path = cliargs['--outdir'] if cliargs['--outdir'] else dir 
    name = cliargs['--outname'] if cliargs['--outname'] else None
    path = cliargs['<outfile>'] or cliargs['<outdir>']
    blendfile = cliargs['<blendfile>']

    bpy.ops.wm.open_mainfile(filepath=blendfile)

    log.debug(cliargs)

    files_written = []

    objs = [x for x in bpy.context.scene.objects if x.type == 'MESH']
    if cliargs['--collection']:
        objs = [x for x in objs if util.is_in_collection(x.users_collection, cliargs['--collection'])]

        count = len(objs)
        if count == 0:
            log.info(f"No mesh(es) found in collection '{cliargs['--collection']}'")
            exit()

        log.info(f"Found {count} mesh(es) in collection '{cliargs['--collection']}'")

    if cliargs['mesh']:
        outpath = '%s/%s.mesh.xml' % (path, os.path.basename(blendfile))
        files = mesh.dot_mesh_xml(
            objs,
            outpath.replace('.blend', ''),
            cliargs
        )
        files_written.extend(files)

    for obj in objs:
        outpath = '%s/%s.skeleton.xml' % (path, os.path.basename(blendfile))
        if cliargs['mesh']:
            files = skeleton.dot_skeleton(obj, outpath)
            files_written.extend(files)

        texture.export_textures(obj, path)

    print(' '.join(files_written))

    exit()
