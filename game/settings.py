
import arcade

ROW_COUNT = 9
COLUMN_COUNT = 9
WIDTH = 70
HEIGHT = 70
MARGIN = 1

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "sudoku"

NUM_KEYS = {
        arcade.key.KEY_1 : 1,
        arcade.key.KEY_2 : 2,
        arcade.key.KEY_3 : 3,
        arcade.key.KEY_4 : 4,
        arcade.key.KEY_5 : 5,
        arcade.key.KEY_6 : 6,
        arcade.key.KEY_7 : 7,
        arcade.key.KEY_8 : 8,
        arcade.key.KEY_9 : 9,
}
