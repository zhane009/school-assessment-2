import math
import os
import time
import turtle

# declare the functions for all the area and perimeter calculations
def square(side):
    area = side * side
    perimeter = side * 4

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm")

def rectangle(side1, side2):
    area = side1 * side2
    perimeter = (side1 * 2) + (side2 * 2)

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm")

def circle(radius):
    area = math.pi * radius * radius
    perimeter = 2 * math.pi * radius

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm")

def equilateralTriangle(side):
    area = 0.25 * (math.sqrt(side * 3)) * (math.sqrt(side)) * (math.sqrt(side)) * (math.sqrt(side))
    perimeter = side * 3

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm")

def isoscelesTriangle(side1And2, side3):
    side1, side2 = side1And2, side1And2

    area = 0.25 * (math.sqrt(side1 + side2 + side3)) \
           * (math.sqrt(side1 + side2 - side3)) \
           * (math.sqrt(side1 - side2 + side3)) \
           * (math.sqrt(-side1 + side2 + side3))
    perimeter = side1 + side2 + side3

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm")

def rightTriangle(side1, side2, side3):

    area = 0.25 * (math.sqrt(side1 + side2 + side3)) \
           * (math.sqrt(side1 + side2 - side3)) \
           * (math.sqrt(side1 - side2 + side3)) \
           * (math.sqrt(-side1 + side2 + side3))

    perimeter = side1 + side2 + side3

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm")

def normalTriangle(side1, side2, side3):
    area = 0.25 * (math.sqrt(side1 + side2 + side3)) \
               * (math.sqrt(side1 + side2 - side3)) \
               * (math.sqrt(side1 - side2 + side3)) \
               * (math.sqrt(-side1 + side2 + side3))

    perimeter = side1 + side2 + side3

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm")

def parallelogram(side1, side2, angle):
    area = side1 * side2 * math.sin(math.radians(angle))
    perimeter = (side1 * 2) + (side2 * 2)

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm")

def hexagon(side):
    area = 3 * (math.sqrt(3)) * side * side / 2
    perimeter = side * 6

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm")


