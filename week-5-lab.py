import random
from collections import deque

def solve_maze(maze):
    if not maze or not maze[0]:
        return None
    
    rows, cols = len(maze), len(maze[0])
    
    if maze[0][0] == 1 or maze[rows-1][cols-1] == 1:
        return None
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(0, 0, [(0, 0)])])  
    
    visited = set([(0, 0)])
    
    while queue:
        row, col, path = queue.popleft()
        
        if row == rows - 1 and col == cols - 1:
            return path
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                maze[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                new_path = path + [(new_row, new_col)]
                queue.append((new_row, new_col, new_path))
                visited.add((new_row, new_col))
    
    return None

maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 0]
]

result = solve_maze(maze)
if result:
    print("The path from start to end is:")
    for i, (row, col) in enumerate(result):
        if i < len(result) - 1:
            next_row, next_col = result[i + 1]
            print(f"({row}, {col}) -> ({next_row}, {next_col})")
else:
    print("No valid path found.")



class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_node, to_node):
        if from_node not in self.graph:
            self.graph[from_node] = []
        if to_node not in self.graph[from_node]:
            self.graph[from_node].append(to_node)

    def print_graph(self):
        for node in self.graph:
            print(f"{node}: {' '.join(self.graph[node])}")

def create_random_graph():
    g = Graph()
    nodes = [chr(i) for i in range(ord('A'), ord('N'))]  
    for node in nodes:
        num_edges = random.randint(1, 5) 
        for _ in range(num_edges):
            to_node = random.choice(nodes)
            if to_node != node:
                g.add_edge(node, to_node)
    return g

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph.graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

random_graph = create_random_graph()

print("Random Graph:")
random_graph.print_graph()

start_node = 'A'
goal_node = 'G'
path = bfs(random_graph, start_node, goal_node)

if path:
    print(f"\nPath from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"\nNo path found from {start_node} to {goal_node}")
    
    

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        nums = []
        if not root:
            return nums
        
        q = deque([root])

        while q:
            level_size = len(q)
            curr_level = []

            for _ in range(level_size):
                node = q.popleft()
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            nums.append(curr_level)
        
        return nums


# Function to create a sample binary tree
def create_sample_tree():
    """
    Create the following binary tree:
           1
          / \
         2   3
        / \   \
       4   5   6
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root

def main():
    tree_root = create_sample_tree()
    solution = Solution()
    result = solution.levelOrder(tree_root)
    print ("Level order traversal")
    print(result)

if __name__ == "__main__":
    main()
