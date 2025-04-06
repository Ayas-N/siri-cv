from pathlib import Path
import numpy as np
import h5py
import json
 
if __name__ == '__main__':
  dataset_path = Path('examples/advanced/coco_annotations/output')
  for scene_folder in dataset_path.iterdir():
    if not scene_folder.is_dir():
      continue
    print(f'Reading scene {scene_folder.name}')
    for sample in scene_folder.iterdir():
      if not sample.name.endswith('.hdf5'):
          continue
      print(f'\tReading sample {sample.name}')
      with h5py.File(sample) as f:
          # Image data
          keys = ['colors', 'depth', 'normals', 'class_segmaps', 'instance_segmaps']
          for key in keys:
             if key in f:
                data = np.array(f[key])
                print(f'\t\t{key}: shape = {data.shape}, type = {data.dtype}')
          # Json objects
          if 'instance_attribute_maps' in f:
            print('\t\tMapping between instance and class:')
            text = np.array(f['instance_attribute_maps']).tobytes()
            json_rep = json.loads(text)
            print(json_rep)
            print()
 
          if 'object_data' in f:
            text = np.array(f['object_data']).tobytes()
            json_rep = json.loads(text)
 
            for object_idx, object_data in enumerate(json_rep):
              print(f'\t\tObject {object_idx} data: ')
              for obj_k in object_data.keys():
                print(f'\t\t\t{obj_k} = {object_data[obj_k]}')
              print()