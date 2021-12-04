import bpy
import numpy as np
import os
import sys
path = r"..//code//"

if path not in sys.path:
    sys.path.append(path)
from CreateScene import delete_objs, create_landscape, add_bluerov, add_oyster, set_camera, set_light, add_plants
from utils import render_img
def start_pipeline(frame,floor_noise,landscape_texture_dir,surface_size,oysters_model_dir,oysters_texture_dir,n_clusters,min_oyster,max_oyster,oyster_range_x,oyster_range_y,out_dir):
    
    TIME_TO_WAIT=150

    # if output dir not present, make one
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # if render output dir not present, make one
    render_out_dir = os.path.join(out_dir, "render_output")
    
    # Delete all objects
    delete_objs()

    # set point source light
    set_light(0, 0, 10, 1000)
    
    # set camera
    camera,_=set_camera(0,0,2.5,0,0,0)

    # create a random landscape everytime
    print("creating landscape")
    create_landscape(floor_noise, landscape_texture_dir,surface_size)

    # import oysters at some random location according to cluster size
    add_oyster(oysters_model_dir,oysters_texture_dir, n_clusters, min_oyster, max_oyster,oyster_range_x,oyster_range_y)
#    plant_path="D:\\Programming\\underwater-perception\\data\\blender_data\\moss\\kkviz tillandsia usneoides_01.obj"
#    bpy.ops.import_scene.obj(filepath=plant_path)
#    print(bpy.context.object)

#    
#    for i in range(TIME_TO_WAIT):
#        print("waiting:",i)
#        bpy.context.scene.frame_set(i)
        
    bpy.context.scene.frame_set(TIME_TO_WAIT)
    
    # render image
    print("rendering frame:",frame)
    render_img(camera,out_dir=out_dir,i=frame)
    

if __name__=="__main__":
    
    # absolute path of the script
    script_path = os.path.dirname(os.path.abspath(__file__))

    # remove the last dir from path so that we are in base directory and can navigate further
    base_dir_path = script_path.split('code')[0]
    
    # output directory of saved images
    out_dir=base_dir_path + "//data/output//"

    # landscape parameters
    floor_noise = 100  # seabed smoothens out as the floor_noise is increased
    landscape_texture_dir = base_dir_path + "//data//blender_data//landscape//textures//"
    surface_size=5 # camera size

    # oysters paramteres
    oysters_model_dir = base_dir_path + "//data//blender_data//oysters//model//"
    oysters_texture_dir = base_dir_path + "//data//blender_data//oysters//textures//"
    n_clusters = 3
    min_oyster = 3
    max_oyster = 6

    # oyster dispersion range
    oyster_range_x=2
    oyster_range_y=1

    # number of random images
    n_images=20
    for frame in range(n_images):
        start_pipeline(frame,floor_noise,landscape_texture_dir,surface_size,oysters_model_dir,oysters_texture_dir,n_clusters,min_oyster,max_oyster,oyster_range_x,oyster_range_y,out_dir)

    print("Pipeline executed.")