import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells[0]), num_rows)
        self.assertEqual(len(maze._cells), num_cols)
    
    def test_maze_entrance_and_exit_exist(self):
        num_rows = 10
        num_cols = 12
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

if __name__ == "__main__":
    unittest.main()