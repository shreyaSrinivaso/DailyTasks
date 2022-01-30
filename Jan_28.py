#write a program to calculate perimeter of the circle with radius 10.2
radius=10.2
PerimeterOfCircle = 2*3.14*radius
print("Perimeter of circle with radius {} is {}".format(radius,PerimeterOfCircle))

#write a program to calculate area of circle with radius (float) (collect using input function)
Radius_2=float(input("Enter Radius(Float value):"))
Area=3.14*(Radius_2**2)
print("Area of circle with radius {} is {}".format(float(radius),Area))

#write a program to calculate perimeter of the cricle with radius (float) (collect it through input function)
Radius_3=float(input("Enter Radius(Float value):"))
Perimeter_2=2*3.14*Radius_3
print("Perimeter of circle with radius {} is {}".format(Radius_3,Perimeter_2))

#Collect radius and height from user,calculate Area of cone (area of cone = 0.33 * pi * r * r * h) (int)
height=int(input("Enter the required height(int value):"))
radiuss=int(input("Enter the required radius (int value):"))
AreaOfCone=0.33*3.14*radiuss**2*height
print("Area of cone with height {} and radius {} is {}".format(height,radiuss,AreaOfCone))