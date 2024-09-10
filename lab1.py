def sum(num1, num2):
    return num1 + num2

def find_velocity_of_moving_object(distance, time):
    return distance/time

def check_positive_or_negative(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def find_volume_of_cylinder(r, h):
    return 3.14 * r**2 * h

def calculate_sales_tax_on_item(cost, tax_rate):
    return cost * tax_rate

def calculate_grade_of_student(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"
 

def main():
    print(f"The sum of 10 and 20 is: {sum(10, 20)}")
    print(f"The velocity of the moving object is: {find_velocity_of_moving_object(100, 20)} m/s")
    print(f"The number -15 is: {check_positive_or_negative(-15)}")
    print(f"The volume of the cylinder is: {find_volume_of_cylinder(5, 10)} cubic units")
    print(f"The sales tax on the item is: {calculate_sales_tax_on_item(100, 0.07)}")
    print(f"The grade of the student is: {calculate_grade_of_student(85)}")

if __name__ == "__main__":
    main()



      
