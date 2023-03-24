import math
import time

# menu = the main menu that the user chooses as the program is required to loop based on what the user chooses
menu = 0

# declare the functions for all the area and perimeter calculations
def square(side):       # the functio that will calculate the area and the perimeter of the square
    area = side * side
    perimeter = side * 4

    if (menu == 3):     # if this is for compound shapes, don't print but return
        return [area, perimeter]

    else:
        print("Area is", round(area, 3), "cm^2")
        print("Perimeter is", perimeter, "cm")


def rectangle(side1, side2):        # the functio that will calculate the area and the perimeter of the rectangle
    area = side1 * side2
    perimeter = (side1 * 2) + (side2 * 2)

    if (menu == 3):
        return [area, perimeter]

    else:
        print("Area is", round(area, 3), "cm^2")
        print("Perimeter is", perimeter, "cm")

def circle(radius):     # the functio that will calculate the area and the perimeter of the circle
    area = math.pi * radius * radius
    perimeter = 2 * math.pi * radius

    if (menu == 3):
        return [area, perimeter]

    else:
        print("Area is", round(area, 3), "cm^2")
        print("Perimeter is", perimeter, "cm")

def equilateralTriangle(side):      # the functio that will calculate the area and the perimeter of the equilateral triangle
    area = 0.25 * (math.sqrt(side * 3)) * (math.sqrt(side)) * (math.sqrt(side)) * (math.sqrt(side))
    perimeter = side * 3

    if (menu == 3):
        return [area, perimeter]

    else:
        print("Area is", round(area, 3), "cm^2")
        print("Perimeter is", perimeter, "cm")

def isoscelesTriangle(side1And2, side3):        # the function that will calculate the area and the perimeter of the iscoceles triangle
    side1, side2 = side1And2, side1And2

    area = 0.25 * (math.sqrt(side1 + side2 + side3)) \
           * (math.sqrt(side1 + side2 - side3)) \
           * (math.sqrt(side1 - side2 + side3)) \
           * (math.sqrt(-side1 + side2 + side3))
    perimeter = side1 + side2 + side3

    if (menu == 3):
        return [area, perimeter]

    else:
        print("Area is", round(area, 3), "cm^2")
        print("Perimeter is", perimeter, "cm")


def rightTriangle(side1, side2, side3):     # the functio that will calculate the area and the perimeter of the right triangle

    area = 0.25 * (math.sqrt(side1 + side2 + side3)) \
           * (math.sqrt(side1 + side2 - side3)) \
           * (math.sqrt(side1 - side2 + side3)) \
           * (math.sqrt(-side1 + side2 + side3))

    perimeter = side1 + side2 + side3

    if (menu == 3):
        return [area, perimeter]

    else:
        print("Area is", round(area, 3), "cm^2")
        print("Perimeter is", perimeter, "cm")


def normalTriangle(side1, side2, side3):        # the functio that will calculate the area and the perimeter of the normal triangle
    area = 0.25 * (math.sqrt(side1 + side2 + side3)) \
               * (math.sqrt(side1 + side2 - side3)) \
               * (math.sqrt(side1 - side2 + side3)) \
               * (math.sqrt(-side1 + side2 + side3))

    perimeter = side1 + side2 + side3

    if (menu == 3):
        return [area, perimeter]

    else:
        print("Area is", round(area, 3), "cm^2")
        print("Perimeter is", perimeter, "cm")

def parallelogram(side1, side2, angle):     # the functio that will calculate the area and the perimeter of the parallelogram
    area = side1 * side2 * math.sin(math.radians(angle))
    perimeter = (side1 * 2) + (side2 * 2)

    if (menu == 3):
        return [area, perimeter]

    else:
        print("Area is", round(area, 3), "cm^2")
        print("Perimeter is", perimeter, "cm")

def hexagon(side):      # the functio that will calculate the area and the perimeter of the hexagon
    area = 3 * (math.sqrt(3)) * side * side / 2
    perimeter = side * 6

    if (menu == 3):
        return [area, perimeter]

    else:
        print("Area is", round(area, 3), "cm^2")
        print("Perimeter is", perimeter, "cm")

