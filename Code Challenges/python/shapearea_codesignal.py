# polygon shape
#
# (User's) Problem
# We Have:
#     n
# We Need:
#     the area of a new type of polygon given: n
#    e.g.
#     n1 = 1
#     n2 = 2*2 + 1
#     n3 = 3*3 + 2*2
#     n4 = 4*4 + 3*3 + 2*2 + 1
# We Must:
#     return the area as an integer
#     calculate within 4 seconds
#
# Solution (Product)
#    A geometry of rotated tiles:
#     while a normal square figure has the volume: side^2
#     this kind of shape has an 'inner diagonal' space
#     that is (n-1)^2 in volume
#     kind of like a partial second dimension?
#     so the final volume is the sum of those two volumes n^2 + (n-1)^2


def shapeArea(n):
    polygon_area = 0

    # volume is n^2 + (n-1)^2
    polygon_area = n ** 2  # add the square
    polygon_area += (n - 1) ** 2  # add the square

    return polygon_area
