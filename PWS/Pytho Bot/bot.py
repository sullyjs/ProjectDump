import cmath

print("Welcome! I'm your personal assistant.\nOPTIONS:\n-Type 'calendar' to get a calendar display (without caps).\n-Type 'tables' to get a display of tables of numbers.(without caps.)\n-Type 'solve quadratic' to solve a quadratic equation.(without caps.)\n-Type 'solve' to solve a liear equation.(without caps.)")

while True:
     print("Type a command.")
     user_input = input(" :")
     if user_input == "calendar":
       try:
         from calendar import month
         yy = int(input("Enter the year in numbers: "))
         mm = int(input("Enter the month in numbers: "))
         if input == yy or mm:
           print(month(yy, mm) + "\nWhat would you like to do now?")
       except ValueError:
         print("You typed something we couldn't understand. Try again:\nCalendar or Tables?")
       except IndexError:
         print("You typed in a month that doesn't exist. Try Again:\n Calendar or Tables? ")
     elif user_input == "tables":
       try:
         num = int(input("What number table would you like to display?"))
         for i in range(1,10):
          print(num, "x", i, "=", num*i)
       except ValueError:
        print("You typed a value we couldn't understand. Please type in a normal number.\nCalendar or Tables?")
       except TypeError:
         print("TypeError. :/")
     elif user_input == "solve quadratic":
       try:
           print("Solve an ax^2 + bx + c = 0 equation!")
           a = int(input("Give an a: "))
           b = int(input("Give an b: "))
           c = int(input("Give an c: "))
            # calculate the discriminant
           d = (b**2) - (4*a*c)
            # find two solutions
           sol1 = (-b-cmath.sqrt(d))/(2*a)
           sol2 = (-b+cmath.sqrt(d))/(2*a)
           print('The solution are {0} and {1}'.format(sol1,sol2))
       except ValueError:
        print("You typed a value we couldn't understand. Please type in a normal number.\nCalendar or Tables?")
       except TypeError:
         print("TypeError. :/")
     elif user_input == "solve":
       try:
           print("Solve an ax+b= 0 equation!")
           a = int(input("Give an a: "))
           b = int(input("Give an b: "))
           x = b/a
           print('x = {0}'.format(x))
       except ValueError:
        print("You typed a value we couldn't understand. Please type in a normal number.\nCalendar or Tables?")
       except TypeError:
         print("TypeError. :/")
      
     else:
       print("You typed something that wasn't in the options, please try again.\nWhat do you want to do?")