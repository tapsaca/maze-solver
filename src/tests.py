import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells[0]), num_rows)
        self.assertEqual(len(maze._cells), num_cols)
    
    def test_maze_break_entrance_and_exit(self):
        num_rows = 10
        num_cols = 12
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[num_cols - 1][num_rows - 1].has_bottom_wall)
    
    def test_maze_reset_cells_visited(self):
        num_rows = 10
        num_cols = 12
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        for column in maze._cells:
            for cell in column:
                self.assertEqual(cell.visited, False)

if __name__ == "__main__":
    unittest.main()