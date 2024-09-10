import math

def print_num_and_square_upto_10():
    for num in range(1, 11):
        print(f"{num} squared is: {num**2}")
        
def check_vowel_or_consonant(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter.lower() in vowels:
        return "Vowel"
    else:
        return "Consonant"

def print_even_odd(start, end):
    even_numbers = []
    odd_numbers = []
    
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    print("Even Numbers:", even_numbers)
    print("Odd Numbers:", odd_numbers)

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print_even_odd(start_range, end_range)

def calculate_points(books_purchased):
    if books_purchased == 0:
        points = 0
    elif books_purchased == 1:
        points = 5
    elif books_purchased == 2:
        points = 15
    elif books_purchased == 3:
        points = 30
    elif books_purchased >= 4:
        points = 60
    else:
        points = 0  

    return points
  
points = int(input("Enter the number of books purchased: "))

print(f"The points earned are: {calculate_points(points)}")

def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def circle_area_circumference(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

def cylinder_volume_surface_area(radius, height):
    volume = math.pi * radius ** 2 * height
    surface_area = 2 * math.pi * radius * (radius + height)
    return volume, surface_area

def display_menu():
    print("\nSelect a shape to calculate:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Cylinder")
    print("4. Exit")
    
def add_numbers():
    total = 0
    while True:
        num = input("Enter a number to add (or type 'done' to finish): ")
        if num.lower() == 'done':
            break
        try:
            total += float(num)
        except ValueError:
            print("Invalid input, please enter a valid number.")
    return total

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area, perimeter = rectangle_area_perimeter(length, width)
            print(f"Rectangle Area: {area}")
            print(f"Rectangle Perimeter: {perimeter}")

        elif choice == '2':
            radius = float(input("Enter the radius of the circle: "))
            area, circumference = circle_area_circumference(radius)
            print(f"Circle Area: {area}")
            print(f"Circle Circumference: {circumference}")

        elif choice == '3':
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            volume, surface_area = cylinder_volume_surface_area(radius, height)
            print(f"Cylinder Volume: {volume}")
            print(f"Cylinder Surface Area: {surface_area}")

        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
    
total_sum = add_numbers()
print(f"Total Sum: {total_sum}")

