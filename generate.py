import blenderproc as bproc
import numpy as np
import os

bproc.init()

objs = bproc.loader.load_blend("dune.blend")
poi = bproc.object.compute_poi(objs)
bproc.camera.set_resolution(512,512)

# Set some category ids for loaded objects
for j, obj in enumerate(objs):
    obj.set_cp("category_id", j + 1)

light = bproc.types.Light()
light.set_location([0, 0, 10])
light.set_energy(10000)

# Set the camera to be in front of the object
cam_pose = bproc.math.build_transformation_mat([0, -5, 0], [np.pi / 2, 0, 0])
for i in range(10000):
    location = np.random.uniform([-10, -10, 0], [10, 10, 5])
    rotation_matrix = bproc.camera.rotation_from_forward_vec(poi - location, inplane_rot = np.random.uniform(-0.7854, 0.7854))
    cam2world_matrix = bproc.math.build_transformation_mat(location, rotation_matrix)
    bproc.camera.add_camera_pose(cam2world_matrix)


# activate normal rendering
bproc.renderer.enable_normals_output()
bproc.renderer.enable_segmentation_output(map_by=["category_id", "instance", "name"])
bproc.camera.add_camera_pose(cam_pose)

# Render the scene
data = bproc.renderer.render()

# Write the rendering into an hdf5 file
bproc.writer.write_coco_annotations(os.path.join("./", 'coco_data'),
                                    instance_segmaps=data["instance_segmaps"],
                                    instance_attribute_maps=data["instance_attribute_maps"],
                                    colors=data["colors"],
                                    color_file_format="JPEG")
