# window details
RESOLUTION = (1200, 800)
FPS = 60

# scenes
class Scenes:
    PATHFINDER = "Pathfinder"
    MENU = "Menu"
    
# node states
class NodeState:
    PATH = "Path"
    OBSTACLE = "Obstacle"
    WALL = "Wall"
    START = "Start"
    DESTINATION = "Destination"
    EXPLORED = "Explored"
    OPTIMAL_PATH = "Optimal Path"
    
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