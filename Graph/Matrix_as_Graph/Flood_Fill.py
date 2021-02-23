from typing import List, Tuple
from collections import deque


def flood_fill(image: List[List[int]], start: Tuple[int, int], replacement_color: int) -> None:
    queue = deque([start])
    start_color = image[start[0]][start[1]]
    x_move = [-1, 0, 0, 1]
    y_move = [0, -1, 1, 0]
    while len(queue) != 0:
        point = queue.popleft()
        image[point[0]][point[1]] = replacement_color
        for i in range(4):
            new_x = point[0] + x_move[i]
            new_y = point[1] + y_move[i]
            if 0 <= new_x < len(image) and 0 <= new_y < len(image[0]):
                if image[new_x][new_y] == start_color:
                    queue.append((new_x, new_y))
    return


if __name__ == "__main__":
    # driver code, do not modify
    start = tuple(int(x) for x in input().split())
    color = int(input())
    image = [[int(x) for x in input().split()] for _ in range(int(input()))]
    flood_fill(image, start, color)
    for row in image:
        print(' '.join(str(x) for x in row))
