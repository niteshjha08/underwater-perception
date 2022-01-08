import bpy

def render_img(camera,out_dir,i):
    # bpy.data.cameras[camera].dof.use_dof = False
    bpy.context.scene.camera = bpy.data.objects[camera]

    save_path = out_dir+"//"+str(i)+'.png'
    r = bpy.context.scene.render
    r.resolution_x = 640
    r.resolution_y = 480
    r.filepath=save_path
    bpy.ops.render.render(write_still=True)