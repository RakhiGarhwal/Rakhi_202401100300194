# -*- coding: utf-8 -*-
"""Rakhi_202401100300194

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BbQ_SUP2UEGaYw2WI1VgpEhH1q_UDSKx
"""

import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (x, y) coordinates of the node
        self.parent = parent  # Parent node to trace back the path
        self.g = 0  # Cost from start node to this node
        self.h = 0  # Estimated cost from this node to goal (heuristic)
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f  # Compare nodes based on their f value for priority queue

def heuristic(a, b):
    # Calculate Manhattan distance as the heuristic (absolute difference in x and y coordinates)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, end):
    open_list = []  # Priority queue to store nodes to be explored
    closed_set = set()  # Set to store visited nodes
    start_node = Node(start)  # Create start node
    goal_node = Node(end)  # Create goal node
    heapq.heappush(open_list, start_node)  # Add start node to priority queue

    while open_list:
        current_node = heapq.heappop(open_list)  # Get node with lowest f value

        if current_node.position == goal_node.position:
            # If we reached the goal, reconstruct the path
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent  # Move to parent node
            return path[::-1]  # Return reversed path (from start to goal)

        closed_set.add(current_node.position)  # Mark node as visited

        # Explore neighboring nodes (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)

            # Skip if the neighbor is out of bounds or is a wall (1 in the maze)
            if (neighbor_pos in closed_set or
                neighbor_pos[0] < 0 or neighbor_pos[0] >= len(maze) or
                neighbor_pos[1] < 0 or neighbor_pos[1] >= len(maze[0]) or
                maze[neighbor_pos[0]][neighbor_pos[1]] == 1):
                continue

            # Create a new node for the neighbor
            neighbor = Node(neighbor_pos, current_node)
            neighbor.g = current_node.g + 1  # Increment g cost (movement cost)
            neighbor.h = heuristic(neighbor_pos, goal_node.position)  # Compute heuristic
            neighbor.f = neighbor.g + neighbor.h  # Compute total cost

            heapq.heappush(open_list, neighbor)  # Add neighbor to the priority queue

    return None  # No path found

# Example usage
maze = [
    [0, 1, 0, 0, 0],  # 0 = open path, 1 = obstacle
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)  # Start position (row, column)
end = (4, 4)  # Goal position (row, column)
path = astar(maze, start, end)  # Find the shortest path
print("Path:", path)  # Print the path from start to goal