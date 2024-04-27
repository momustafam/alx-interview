#!/usr/bin/python3
'''Simple module since it has one simple function (pascal_triangle).'''


def pascal_triangle(nrows):
    '''Represent the pascal's triangle using a list of lists of integers.
    
        Paramters:
            - nrows (int): number of triangle's rows

        Return: A list of lists of integers
    '''
    pascals_triangle = []

    for row in range(nrows):
        row_values = []
        for col in range(row+1):
            if col == 0 or col == row:
                row_values.append(1)
            else:
                row_values.append(pascals_triangle[row-1][col] + pascals_triangle[row-1][col-1])
        pascals_triangle.append(row_values)
    return pascals_triangle
