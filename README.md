# Dependencies:
- Pygame

# Controls for Pathfinder
## Generic controls:
    - G: Clear board
    - B: Run algorithm
    - Escape: Settings
## In Mouse mode:
    - Left click: Walls
    - Ctrl + Left click: Obstacles
    - Middle click: Starting point
    - Ctrl + Middle click: Destination
    - Right click: Delete Tiles
## In Trackpad mode:
    - Click: Starting point
    - Ctrl + Click: Destination
    - D + Click: Delete Tiles
    - W + Click: Wall
    - 1 + Click: Obstacles

# Todo:
- Until the middle mouse button is released, walls affected by starting points/destinations will revert back to walls.
- Speed of program is not frame independant (CPU speed matters), so maybe that could be fixed while keeping a high framerate
- Make Grid data scalable on sideLength of nodes
- Add a scene-loading function to each scene for better abstraction