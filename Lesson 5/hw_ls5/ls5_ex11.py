# Write a function is_inside that checks if a point is inside a rectangle.
# def is_inside(a,b,x,y,w,h):
#     # a,b are the coordinates of the point
#     # x,y are the coordinates of top left angle of the rectangle
#     # w,h are width and height of the rectangle
#     if x<a<x+w:
#         return True 
#     else:
#         return False
#     if y<b<y+h:
#         return True 
#     else:
#         return False
# print(is_inside(200,120,140,60,43,70))

# # check if is_inside function is correct. 
# in_or_out = is_inside(100,120,140,60,0,0)
# if in_or_out == False:
#     print("Your function is correct.")
# else:
#     print("Oops, there's a bug. ")


# HOMEWORK CORRECTION
def is_inside(point,rect):
    if len(point) != 2:
        print("List has to have 2 elements.")
        return None
    print(point)
    print(rect)
    x0,y0,w,h = rect
    print((x0,y0,w,h))
    # x0 = rect[0]
    # y0 = rect[1]
    # w = rect[2]
    # h = rect[3]
    
    x,y = point
    # x = point[0]
    # y = point[1]

    if x<x0 or y<y0 or x>x0+w or y>y0+h:
        return False
    return True
print(is_inside([200,120],[140,60,100,200]))


