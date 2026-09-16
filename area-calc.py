def area_rectangle(width, height):

    return width * height


def area_circle(radius):

    return 3.14159 * radius * radius


def area_triangle(base, height):
  
    return 0.5 * base * height


shape = input("Shape (rectangle / circle / triangle): ").strip().title()

if shape == "Rectangle":
    width = float(input("Width: "))
    height = float(input("Height: "))
    
    area = area_rectangle(width, height)
    
    print(f"Area of rectangle: {area}")

elif shape == "Circle":
    radius = float(input("Radius: "))
    
    area = area_circle(radius)
    
    print(f"Area of circle with radius {radius}: {area}")

elif shape == "triangle":
    base = float(input("Base: "))
    height = float(input("Height: "))
    
    area = area_triangle(base, height)
    
    print(f"Area of triangle: {area}")

else:
    print("Invalid shape")
