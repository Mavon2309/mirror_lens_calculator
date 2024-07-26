import time

print("Welcome, this will help you calculate the most important things about any mirror and lens calculation")
time.sleep(0.1)

while True:
    to_determine = input("Input one of the letters between f, u, v that you wish to determine: ")

    if to_determine == "f":
        print("Determining focal length.")
        time.sleep(0.1)
        print("Remember, concave mirrors have a negative focal length, while convex mirrors have a positive focal length and it's the other way for lenses.")
        time.sleep(0.1)
        u = float(input("Please input object distance (negative for the left of the mirror): "))
        v = float(input("Please input image distance: "))
        f = 1 / ((1 / v) + (1 / u))
        print("Calculating...")
        time.sleep(2)
        print("The focal length is: " + str(f) + "! Thanks for using this program!")
        extra = input("Do you have something else you want to calculate? (I can only understand a y for yes or n for no!)")
        if extra == "n": 
            print("Delightful, bye!")
            break
        print("Lets get to it then!")
    elif to_determine == "u":
        print("Determining object distance.")
        time.sleep(0.1)
        print("Remember, concave mirrors have a negative focal length, while convex mirrors have a positive focal length and it's the other way for lenses.")
        time.sleep(0.1)
        f = float(input("Please input focal length (negative for concave mirrors): "))
        v = float(input("Please input image distance: "))
        u = 1 / ((1 / f) - (1 / v))
        print("Calculating...")
        time.sleep(2)
        print("The object distance is: " + str(u) + "! Thanks for using this program!")
        extra = input("Do you have something else you want to calculate? (I can only understand a y for yes or n for no!)")
        if extra == "n": 
            print("Delightful, bye!")
            break
        print("Lets get to it then!")
    elif to_determine == "v":
        print("Determining image distance.")
        time.sleep(0.1)
        print("Remember, concave mirrors have a negative focal length, while convex mirrors have a positive focal length and it's the other way for lenses.")
        time.sleep(0.1)
        f = float(input("Please input focal length (negative for concave mirrors): "))
        u = float(input("Please input object distance: "))
        if u == f:
            print("No image will be formed!")
            break
        v = 1 / ((1 / f) - (1 / u))
        print("Calculating...")
        time.sleep(2)
        print("The image distance is: " + str(v) + "! Thanks for using this program!")
        extra = input("Do you have something else you want to calculate? (I can only understand a y for yes or n for no!)")
        if extra == "n": 
            print("Delightful, bye!")
            break
        print("Lets get to it then!")
    else:
        print("Invalid input! Only f, u, v are allowed. You can't put in " + to_determine + "!")
