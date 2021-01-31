#

error_handling = raw_input(" Would you like to run this program with input error handling? (y/n) ");                       #    asking user if they want error handling or no
while error_handling != 'y' and error_handling != 'n':
    error_handling = raw_input(" Please enter 'y' or 'n'. ");



input = raw_input("  Enter an integer! ");                                                                                  #   prompting year input

valid = 0;


if error_handling == "y":                                                                                                   #   simple error handling
    while valid == 0:
        if input.isdigit() == True:
            valid = 1;
            break;
        else:
            input = raw_input(" Invalid input. Please enter a positive integer ");





leap = True;


if int(input) % 4 == 0:                                                                                                     #   logic of the program checks if its a leap year 
        leap = True;
else:
    print(" " + str(input) + " is not a leap year.")
    exit();

if int(input) % 100 == 0:
    if input % 400 != 0:
        leap = False;



if leap == False:
    print(" " + str(input) + " is not a leap year.")
    exit();

else:
    print(" " + str(input) + " is a leap year!")
