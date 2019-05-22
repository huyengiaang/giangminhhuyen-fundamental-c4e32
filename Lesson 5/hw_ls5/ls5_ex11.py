# Write a function is_inside that checks if a point is inside a rectangle.
def is_inside(a,b,x,y,w,h):
    # a,b are the coordinates of the point
    # x,y are the coordinates of top left angle of the rectangle
    # w,h are width and height of the rectangle
    if x<a<x+w:
        return True 
    else:
        return False
    if y<b<y+h:
        return True 
    else:
        return False
print(is_inside(200,120,140,60,100,200))

# check if is_inside function is correct. 
in_or_out = is_inside(100,120,140,60,0,0)
if in_or_out == False:
    print("Your function is correct.")
else:
    print("Oops, there's a bug. ")

