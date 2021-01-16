#

print(" Enter an integer!");

input = input(" ");
leap = True;


if input % 4 == 0:
        leap = True;
else:
    print(" " + str(input) + " is not a leap year.")
    exit();

if input % 100 == 0:
    if input % 400 != 0:
        leap = False;



if leap == False:
    print(" " + str(input) + " is not a leap year.")
    exit();

else:
    print(" " + str(input) + " is a leap year!")
