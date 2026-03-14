from tree import create_tree
from search import dfs, bfs
from game import play_game

root = create_tree()

print("\n--- DFS ---")
dfs(root)

print("\n--- BFS ---")
bfs(root)

print("\n--- JOGO ---")
play_game(root)