def squareCube(side):
    area = 6 * side * side
    volume = side * side * side

    print("The surface area of the cube is", round(area, 3), "cm^2")
    print("The volume of the cube is", round(volume, 3), "cm^3")

def rectangleCube(length, height, thickness):
    area = (2 * length * height) + (2 * height * thickness) + (2 * length * thickness)
    volume = length * height * thickness

    print("The surface area of the cube is", round(area, 3), "cm^2")
    print("The volume of the cube is", round(volume, 3), "cm^3")

def sphere(raduis):
    area = 4 * math.pi * raduis * raduis
    volume = 4 / 3 *  math.pi * raduis * raduis * raduis

    print("The surface area of the sphere is", round(area, 3), "cm^2")
    print("The volume of the sphere is", round(volume, 3), "cm^3")

def cylinder(radius, height):
    area = (2 * math.pi * radius * radius) + (2 * math.pi * radius * height)
    volume = math.pi * radius * radius * height

    print("The surface area of the cylinder is", round(area, 3), "cm^2")
    print("The volume of the cylinder is", round(volume, 3), "cm^3")

def pyramid(base, height, one_face_length):
    area = (2 * base * one_face_length) + (base * base)
    volume = 1 / 3 * base * base * height

    print("The surface area of the pyramid is", round(area, 3), "cm^2")
    print("The volume of the pyramid is", round(volume, 3), "cm^3")


# the class that will perform all the main non-math things
class calculate:

    def cal2d(self):
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
                    if (menu == 3):     # if what user wants to do is compound shapes
                        return square(side)  # call the function to calculate the area and the perimeter and return them

                    else:
                        square(side)        # else just print
                        calculate.cal2d(self)  # recursion
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
                    if (menu == 3):
                        return rectangle(side1, side2)

                    else:
                        rectangle(side1, side2)
                        calculate.cal2d(self)
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
                    if (menu == 3):
                        return circle(radius)

                    else:
                        circle(radius)
                        calculate.cal2d(self)
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
                        if (menu == 3):
                            return equilateralTriangle(side)

                        else:
                            equilateralTriangle(side)
                            calculate.cal2d(self)
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
                            if (menu == 3):
                                return isoscelesTriangle(side1And2, side3)

                            else:
                                isoscelesTriangle(side1And2, side3)
                                calculate.cal2d(self)
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

                            if (menu == 3):
                                return rightTriangle(side1, side2, side3)

                            else:
                                rightTriangle(side1, side2, side3)
                                calculate.cal2d(self)  # if yes, calculate the area and the perimeter
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
                            if (menu == 3):
                                return normalTriangle(side1, side2, side3) # if yes, calculate the area and the perimeter

                            else:
                                normalTriangle(side1, side2, side3)
                                calculate.cal2d(self)
                                break       # loop until the three sides make up a valid triangle
                        else:
                            print("\nThe three sides you entered do not make up a valid triangle.\nPlease try again.") # if not, ask the user to input again

                    else:
                        print("\nPlease input positive values only.")

            elif (type == 5):
                print("\n")         # for some separation
                calculate.cal2d(self)

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
                        if (menu == 3):
                            return parallelogram(side1, side2, angle)

                        else:
                            parallelogram(side1, side2, angle)
                            calculate.cal2d(self)
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
                    if (menu == 3):
                        return hexagon(side)

                    else:
                        hexagon(side)
                        calculate.cal2d(self)
                        break
                else:
                    print("\nPlease input positive values only")

        elif (category == 7):
            print("\nGoing back to main menu\n")
            time.sleep(1)
            execute.exe()

        else:
            print("\nPlease input a valid option")
            calculate.cal2d(self)

    def cal3d(self):
        print("1. Square Cube\n"
              "2. Rectangle Cube\n"
              "3. Sphere\n"
              "4. Cylinder\n"
              "5. Pyramid\n"
              "6. Back to main menu.\n")

        while (True):
            try:
                category = int(input("Please choose a shape: "))
                break

            except:
                print("Please input a number only\n")

        if (category == 1):
            while(True):
                while(True):
                    try:
                        side = float(input("Input the side of the square cube: "))
                        break

                    except:
                        print("Please input a number only.\n")

                if (side > 0):
                    squareCube(side)
                    break

                else:
                    print("The value(s) cannot be negative.\n")


        elif (category == 2):
            while (True):
                while (True):
                    try:
                        length = float(input("Input the length of the rectangle cube: "))
                        height = float(input("Input the height of the rectangle cube: "))
                        thickness = float(input("Input the thickness of the rectangle cube: "))
                        break

                    except:
                        print("Please input a number only.\n")

                if (length > 0 and height > 0 and thickness > 0):
                    rectangleCube(length, height, thickness)
                    break

                else:
                    print("The value(s) cannot be negative.\n")

        elif (category == 3):
            while (True):
                while (True):
                    try:
                        radius = float(input("Input the radius of the sphere: "))
                        break

                    except:
                        print("Please input a number only.\n")

                if (radius > 0):
                    sphere(radius)
                    break

                else:
                    print("The value(s) cannot be negative.\n")

        elif (category == 4):
            while (True):
                while (True):
                    try:
                        radius = float(input("Input the radius of the cylinder: "))
                        height = float(input("Input the height of the cylinder: "))
                        break

                    except:
                        print("Please input a number only.\n")

                if (radius > 0 and height > 0):
                    cylinder(radius, height)
                    break

                else:
                    print("The value(s) cannot be negative.\n")

        elif (category == 5):
            while (True):
                while (True):
                    try:
                        base = float(input("Input the base of the pyramid: "))
                        height = float(input("Input the height of the pyramid: "))
                        one_face_length = float(input("Input the length of one face of the pyramid: "))
                        break

                    except:
                        print("Please input a number only.\n")

                if (base > 0 and height > 0 and one_face_length > 0):
                    pyramid(base, height, one_face_length)
                    break

                else:
                    print("The value(s) cannot be negative.\n")

        elif (category == 6):
            print("Going back to main menu.....")
            time.sleep(1)
            execute.exe()

        else:
            print("Please input a valid number.\n")
            calculate.cal3d(self)

