# window details
SCREEN_RESOLUTION = (1400, 800)
GRID_RESOLUTION = (1200, 800)
FPS = 60

# scenes
class Scenes:
    PATHFINDER = 1
    MENU = 2
    
# node states
class NodeState:
    PATH = 1
    OBSTACLE = 2
    WALL = 3
    START = 4
    DESTINATION = 5
    EXPLORED = 6
    OPTIMAL_PATH = 7
    
# algorithms
class Algorithms:
    BFS = "BFS"
    DIJKSTRA = "Dijkstra"
    GREEDY_BFS = "Greedy BFS"
    ASTAR = "A*"

# colors
class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PASTEL_LIME = (207, 255, 136)
    RED = (255, 58, 43)
    BLUE = (65, 59, 209)
    GREY = (203, 203, 203)
    PURPLE = (150, 93, 197)