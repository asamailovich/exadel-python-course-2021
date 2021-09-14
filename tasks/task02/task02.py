import math
print("Welcome to the triangle area calculation tool.")
menu = '''Menu:
1. Calculate triangle area by base and height
2. Calculate triangle area by 2 sides and angle between them
3. Exit
'''
while True:
    print(menu)
    try:
        p = int(input("Enter menu item number: "))
    except ValueError:
        print("Incorrect input, please input a number")
    else:
        if p == 3:
            break
        elif p == 1:
            s = input("Enter base and height: ")
            parts = s.split()
            base = int(parts[0])
            height = int(parts[1])
            print(f'Area is: {0.5 * base * height}')
        elif p == 2:
            s = input("Enter 2 sides and angle(degrees) between them: ")
            parts = s.split()
            side1 = int(parts[0])
            side2 = int(parts[1])
            degree = int(parts[2])
            print(f'Area is: {0.5 * side1 * side2 * math.sin(math.radians(degree))}')