# the class that will perform all the main non-math things
class calculate:

    def cal(self):
        print("\n1.Squres"    # let the user choose one of the shapes
              "\n2.Rectangles"
              "\n3.Circles"
              "\n4.Triangles"
              "\n5.Parallelograms"
              "\n6.Hexagons"
              "\n7.Back to main menu")

        while(True): # check the input is an integer or not and loop until an integer is entered
            try:
                category = int(input("Please select a shape:"))
                break
            except:
                print("Please input a number only")

        if (category == 1):
            while(True):    # to check whether the input value is positive or not and loop until it is positive
                while(True):    # to check whether the input value is an integer or not
                    try:
                        side = float(input("\nInput the length of the side in cm : "))  # ask for user to input the value of the side
                        break   # break the loop if there's no error
                    except:
                        print("\nPlease input a number only")   # handle the error

                if (side>0):    # if the value is positive
                    square(side)  # call the function to calculate the area and the perimeter
                    calculate.cal(self)  # recursion
                    break   # break the loop
                else:
                    print("\nPlease input a positive value.")   # ask the uesr to try again

        elif (category == 2):
            while(True):
                while(True):
                    try:
                        side1 = float(input("\nInput the length of the first side in cm : "))
                        side2 = float(input("Input the length of the second side in cm : "))
                        break

                    except:
                        print("\nPlease input a number only")

                if not(side1 < 0 or side2 < 0):
                    rectangle(side1, side2)
                    calculate.cal(self)
                    break

                else:
                    print("\nPlease input positive values only")


        elif (category == 3):
            while (True):
                while (True):
                    try:
                        radius = float(input("\nInput the length of the radius in cm : "))
                        break
                    except:
                        print("\nPlease input a number only")

                if (radius > 0):
                    circle(radius)
                    calculate.cal(self)
                    break

                else:
                    print("\nPlease input positive values only")

        elif (category == 4):
            # let the user choose one of the triangle types
            print("\n1.Equilateral Triangle"   # all three sides are equal to each other
                  "\n2.Isosceles Triangle"     # two sides are equal to each other
                  "\n3.Right Triangle"         # a triangle with a right angle
                  "\n4.Normal Triangle(can be any one from the above three)"        # can be one or none of the above
                  "\n5.Back")           # go back to main menu

            while(True):
                try:
                    type = int(input("Choose one triangle type : "))
                    break
                except:
                    print("Plese only enter a valid option")

            if (type == 1):
                while(True):
                    while(True):
                        try:
                            side = float(input("\nInput the length of the side in cm : "))
                            break
                        except:
                            print("\nPlease input a number only")

                    if (side > 0):
                        equilateralTriangle(side)
                        calculate.cal(self)
                        break

                    else:
                        print("\nPlease input positive values only.")

            elif (type == 2):
                while(True):
                    while(True):
                        try:
                            side1And2 = float(input("\nInput the length of the two equal sides in cm : "))
                            side3 = float(input("Input the length of the third side in cm : "))
                            break
                        except:
                            print("\nPlease input a number only")

                    side1, side2 = side1And2, side1And2

                    if not(side1And2 < 0 or side3 < 0):     # first check if the sides are positive
                        if (((side1 + side2) > side3)   # check if the triangle is valid or not
                                and ((side1 + side3) > side2)
                                and ((side2 + side3) > side1)):
                            isoscelesTriangle(side1And2, side3)
                            calculate.cal(self)
                            break       # loop until a valid triangle is entered

                        else:
                            print("Your three sides do not make up a valid triangle.\nPlease try again.")   # let the user try again if not valid

                    else:
                        print("\nPlease input positive values only")

            elif (type == 3):
                while (True):
                    while(True):
                        try:
                            side1 = float(input("\nInput the length of the first side in cm : "))
                            side2= float(input("Input the length of the second side in cm : "))
                            side3 = float(input("Input the length of the third side in cm : "))
                            break
                        except:
                            print("\nPlease input a number only")


                    if not(side1 < 0 or side2 < 0 or side3 < 0):

                        if ((((side1 * side1) + (side2 * side2)) == (side3 * side3)) # cheak if the three sides satisfy the Pythagora's Theorem
                                or (((side1 * side1) + (side3 * side3)) == (side2 * side2))
                                or (((side3 * side3) + (side2 * side2)) == (side1 * side1))):

                            rightTriangle(side1, side2, side3)
                            calculate.cal(self)# if yes, calculate the area and the perimeter
                            break       # loop until the three sides make up a valid right triangle

                        else:
                            print("\nYour three sides do not make up a valid triangle.\nPlease try again.") # if not, ask the user to input again

                    else:
                        print("\nPlease input positive values only.")


            elif (type == 4):
                while (True):
                    while (True):
                        try:
                            side1 = float(input("\nInput the length of the first side in cm : "))
                            side2 = float(input("Input the length of the second side in cm : "))
                            side3 = float(input("Input the length of the third side in cm : "))
                            break
                        except:
                            print("\nPlease input a number only")

                    if not (side1 < 0 or side2 < 0 or side3 < 0):

                        if (((side1 + side2) > side3) # check if the three sides make up a valid triangle
                                and ((side1 + side3) > side2)
                                and ((side2 + side3) > side1)):
                            normalTriangle(side1, side2, side3) # if yes, calculate the area and the perimeter
                            calculate.cal(self)
                            break       # loop until the three sides make up a valid triangle
                        else:
                            print("\nThe three sides you entered do not make up a valid triangle.\nPlease try again.") # if not, ask the user to input again

                    else:
                        print("\nPlease input positive values only.")

            elif (type == 5):
                print("\n")         # for some separation
                calculate.cal(self)

            else:
                print("\nPlease input a valid option only.")

        elif (category == 5):
            while (True):
                while(True):
                    try:
                        side1 = float(input("\nInput the length of the first side in cm : "))
                        side2 = float(input("Input the length of the second side in cm : "))
                        angle = float(input("Input the degree of the angle between the two sides in degrees : "))
                        break
                    except:
                        print("\nPlease input a number only")

                if not (side1 < 0 or side2 < 0 or angle < 0):
                    if (angle > 180):
                        print("\nYour angle cannot be greater than 180 degrees")

                    else:
                        parallelogram(side1, side2, angle)
                        calculate.cal(self)
                        break

                else:
                    print("\nPlease input positive values only")

        elif (category == 6):
            while (True):
                while (True):
                    try:
                        side = float(input("\nInput the length of the side in cm : "))
                        break
                    except:
                        print("\nPlease input a number only")

                if (side > 0):
                    hexagon(side)
                    calculate.cal(self)
                    break
                else:
                    print("\nPlease input positive values only")

        elif (category == 7):
            print("\nGoing back to main menu\n")
            time.sleep(1)
            execute.exe()

        else:
            print("\nPlease input a valid option")
            calculate.cal(self)

