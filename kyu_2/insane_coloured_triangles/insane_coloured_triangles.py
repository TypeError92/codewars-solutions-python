from math import floor, log

bottom_corner = {
    'R': {
        'R': 'R',
        'G': 'B',
        'B': 'G'
    },
    'G': {
        'R': 'B',
        'G': 'G',
        'B': 'R'
    },
    'B': {
        'R': 'G',
        'G': 'R',
        'B': 'B'
    }
}


def triangle(top_row):
    def square(row, column):
        if row:
            side_length = 3 ** floor(log(row, 3))
            left_corner = square(row - side_length, column)
            right_corner = square(row - side_length, column + side_length)
            return bottom_corner[left_corner][right_corner]
        return top_row[column]
    return square(len(top_row) - 1, 0)
