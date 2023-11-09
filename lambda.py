a=int(input("enter the side of the square\n"))
area=lambda b:b*b
print("area of square",area(a))


a=int(input("enter the length of the rectangle"))
b=int(input("enter the breadth of the rectangle"))
area=lambda l,b:1*b
print("Area of the rectangle is",area(a,b))


a=int(input("enter the height of the triangle\n"))
b=int(input("enter the breadth of the triangle\n"))
area=lambda h,b:h*b
print("area of triangle is",area(a,b))
