# pyright: reportMissingImports=false
# Blender Add-on Metadata
bl_info = {
    "name": "7xeh's CarX Tools",
    "version": (1, 2, 0),
    # Minimum Blender version supported
    "blender": (5, 0, 0),
    "author": "7xeh",
    "description": "Tools for preparing CarX maps: physics prefixes, alpha setup, placeholders, and OBJ export with extra data.",
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
