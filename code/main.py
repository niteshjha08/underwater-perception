import bpy
from code.CreateScene import SURFACE_SIZE
import numpy as np
import os
import sys
path = r"..//code//"

if path not in sys.path:
    sys.path.append(path)
from CreateScene import delete_objs, create_landscape, add_bluerov, add_oyster, set_camera, set_light

def start_pipeline(floor_noise,landscape_texture_dir,surface_size,oysters_model_dir,oysters_texture_dir,n_clusters,min_oyster,max_oyster):
    # Delete all objects
    delete_objs()

    # set point source light
    set_light(0, 0, 30, 1000)

    # create a random landscape everytime
    create_landscape(floor_noise, landscape_texture_dir,surface_size)

    # import oysters at some random location according to cluster size
    add_oyster(oysters_model_dir,oysters_texture_dir, n_clusters, min_oyster, max_oyster)

    # import blueROV 3d model 
    front_cam, bottom_cam = add_bluerov(bluerov_model_path, bluerov_location)



if __name__=="__main__":
    
    # absolute path of the script
    script_path = os.path.dirname(os.path.abspath(__file__))

    # remove the last dir from path so that we are in base directory and can navigate further
    base_dir_path = script_path.split('code')[0]

    # landscape parameters
    floor_noise = 3.5  # seabed smoothens out as the floor_noise is increased
    landscape_texture_dir = base_dir_path + "//data//blender_data//landscape//textures//"
    surface_size=80

    # oysters paramteres
    oysters_model_dir = base_dir_path + "//data//blender_data//oysters//model//"
    oysters_texture_dir = base_dir_path + "//data//blender_data//oysters//textures//"
    n_clusters = 1
    min_oyster = 1
    max_oyster = None

    # blueRov parameters, initial position and orientation
    bluerov_model_path = base_dir_path + "//data//blender_data//blueROV//BlueRov2.dae"
    bluerov_location = (-0.85, -0.65, 7.45)
    bluerov_orientation = (1.57, 0, 1.57)

    # bluerov motion path
    motion_path = {
        0+TIME_TO_WAIT: [bluerov_location, bluerov_orientation],
        80+TIME_TO_WAIT: [(bluerov_location[0]+4.5, bluerov_location[1], bluerov_location[2]),
        (bluerov_orientation[0], bluerov_orientation[1], bluerov_orientation[2])],
        100+TIME_TO_WAIT: [(bluerov_location[0]+5, bluerov_location[1], bluerov_location[2]),
        (bluerov_orientation[0], bluerov_orientation[1]+0.2, bluerov_orientation[2]+1.57)],
        180+TIME_TO_WAIT: [(bluerov_location[0]+4.5, bluerov_location[1]+2.3, bluerov_location[2]+0.7),
        (bluerov_orientation[0], bluerov_orientation[1]+0.1, bluerov_orientation[2]+1.57)],
        200+TIME_TO_WAIT: [(bluerov_location[0]+4, bluerov_location[1]+2.8, bluerov_location[2]+1),
        (bluerov_orientation[0], bluerov_orientation[1]+0.1, bluerov_orientation[2]+2.8)],
        300+TIME_TO_WAIT: [(bluerov_location[0], bluerov_location[1]+5, bluerov_location[2]),
        (bluerov_orientation[0], bluerov_orientation[1], bluerov_orientation[2]+2.8)]
                    }

    start_pipeline(floor_noise,landscape_texture_dir,surface_size,oysters_model_dir,oysters_texture_dir,n_clusters,min_oyster,max_oyster)

    print("Pipeline executed.")