import math
import pprint
import queue
from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia

pp = pprint.PrettyPrinter(indent=4)
data = generar_muestra_pais(7)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.depth = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node 


    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def pre_order(self):
        print(self.depth)
        print(self.value)
        
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

"""
def knn(k):
    kdtree = build_kdtree(data)
    pp.print(kdtree)

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx * dx + dy * dy)

def kdtree_closest_point(root, point, depth=0):
    if root is None:
        return None
    axis = depth % k
    next_branch = None
    opposite_branch = None
    if point[axis] < root['point'][axis]:
        next_branch = root['left']
        opposite_branch = root['right']
    else:
        next_branch = root['right']
        opposite_branch = root['left']
    best = closer_distance(point,kdtree_closest_point(next_branch,point,depth + 1),root['point'])
    if distance(point, best) > abs(point[axis] - root['point'][axis]):
        best = closer_distance(point,kdtree_closest_point(opposite_branch,point,depth + 1),best)
    return best
"""
def build_kdtree(points, depth=0):
    n = len(points)
    if n <= 0:
        return None
    kd = len(points[0])
    axis = depth % kd
    sorted_points = sorted(points, key=lambda point: point[axis])
    #print("depth")
    #print(depth)
    #print(sorted_points)
    medium = int(n/2)
    #print(n/2)
    node = BinaryTree(sorted_points[medium])
    node.depth = depth
    node.left_child = build_kdtree(sorted_points[:medium], depth + 1)
    node.right_child = build_kdtree(sorted_points[medium + 1:], depth + 1)
    return node

kdtree = build_kdtree(data)
print("")
kdtree.pre_order()
#print(kdtree.value)
#print(kdtree.right_child.value)
#print(kdtree.left_child.value)

