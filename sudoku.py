
import arcade

from game_settings import *
from game_logics import Sudoku

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.sudoku = Sudoku()
        self.selected_case = None
    
    def on_draw(self):
        arcade.start_render()

        for row, column in self.all_cases_position():
            x, y = self.pixel_position(row, column)
            sudoku_case = self.sudoku.partial_grid.case_by_indexes(row, column)

            color = arcade.color.LIGHT_GRAY
            if sudoku_case == self.selected_case:
                color = arcade.color.WHITE

            # Draw the box
            arcade.draw_rectangle_filled(
                x,
                y,
                WIDTH,
                HEIGHT,
                color
            )
            arcade.draw_text(
                str(sudoku_case.value),
                x-15,
                y-25,
                arcade.color.BLACK,
                40
            )
                

    def pixel_position(self, row, column):
        y = SCREEN_HEIGHT - ((MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2)
        x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
        return x, y

    def all_cases_position(self):
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                yield row, column

    def on_mouse_press(self, x, y, button, modifiers):
        for row, column in self.all_cases_position():
            xrow, ycol = self.pixel_position(row, column)
            if xrow - WIDTH//2 < x < xrow + WIDTH//2 and ycol - HEIGHT//2 < y < ycol + HEIGHT//2:
                case = self.sudoku.partial_grid.case_by_indexes(row, column)
                if case.value == " ":
                    self.selected_case = case

    def on_key_press(self, key, modifiers):
        if key not in NUM_KEYS.keys():
            return
        case = self.sudoku.partial_grid.case_by_indexes(self.selected_case.row_index, self.selected_case.col_index)
        case.value = NUM_KEYS[key]
        self.selected_case = None

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
