def decorator(func):
    def decorated(height, weight):
        if height < 0 or weight < 0:
            print("Error!")
        else:
            func(height,weight)
    return decorated

@decorator
def area_tri(height, weight):
    tri_area = 0.5 * weight * height
    print(tri_area)
@decorator
def area_square(height,weight):
    square_area = height * weight
    print(square_area)


area_tri(-4,-3)
area_square(2,3)