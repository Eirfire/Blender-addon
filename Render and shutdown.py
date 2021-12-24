bl_info = {
    "name": "Render and shutdown pc",
    "author": "Jacob Samorowski email:jacob35422@gmail.com",
    "version": (0, 0, 1),
    "blender": (2, 65, 0),
    "location": "render > Render and shutdown",
    "description": "Once render is finished it will save the blend file and shutdown your pc",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "Render",
}
import random
import bpy
import os
from bpy.props import *
from bpy.types import (Panel,Menu,Operator,PropertyGroup)


def some_other_function(dummy):
    print("Render complete")
    bpy.ops.wm.save_mainfile()
    bpy.ops.wm.quit_blender() #instead of quitting blender shutdown computer: os.system("shutdown /s /t 1") 




    


# Will be executed once when the whole rendering process is completed



#--------------------------------------------------------
                #Operators
#--------------------------------------------------------




#--------------------------------------------------------
                #Panels
#--------------------------------------------------------

               
class TestPanel(bpy.types.Panel):

    bl_label = "Render and shutdown"
    bl_idname = "PT_Test"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Render extras'


    def draw(self, context):
        layout = self.layout
        view = context.space_data
        row = layout.row()
        EItool = scene.EI_tool

        row.prop(EItool, " Render_Shutdown")

        
        if  Render_Shutdown == True:
            bpy.app.handlers.render_complete.append(some_other_function)
        


   






#--------------------------------------------------------
                #Menus
#--------------------------------------------------------





       
 






#--------------------------------------------------------
                #Properties 
#--------------------------------------------------------



class EirfireProperties(PropertyGroup):
    
    Render_Shutdown: bpy.props.BoolProperty(
        Render_Shutdown="Shutdown computer",
        description="Once a render is finihsed shutdown computer",
        default = False
        )
    

#Refence of a check box working in blender
"""class CYCLES_RENDER_PT_sampling_render_denoise(CyclesButtonsPanel, Panel):
    bl_label = "Denoise"
    bl_parent_id = 'CYCLES_RENDER_PT_sampling_render'
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        scene = context.scene
        cscene = scene.cycles

        self.layout.prop(context.scene.cycles, "use_denoising", text="")

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        scene = context.scene
        cscene = scene.cycles"""

    
    
            
  
#--------------------------------------------------------
                #Notes
#--------------------------------------------------------
   

#Once a render is finished

#save file 
#bpy.ops.wm.save_mainfile()

#shutdown computer
#os.system("shutdown /s /t 1") 

#close blender aplication
#bpy.ops.wm.quit_blender()

#--------------------------------------------------------
                #Register and Unregister plus keymaps
#--------------------------------------------------------






addon_keymaps = []

classes = [TestPanel,
EirfireProperties,

]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.EI_tool = bpy.types.PointerProperty(type=EirfireProperties)

   
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    


if __name__ == '__main__':
    register()
