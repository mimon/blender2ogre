import logging
log = logging.getLogger(__name__)

def flatten(list):
    return [item for sublist in list for item in sublist]

def textures(nodes):
    return [x for x in nodes if x.type == 'TEX_IMAGE']

def get_textures(ob):
    materials = [x.material for x in ob.material_slots if x.material]
    nodes = [x.node_tree.nodes for x in materials if x.node_tree]

    textures_per_material = [textures(x) for x in nodes]
                        
    return flatten(textures_per_material)

def export_textures(obj, path):
  textures = get_textures(obj)
  log.info(f"Found {len(textures)} texture(s) to export")
  for t in textures:
      filename = f"{t.image.name_full}.{t.image.file_format}"
      log.info(f"Exporting {filename}")
      t.image.save_render(f'{path}/{filename}')
