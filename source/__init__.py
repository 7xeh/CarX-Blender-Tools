# Blender Add-on Metadata
bl_info = {
    "name": "7xeh's CarX Tools",
    "version": (1, 0, 0),
    "blender": (3, 6, 1),
    "author": "7xeh",
    "location": "View3D",
    "category": "Development",
}

import bpy
from . import CarXTools  # Import the main add-on script

def register():
    try:
        CarXTools.register()  # Register the add-on functionalities
    except Exception as e:
        print(f"Failed to register add-on: {e}")

def unregister():
    try:
        CarXTools.unregister()  # Unregister the add-on functionalities
    except Exception as e:
        print(f"Failed to unregister add-on: {e}")

if __name__ == "__main__":
    register()
