# CarX Blender Tools
<img align="right" src="https://raw.githubusercontent.com/7xeh/CarX-Blender-Tools/main/Media/blender_L4OJoXsrM9.png">

This is an updated version of an addon based on [Blender CarX Mod Tools](https://github.com/Zi9/Blender-CarX-Mod-Tools)

It generates an additional panel within the right toolbox (toggle with 'N') containing buttons for effortless material adjustment and placeholder creation.

Tested on Blender 4.2 LTS. Minimum supported: Blender 4.0. It should also work on 3.6 LTS via legacy fallbacks.


## Installation

To begin, please follow these steps:

1. Start by downloading the most recent version of the addon from the "[Releases](https://github.com/7xeh/CarX-Blender-Tools/releases)" section.

2. Next, launch Blender and navigate to the "Edit" menu, then select "Preferences..."

3. Inside the preferences window, find the "Add-ons" tab.

4. Within this tab, you'll see an "Install" button. Click on it and choose the zip file you just downloaded.

## Usage

- Open the sidebar (N) in the 3D Viewport and switch to the "CarX Blender Tools" tab.
- Set material/object prefixes, manage alpha modes, create placeholders (spawn, camera, lights).
- Use "Export Map" to export OBJ. On Blender 4.x this uses the new OBJ exporter; on 3.x it falls back to the legacy exporter.
- Use "Export Extra Data" to write a companion `.objdata` file (spawn points, cameras, lights).

## Troubleshooting

- If OBJ export fails, ensure the official "Wavefront OBJ format" add-on is enabled (Blender Preferences > Add-ons) on Blender 3.x. On 4.x, the built-in OBJ exporter should be available by default.
- If you see Python type warnings about bpy in your editor, they're harmless; they don't affect Blender runtime.