class draw2d():

    def rectangle(self):
        side1 = int(input("\ninput the height of the rectangle : "))
        side2 = int(input("input the length of the rectangle : "))
        print("\n")
        i = 0
        n = 0
        line = ""
        while (i < side1):
            while (n < side2):
                if ((i == 0) or (i == side1 -1)):
                    line += "*  "

                elif ((n == 0) or (n == side2 - 1)):
                    line += "*  "

                else:
                    line += "   "
                n += 1
            n = 0
            i += 1
            print(line)
            line = ""

    def square(self):
        side = int(input("\ninput the side of the square : "))
        print("\n")
        i = 0
        n = 0
        line = ""
        while (i < side):
            while (n < side):
                if ((i == 0) or (i == side - 1)):
                    line += "*  "

                elif ((n == 0) or (n == side - 1)):
                    line += "*  "

                else:
                    line += "   "

                n += 1
            n = 0
            i += 1
            print(line)
            line = ""

    def triangle(self):
        height = int(input("\ninput the height of the triangle : "))
        print("\n")
        i = height
        n = height
        j = 0
        line = ""

        while (i > 0):
            while (n > i):
                line += "   "
                n -= 1

            while (j < i):
                if (i == height):
                    line += "#  "

                elif ((j == 0) or (j == i - 1)):
                    line += "#  "

                else:
                    line += "   "
                j += 1

            print(line)
            line = ""
            i -= 1
            n = height
            j = 0


    def parallelogram(self):
        side1 = int(input("\ninput the height of the parallelogram : "))
        side2 = int(input("input the length of the parallelogram : "))
        i = 0
        j = 0
        n = side1
        k = 0
        m = side1
        line = ""


        while (i < side1):
            while (n > 0):
                while (k < n):
                    line += "   "
                    k += 1
                n -= 1
            while (j < side2):
                if (i == 0) or (i == side1 - 1):
                    line += "#  "

                elif (j == 0) or (j == side2 - 1):
                    line += "#  "

                else:
                    line += "   "
                j += 1

            print(line)
            line = ""
            j = 0
            i += 1
            n = side1 - i
            k = 0

    def hexagon(self):
        side = int(input("\ninput the side of the hexagon : "))
        print("\n")
        i = 0
        j = side
        n = side
        if (side > 4):
            s = (side * 2) + (side - 4)
        elif (side < 4):
            s = (side * 2) - (4 - side)
        else:
            s = (side * 2)
        line = ""

        while (i < side):
            while (j > i):
                line += "   "
                j -= 1

            while (n > 0):
                if (i == 0):
                    line += "*  "

                elif (n == 1) or (n == (side) + (2 * i)):
                    line += "*  "

                else:
                    line += "   "
                n -= 1

            i += 1
            j = side
            n = (side) + (2 * i)
            print(line)
            line = ""

        for m in range(1, side):
            for h in range(0, m + 1):
                line += "   "

            for k in range(0, s):
                if (k == 0) or (k == s - 1):
                    line += "*  "

                elif (m == side - 1):
                    line += "*  "

                else:
                    line += "   "

            print(line)
            line = ""
            s -= 2

    def draw(self):
        print("\n1.Squres"  # let the user choose one of the shapes
              "\n2.Rectangles"
              "\n3.Circles"
              "\n4.Triangles"
              "\n5.Parallelograms"
              "\n6.Hexagons"
              "\n7.Back to main menu")

        while (True):

            category = int(input("Please select a shape : "))

            if (category == 1):
                draw2d.square(self)
                break

            elif (category == 2):
                draw2d.rectangle(self)
                break

            elif (category == 3):
                print("We are still working on it")
                break

            elif (category == 4):
                draw2d.triangle(self)
                break

            elif (category == 5):
                draw2d.parallelogram(self)
                break

            elif (category == 6):
                draw2d.hexagon(self)
                break

            elif (category == 7):
                execute.exe()
                break

            else:
                print("Please input a valid option.\n")


class execute:
    def exe(self):
        print("\n1.Calculate the area and the perimeter\n"
              "2.Draw 2D and 3D shapes\n"
              "3.Exit\n")

        while (True):  # check the input is an integer or not and loop until an integer is entered
            try:
                category = int(input("Please select a category:"))
                break
            except:
                print("Please input a number only")

        if (category == 1):
            calculate().cal()

        elif (category == 2):
            draw2d.draw(self)

        elif (category == 3):
            print("\nBye")
            exit(0)

        else:       # check if the entered value is valid and
            print("\nPlease input a valid option\n")
            execute.exe()


# execute the class in the main function
if __name__ == "__main__":
    execute = execute()
    execute.exe()
