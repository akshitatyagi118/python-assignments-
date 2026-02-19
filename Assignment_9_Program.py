import Assignment_9_Shapes

print("Choose a shape to find area:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
	r = float(input("Enter radius of circle: "))
	area = Assignment_9_Shapes.area_circle(r)
	print("Area of Circle =", area)

elif choice == 2:
	l = float(input("Enter length of rectangle: "))
	w = float(input("Enter width of rectangle: "))
	area = Assignment_9_Shapes.area_rectangle(l, w)
	print("Area of Rectangle =", area)

elif choice == 3:
	l = float(input("Enter length of triangle: "))
	w = float(input("Enter width of triangle: "))
	area = Assignment_9_Shapes.area_triangle(l, w)
	print("Area of Triangle =", area)

else:
	print("Invalid choice")