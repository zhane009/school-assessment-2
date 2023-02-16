import math
import os

# declare the functions for all the area and perimeter calculations
def square(side):
    area = side * side
    perimeter = side * 4

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm\n")

def rectangle(side1, side2):
    area = side1 * side2
    perimeter = (side1 * 2) + (side2 * 2)

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm\n")

def circle(radius):
    area = math.pi * radius * radius
    perimeter = 2 * math.pi * radius

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm\n")

def equilateralTriangle(side):
    area = 0.25 * (math.sqrt(side * 3)) * (math.sqrt(side)) * (math.sqrt(side)) * (math.sqrt(side))
    perimeter = side * 3

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm\n")

def isoscelesTriangle(side1And2, side3):
    side1, side2 = side1And2, side1And2

    area = 0.25 * (math.sqrt(side1 + side2 + side3)) \
           * (math.sqrt(side1 + side2 - side3)) \
           * (math.sqrt(side1 - side2 + side3)) \
           * (math.sqrt(-side1 + side2 + side3))
    perimeter = side1 + side2 + side3

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm\n")

def rightTriangle(side1, side2, side3):

    area = 0.25 * (math.sqrt(side1 + side2 + side3)) \
           * (math.sqrt(side1 + side2 - side3)) \
           * (math.sqrt(side1 - side2 + side3)) \
           * (math.sqrt(-side1 + side2 + side3))

    perimeter = side1 + side2 + side3

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm\n")

def normalTriangle(side1, side2, side3):
    area = 0.25 * (math.sqrt(side1 + side2 + side3)) \
               * (math.sqrt(side1 + side2 - side3)) \
               * (math.sqrt(side1 - side2 + side3)) \
               * (math.sqrt(-side1 + side2 + side3))

    perimeter = side1 + side2 + side3

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm\n")

def parallelogram(side1, side2, angle):
    area = side1 * side2 * math.sin(math.radians(angle))
    perimeter = (side1 * 2) + (side2 * 2)

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm\n")

def hexagon(len):
    area = 3 * (math.sqrt(3)) * len * len / 2
    perimeter = len * 6

    print("Area is", round(area, 3), "cm^2")
    print("Perimeter is", perimeter, "cm\n")

# the class that will perform all the main non-math things
class calculate:

    def cal(self):
        print("\n1.Squres"    # let the user choose one of the shapes
              "\n2.Rectangles"
              "\n3.Circles"
              "\n4.Triangles"
              "\n5.Parallelograms"
              "\n6.Hexagons"
              "\n7.Exit")

        while(True): # check the input is an integer or not and loop until an integer is entered
            try:
                category = int(input("Please select a shape:"))
                break
            except:
                print("Please input a number only")

        if (category == 1):
            side = float(input("\nInput the length of the side in cm : "))  # ask for user to input the value of the side

            square(side)  # call the function to calculate the area and the perimeter

            calculate.cal(self)  # recursion

        elif (category == 2):
            side1 = float(input("\nInput the length of the first side in cm : "))
            side2 = float(input("Input the length of the second side in cm : "))

            rectangle(side1, side2)

            calculate.cal(self)

        elif (category == 3):
            radius = float(input("\nInput the length of the radius in cm : "))

            circle(radius)

            calculate.cal(self)

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
                side = float(input("\nInput the length of the side in cm : "))
                equilateralTriangle(side)

                calculate.cal(self)

            elif (type == 2):

                while(True):
                    side1And2 = float(input("\nInput the length of the two equal sides in cm : "))
                    side3 = float(input("Input the length of the third side in cm : "))

                    side1, side2 = side1And2, side1And2
                    if (((side1 + side2) > side3)   # check if the triangle is valid or not
                            and ((side1 + side3) > side2)
                            and ((side2 + side3) > side1)):
                        isoscelesTriangle(side1And2, side3)
                        break       # loop until a valid triangle is entered

                    else:
                        print("Your three sides do not make up a valid triangle.\nPlease try again.")   # let the user try again if not valid
                calculate.cal(self)

            elif (type == 3):

                while (True):
                    side1 = float(input("\nInput the length of the first side in cm : "))
                    side2= float(input("Input the length of the second side in cm : "))
                    side3 = float(input("Input the length of the third side in cm : "))

                    if ((((side1 * side1) + (side2 * side2)) == (side3 * side3)) # cheak if the three sides satisfy the Pythagora's Theorem
                            or (((side1 * side1) + (side3 * side3)) == (side2 * side2))
                            or (((side3 * side3) + (side2 * side2)) == (side1 * side1))):
                        rightTriangle(side1, side2, side3) # if yes, calculate the area and the perimeter
                        break       # loop until the three sides make up a valid right triangle

                    else:
                        print("Your three sides do not make up a valid triangle.\nPlease try again.") # if not, ask the user to input again

                calculate.cal(self)

            elif (type == 4):

                while (True):
                    side1 = float(input("\nInput the length of the first side in cm : "))
                    side2 = float(input("Input the length of the second side in cm : "))
                    side3 = float(input("Input the length of the third side in cm : "))

                    if (((side1 + side2) > side3) # check if the three sides make up a valid triangle
                            and ((side1 + side3) > side2)
                            and ((side2 + side3) > side1)):
                        normalTriangle(side1, side2, side3) # if yes, calculate the area and the perimeter
                        break       # loop until the three sides make up a valid triangle

                    else:
                        print("The three sides you entered do not make up a valid triangle.\nPlease try again.") # if not, ask the user to input again

                calculate.cal(self)

            elif (type == 5):
                print("\n")         # for some separation
                calculate.cal(self)

        elif (category == 5):
            side1 = float(input("\nInput the length of the first side in cm : "))
            side2 = float(input("Input the length of the second side in cm : "))
            angle = float(input("Input the degree of the angle between the two sides : "))

            parallelogram(side1, side2, angle)

            calculate.cal(self)

        elif (category == 6):
            side = float(input("\nInput the length of the side in cm : "))

            hexagon(side)

            calculate.cal(self)

        elif (category == 7):
            print("\nBye\n")
            execute.exe()

        else:
            print("\nPlease input a valid option")
            calculate.cal(self)

class execute:
    def exe(self):
        print("1.Calculate the area and the perimeter\n"
              "2.Draw 3D shapes\n"
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
            print("\nWe are still working on it.\n")
            execute.exe()

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


