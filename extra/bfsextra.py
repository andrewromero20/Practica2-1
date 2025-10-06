import cv2
import numpy as np
from collections import deque

START_COORDS = (24, 915)
END_COORDS = (894, 209)

BLACK_COLOR = (0, 0, 0)
BLUE_COLOR = (255, 0, 0)

MAX_WIDTH = 1030
MAX_HEIGHT = 939

#Down, Up, Right, Left
directions = [(0,1), (0,-1), (1, 0), (-1, 0)]

# Load the image
img = cv2.imread('./bitmap.jpg')

#Tener un margen de movimiento de 3 pixeles
kernel = np.ones((3,3), np.uint8)
mask = cv2.inRange(img, BLACK_COLOR, BLACK_COLOR)
dilated = cv2.dilate(mask, kernel, iterations=5)

def can_move_to(x, y):
    return (0 <= x < MAX_WIDTH and 0 <= y < MAX_HEIGHT
            and not compare_colors(BLACK_COLOR, img[y][x]) and dilated[y][x] == 0)

def compare_vectors(a, b):
    return a[0] == b[0] and a[1] == b[1]

def compare_colors(a, b):
    is_equal = True

    for i, v in enumerate(a):
        if v != b[i]:
            is_equal = False
            break

    return is_equal

def bfs(start):
    visited = set()
    queue = deque([start])
    came_from = {}

    print("Searching the path. . .")

    while queue:
        node = queue.popleft()
        x, y = node


        if node not in visited:
            visited.add(node)
           # img[y][x] = BLUE_COLOR

            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy

                if compare_vectors((next_x, next_y), END_COORDS):
                    came_from[(next_x, next_y)] = node
                    reconstruct_path(came_from, end=END_COORDS)
                    return

                if can_move_to(next_x, next_y) and (next_x, next_y) not in visited:
                    queue.append((next_x, next_y))
                    came_from[(next_x, next_y)] = node

def reconstruct_path(nodes, end):
    print("Reconstructing the path")

    current_vector = end
    path = []

    while not compare_vectors(current_vector, START_COORDS):
        path.append(current_vector)
        tmp = current_vector
        current_vector = nodes[tmp]

    mask_path = np.zeros((MAX_HEIGHT, MAX_WIDTH), np.uint8)

    for x,y in path:
        mask_path[y][x] = 255

    kernel_path = np.ones((5,5), np.uint8)
    mask_path_thick = cv2.dilate(mask_path, kernel_path, iterations=1)

    img[mask_path_thick == 255] = (0, 0, 255)

    for v in path:
        img[v[1]][v[0]] = (0,0,255)

bfs(START_COORDS)


cv2.imwrite("resultado.jpg", img)
cv2.destroyAllWindows()