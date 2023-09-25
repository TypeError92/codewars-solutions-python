from random import choice
from sys import path
path.append('../../..')
from codewars_solutions_python.kyu_7.coloured_triangles.coloured_triangles import triangle
from insane_coloured_triangles import triangle as insane_triangle


def test_suite1():
    for iteration in range(100):
        length = choice(range(10**0, 10**1))
        row = ''
        for i in range(length):
            row += choice('RGB')
        simple = triangle(row)
        insane = insane_triangle(row)
        assert insane_triangle(row) == triangle(row)


def test_suite2():
    for iteration in range(100):
        length = choice(range(10**1, 10**2))
        row = ''
        for i in range(length):
            row += choice('RGB')
        simple = triangle(row)
        insane = insane_triangle(row)
        assert insane_triangle(row) == triangle(row)