class draw():     # the class that will perform the drawing of shapes

    def rectangle(self):        # the function that will draw a rectangle
        try:
            side1 = int(input("\ninput the height of the rectangle : "))
            side2 = int(input("input the length of the rectangle : "))
            print("\n")

            if (side1 > 0 and side2 > 0):
                i = 0
                n = 0
                line = ""
                while (i < side1):      # loop through the height
                    while (n < side2):      # loop through the length
                        if ((i == 0) or (i == side1 - 1)):      # if they are the first or the last line
                            line += "*  "       # fill the line with *s

                        elif ((n == 0) or (n == side2 - 1)):
                            line += "*  "       # add * to the first or the last row of the lines other than the first and the last

                        else:
                            line += "   "       # fill the middle part with white space
                        n += 1      # increment the length
                    n = 0   # reset the length so that it can run again
                    i += 1      # increment the height
                    print(line)     # print the line
                    line = ""       # reset the line

            else:
                print("Pleaase input positive values")
                draw.rectangle(self)

        except:
            print("Please input an integer number only")
            draw.rectangle(self)



    def square(self):       # the function that will draw a square
        try:
            side = int(input("\ninput the side of the square : "))
            print("\n")
            if (side > 0):
                i = 0
                n = 0
                line = ""
                while (i < side):       # first loop through the height
                    while (n < side):       # loop through the length
                        if ((i == 0) or (i == side - 1)):           # if they are the first and the last line
                            line += "*  "       # fill the line with *s

                        elif ((n == 0) or (n == side - 1)):     # if they are the first and the last column of other lines
                            line += "*  "       # add the * to the first or the last column of the shape

                        else:
                            line += "   "       # use only white spaces for the middle part of the other lines

                        n += 1      # increment the length
                    n = 0       # after exiting the length loop, reset the value of n to 0 so that it can restart
                    i += 1      # increment the height
                    print(line)     # print out the line
                    line = ""       # reset the line

            else:
                print("Please input a positive value.\n")
                draw.square(self)

        except:
            print("Please input an integer number only.")
            draw.square(self)




    def triangle(self):     # the function that will draw a triangle
        try:
            height = int(input("\ninput the height of the triangle : "))
            print("\n")

            if (height > 0):
                i = height
                n = height
                j = 0
                line = ""


                while (i > 0):      # loop through the height
                    # for the white space in front of each row
                    # this loop's looping times will increase each time the mother loop is done
                    while (n > i):
                        line += "   "
                        n -= 1

                    # for the #s that will make up the triangle
                    # this loop's looping times will decrease each time the mother loop is done
                    while (j < i):
                        if (i == height):       # if it is the first line, fill the line with #s
                            line += "#  "

                        elif ((j == 0) or (j == i - 1)):        # if not, fill only the first and the last column with #s
                            line += "#  "

                        else:       # fill the middle parts with white space
                            line += "   "
                        j += 1

                    print(line)     # print the line
                    line = ""       # reset
                    i -= 1      # minus one from height
                    n = height      # reset n so that it can loop again
                    j = 0       # reset j so that it can loop again

            else:
                print("Please input a positive value.")
                draw.triangle(self)

        except:
            print("Please input a number only.")
            draw.triangle(self)

    def parallelogram(self):        # the function that will draw a parallelogram
        try:
            side1 = int(input("\ninput the height of the parallelogram : "))
            side2 = int(input("input the length of the parallelogram : "))

            if (side1 > 0 and side2 > 0):
                i = 0
                j = 0
                n = side1
                k = 0
                m = side1
                line = ""

                while (i < side1):      # loop through the height
                    # for the white spaces in front of each row
                    # this loop's looping times will decrease each time the mother loop is done
                    while (n > 0):
                        while (k < n):
                            line += "   "
                            k += 1
                        n -= 1

                    # for the #s that will make up the shape
                    while (j < side2):
                        if (i == 0) or (i == side1 - 1):        # fill the first and the last row with #s
                            line += "#  "

                        elif (j == 0) or (j == side2 - 1):      # fill the first and last column of other rows
                            line += "#  "

                        else:
                            line += "   "       # fill the middle parts with white spaces
                        j += 1

                    print(line)
                    line = ""       # reset the variables so that the loop can go again
                    j = 0
                    i += 1
                    n = side1 - i       # white spaces in front of each row needs to decrease with each row
                    k = 0
            else:
                print("Please input a positive value.")
                draw.parallelogram(self)

        except:
            print("Please input an integer number only.\n")
            draw.parallelogram(self)

    # I copied this directly so I cannot explain what this does
    def circle(self):       # the function that will draw the hexagon
        try:
            diameter = int(input("Enter the diameter of the circle : "))
            if (diameter > 0):
                radius = diameter / 2 - .5
                r = (radius + .25) ** 2 + 1
                r_min = (radius - 1) ** 2 + 1

                result = ''

                for i in range(diameter):
                    y = (i - radius) ** 2
                    for j in range(diameter):
                        x = (j - radius) ** 2
                        if r_min <= x + y <= r:
                            result = result + '*  '
                        else:
                            result = result + '   '
                    result = result + '\n'

                print(result)

            else:
                print("Please input a positive value.")
                draw.circle(self)

        except:
            print("Please input an integer number only.\n")
            draw.circle(self)



    def hexagon(self):      # the function that will draw a hexagon
        try:
            side = int(input("\ninput the side of the hexagon : "))
            print("\n")


            # even though I did this myself, even I don't understand this anymore.
            # it was a spurt of a moment and somehow a hexagon is produced.
            if (side > 0):
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

            else:
                print("Please input a positive value.")

        except:
            print("Please input an integer number only.")
            draw.hexagon(self)

    def draw2d(self):     # the function that will call all the drawing functions
        print("\n1.Squares"  # let the user choose one of the shapes
              "\n2.Rectangles"
              "\n3.Circles"
              "\n4.Triangles"
              "\n5.Parallelograms"
              "\n6.Hexagons"
              "\n7.Back to main menu")

        while (True):

            category = int(input("Please select a shape : "))

            if (category == 1):
                draw.square(self)
                break

            elif (category == 2):
                draw.rectangle(self)
                break

            elif (category == 3):
                draw.circle(self)
                break

            elif (category == 4):
                draw.triangle(self)
                break

            elif (category == 5):
                draw.parallelogram(self)
                break

            elif (category == 6):
                draw.hexagon(self)
                break

            elif (category == 7):
                execute.exe()
                break

            else:
                print("Please input a valid option.\n")

    def cube(self):
        try:
            a = int(input("Enter the length : "))

            if (a > 0):
                h = a * 2
                j = d = int(h / 4)
                q, e, u, p, k = "| \n+/"
                w = e * d
                s = p + '-' * h + p
                i = ''
                o = e + w + s + u
                v = q + e * h + q
                while j: o += e * j + k + e * h + k + e * (d - j) + q + u;j -= 1;i += v + e * j + k + u
                print(o + s + w + q + u + (v + w + q + u) * (d - 1) + v + w + p + u + i + s)

            else:
                print("Please input a positive number.\n")
                draw.cube(self)


        except:
            print("Please input an integer number only.\n")
            draw.cube(self)


    def draw3d(self):

        print("1. Cube\n"
              "2. Cylinder\n"
              "3. Pyramid.\n"
              "4. Return to main menu.\n")

        while (True):
            while (True):
                try:
                    category = int(input("Please select a shape: "))
                    break

                except:
                    print("Please input a number only.\n")

            if (category == 1):
                draw.cube(self)
                break

            elif (category == 2):
                print("Sorry this shape is currently not available.\n Please select another one.\n")

            elif (category == 3):
                print("Sorry this shape is currently not available.\n Please select another one.\n")

            elif (category == 4):
                execute.exe()
                break

            else:
                print("Please input a valid option.\n")

