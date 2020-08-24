import random
from copy import deepcopy

class Sudoku:

    def __init__(self):
        self.generate_full_grid()
        self.generate_partial_grid()

    def remove_number_blocked_on(self, case):
        for row_case in self.grid.row(case.row_index):
            case.remove_free_number(row_case.value)
        for col_case in self.grid.col(case.col_index):
            case.remove_free_number(col_case.value)
        for square_case in self.grid.square(case.row_index, case.col_index):
            case.remove_free_number(square_case.value)

    def set_case_free_choices(self, case):
        case.init_free_numbers()
        self.remove_number_blocked_on(case)

    def generate_full_grid(self):
        self.grid = Grid()
        # on rempli case par case, si une case a plus de dispo, on remonte a la précédente, on lui interdit sa valeur actuelle, et on repart de la. Si elle a plus de dispo, on remonte encore, quand on retombe sur celle la, il faut ignorer les interdit, juste les bloqué sont pris en compte : pas besoin de stocker les interdits.
        case = self.grid.cases[0]
        while not self.grid.all_cases_value_set():#theres still a 0
            self.set_case_free_choices(case)

            case = self.backup_if_needed(case)

            case.value = random.choice(case.free_numbers)

            try:
                case = self.grid.next_case(case)
            except IndexError: 
                pass # can't find next case when all are ok.
            print('----')
            print(repr(self.grid))

    def backup_if_needed(self, case):
        while not case.free_numbers:
            case = self.grid.previous_case(case)
            case.remove_free_number(case.value)
            case.value = 0
            print('BAAAAAAACK')
            print('----')
            print(repr(self.grid))
        return case

    def generate_partial_grid(self):
        self.partial_grid = deepcopy(self.grid)
        case_to_remove = [
            (0, 3), (0, 4), (0, 5),
            (1, 1), (1, 2), (1, 3), (1, 5), (1, 6), (1, 7),
            (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
            (3, 0), (3, 1), (3, 4), (3, 7), (3, 8),
            (4, 0), (4, 1), (4, 3), (4, 4), (4, 5), (4, 7), (4, 8),
            (5, 0), (5, 1), (5, 4), (5, 7), (5, 8),
            (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
            (7, 1), (7, 2), (7, 3), (7, 5), (7, 6), (7, 7),
            (8, 3), (8, 4), (8, 5),
        ]
        for indexes in case_to_remove:
            self.partial_grid.case_by_indexes(*indexes).value = " "

class Grid:

    def __init__(self):
        self.cases = []
        for rind in range(9):
            for cind in range(9):
                self.cases.append(Case(rind, cind))

    def previous_case(self, case):
        previous_index = self.cases.index(case)-1
        return self.cases[previous_index]

    def next_case(self, case):
        next_index = self.cases.index(case)+1
        return self.cases[next_index]

    def all_cases_value_set(self):
        for case in self.cases:
            if case.value == 0:
                return False
        return True

    def case_by_indexes(self, rind, cind):
        for case in self.cases:
            if case.row_index == rind and case.col_index == cind:
                return case

    def row(self, rind):
        for case in self.cases:
            if case.row_index == rind:
                yield case

    def col(self, cind):
        for case in self.cases:
            if case.col_index == cind:
                yield case

    def square(self, rind, cind):
        for case in self.cases:
            if case.row_index in range(3*(rind//3), 3*(rind//3)+3):
                if case.col_index in range(3*(cind//3), 3*(cind//3)+3):
                    yield case

    def __repr__(self):
        return "\n".join([
            ",".join([
                str(self.case_by_indexes(rind, cind).value)
                for cind in range(9)
            ])
            for rind in range(9)
        ])

class Case:

    def __init__(self, row_index, col_index, value=0):
        self.row_index = row_index
        self.col_index = col_index
        self.value = value
        self.init_free_numbers()

    def init_free_numbers(self):
        self.free_numbers = list(range(1, 10))

    def remove_free_number(self, nb):
        if nb in self.free_numbers:
            self.free_numbers.remove(nb)