class compound():
    def compound_calculate(self):       # the function that will perform the calculation of the compund shapes
        print("\nPleaes choose 2 shapes and we will calculate the total area and parameter for you.")
        total_area = 0
        total_parameter = 0

        while (True):
            try:
                for i in range(2):   # there will be only two times as it is only a two-compound
                    lst = calculate.cal2d(self)
                    for n in range(len(lst)):
                        if (n == 0):
                            total_area += lst[n]        # first one is the area
                        else:
                            total_parameter += lst[n]       # second one is the parameter


                print("\nThe total area for the two shapes is",round(total_area, 3), "cm^2"
                      "\nThe total parameter for the two shapes is",round(total_parameter, 3), "cm")
                break

            except:
                print("You have to choose both valid inputs.\nPlease try again.")

class execute:
    def exe(self):
        global menu
        print("\n1.Calculate the area and the perimeter of 2D shapes\n"
              "2.Draw 2D and 3D shapes\n"
              "3.Calculate the area and the perimeter of the compound shapes\n"
              "4.Calculate the area and the surface area of 3D shapes\n"
              "5.Exit\n")

        while (True):  # check the input is an integer or not and loop until an integer is entered
            try:
                menu = int(input("Please select a category:"))
                break
            except:
                print("Please input a number only")

        if (menu == 1):
            calculate().cal2d()

        elif (menu == 2):
            print("1. 2D shapes.\n"
                  "2. 3D shapes.\n")
            while (True):
                while (True):
                    try:
                        category = int(input("Please select a category: "))
                        break

                    except:
                        print("Please input a number only.\n")

                if (category == 1):
                    draw.draw2d(self)
                    break

                elif (category == 2):
                    draw.draw3d(self)
                    break

                else:
                    print("Please input a valid option.\n")

        elif (menu == 3):
            compound.compound_calculate(self)

        elif (menu == 4):
            calculate.cal3d(self)


        elif (menu == 5):
            print("\nBye")

        else:       # check if the entered value is valid and
            print("\nPlease input a valid option\n")
            execute.exe()


# execute the class in the main function
if __name__ == "__main__":
    execute = execute()
    execute.exe()
