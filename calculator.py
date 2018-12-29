import math

# Just makes sure the first block works right
calculator_mode = 3

# Asks user which mode they want
while calculator_mode == 3:
    print("Enter 'boolean' to run boolean equations")
    print("Enter 'basic' to use a basic caluculator")
    print("Enter 'scientific' to use a scientific calculator")
    print("Enter 'quit' to end the program")
    calculator_mode = input(": ")

    if calculator_mode == "quit":
        print("quitting...")
        break
    elif calculator_mode == "boolean":
        calculator_mode = 0
    elif calculator_mode == "basic":
        calculator_mode = 1
    elif calculator_mode == "scientific":
        calculator_mode = 2
    else:
        calculator_mode = 3
        print("Please type an acceptable input")

# Asks user what calculation mode they would like to use
while calculator_mode == 0:
    print("Options:")
    print("Enter 'and' to find if two value are the same")
    print("Enter 'not' to find if two values are not the same")
    print("Enter 'xor' to encrypt values via xor encryption")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    # Quits user
    if user_input == "quit":
        print("quitting...")
        break
    # Runs 'and' calculations
    elif user_input == "and":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
        except ValueError:
            print("Value error: Try again")
            continue
        try:
            if num1 == num2:
                print("True")
            else:
                print("False")
        except TypeError:
            print("Type error: Try again.")
            continue
    # Runs 'not' calculations
    elif user_input == "not":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
        except ValueError:
            print("Type error: Try again.")
            continue
        try:
            if num1 != num2:
                print("True")
            else:
                print("False")
        except ValueError:
            print("Type error: Try again.")
            continue
    # Runs 'xor' calculations
    elif user_input == "xor":
        try:
            plaintext = str(input("Enter plaintext: "))
            key = str(input("Enter key: "))
            code = [0, 0, 0, 0, 0, 0, 0, 0]
        except ValueError:
            continue
        try:
            if plaintext[0] != key[0]:
                code[0] = "1"
            else:
                code[0] = "0"

            if plaintext[1] != key[1]:
                code[1] = "1"
            else:
                code[1] = "0"

            if plaintext[2] != key[2]:
                code[2] = "1"
            else:
                code[2] = "0"

            if plaintext[3] != key[3]:
                code[3] = "1"
            else:
                code[3] = "0"

            if plaintext[4] != key[4]:
                code[4] = "1"
            else:
                code[4] = "0"

            if plaintext[5] != key[5]:
                code[5] = "1"
            else:
                code[5] = "0"

            if plaintext[6] != key[6]:
                code[6] = "1"
            else:
                code[6] = "0"

            if plaintext[7] != key[7]:
                code[7] = "1"
            else:
                code[7] = "0"
        except:
            print("Didn't work, try again")
            continue
        print("".join(code))
    else:
        print("unknown input")

# Asks user what calculation mode to use
while calculator_mode == 1:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    # Quits program
    if user_input == "quit":
        print("quitting...")
        break
    # Runs addition script
    elif user_input == "add":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
        except ValueError:
            print("Value error: Try again")
            continue
        result = str(num1 + num2)
        print("The answer is " + result)
    # Runs subtraction script
    elif user_input == "subtract":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
        except ValueError:
            print("Value error: Try again")
            continue
        result = str(num1 - num2)
        print("The answer is " + result)
    # Runs multiplication script
    elif user_input == "multiply":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
        except ValueError:
            print("Value error: Try again")
            continue
        result = str(num1 * num2)
        print("The answer is " + result)
    # Runs division script
    elif user_input == "divide":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
        except ValueError:
            print("Value error: Try again")
            continue
        try:
            result = str(num1 / num2)
            print("The answer is " + result)
        except ZeroDivisionError:
            print("Can't divide by zero: Try again")
            continue
    else:
        print("Unknown input")

# Asks what calculator mode to use
while calculator_mode == 2:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'exponent' to take a number to a power")
    print("Enter 'sqrt' to find the square root of a number")
    print("Enter 'absval' to find the absolute value of a number")
    print("Enter 'percent' to find a percentage")
    print("Enter 'ans' to work with your last result")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    # Quits program
    if user_input == "quit":
        print("quitting...")
        break
    # Runs addition script
    elif user_input == "add":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
        except ValueError:
            print("Value error: Try again")
            continue
        result = str(num1 + num2)
        ans = result
        print("The answer is " + result)
    # Runs subtraction script
    elif user_input == "subtract":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
        except ValueError:
            print("Value error: Try again")
            continue
        result = str(num1 - num2)
        ans = result
        print("The answer is " + result)
    # Runs multiplication script
    elif user_input == "multiply":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
        except ValueError:
            print("Value error: Try again")
            continue
        result = str(num1 * num2)
        ans = result
        print("The answer is " + result)
    # Runs division script
    elif user_input == "divide":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
        except ValueError:
            print("Value error: Try again")
            continue
        try:
            result = str(num1 / num2)
            ans = result
            print("The answer is " + result)
        except ZeroDivisionError:
            print("Can't divide by zero: Try again")
            continue
    # Finds a number to a given exponent
    elif user_input == "exponent":
        try:
            base = float(input("Enter a number: "))
            exponent = float(input("Enter the exponent: "))
        except ValueError:
            print("Value error: Try again")
            continue
        try:
            result = str(base ** exponent)
            ans = result
            print("The answer is " + result)
        except (ValueError, TypeError):
            print("Error: Try again")
    # Finds the square root of a given number
    elif user_input == "sqrt":
        try:
            square = float(input("Enter a number: "))
        except ValueError:
            print("Value error: Try again")
            continue
        try:
            result = str(math.sqrt(square))
            ans = result
            print("The answer is " + result)
        except (ValueError, TypeError):
            print("Error: Try again")
            continue
    # Finds the absolute value of a given number
    elif user_input == "absval":
        try:
            num = float(input("Enter a number: "))
        except ValueError:
            print("Value error: Try again")
            continue
        try:
            if num < 0:
                result = -num
            else:
                result = num
            ans = result
            print(result)
        except (ValueError, TypeError):
            print("Error: Try again")
    # Finds the percent of one number out of another
    elif user_input == "percent":
        try:
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))
        except ValueError:
            print("Value error: Try again")
            continue
        try:
            raw = numerator / denominator
            result = raw * 100
            ans = result
            print(result)
        except (ValueError, TypeError):
            print("Error: Try again")
            continue
    # replaces certain numbers with the 'ans' variable defined from earlier operations. Basically copied and pasted
    elif user_input == "ans":
        print("Options:")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'exponent' to take a number to a power")
        print("Enter 'sqrt' to find the square root of a number")
        print("Enter 'absval' to find the absolute value of a number")
        print("Enter 'percent' to find a percentage")
        print("Enter 'quit' to end the program")
        user_input = input(": ")

        # Quits program
        if user_input == "quit":
            print("quitting...")
            break
        # Runs addition script
        elif user_input == "add":
            try:
                num2 = float(input("Enter another number: "))
            except ValueError:
                print("Value error: Try again")
                continue
            result = str(float(ans) + num2)
            ans = result
            print("The answer is " + result)
        # Runs subtraction script
        elif user_input == "subtract":
            try:
                num2 = float(input("Enter another number: "))
            except ValueError:
                print("Value error: Try again")
                continue
            result = str(float(ans) - num2)
            ans = result
            print("The answer is " + result)
        # Runs multiplication script
        elif user_input == "multiply":
            try:
                num2 = float(input("Enter another number: "))
            except ValueError:
                print("Value error: Try again")
                continue
            result = str(float(ans) * num2)
            ans = result
            print("The answer is " + result)
        # Runs division script
        elif user_input == "divide":
            try:
                num2 = float(input("Enter another number: "))
            except ValueError:
                print("Value error: Try again")
                continue
            try:
                result = str(float(ans) / num2)
                ans = result
                print("The answer is " + result)
            except ZeroDivisionError:
                print("Can't divide by zero: Try again")
                continue
        # Finds 'ans' to a given power
        elif user_input == "exponent":
            try:
                exponent = float(input("Enter the exponent: "))
            except ValueError:
                print("Value error: Try again")
                continue
            try:
                result = str(float(ans) ** exponent)
                ans = result
                print("The answer is " + result)
            except (ValueError, TypeError):
                print("Error: Try again")
        # Finds the square root of 'ans'
        elif user_input == "sqrt":
            try:
                result = str(math.sqrt(float(ans)))
                ans = result
                print("The answer is " + result)
            except (ValueError, TypeError):
                print("Error: Try again")
                continue
        # Finds the absolute value of 'ans'
        elif user_input == "absval":
            try:
                if float(ans) < 0:
                    result = -ans
                else:
                    result = ans
                ans = result
                print(result)
            except (ValueError, TypeError):
                print("Error: Try again")
        # Finds the percentage of 'ans' out of a given total
        elif user_input == "percent":
            try:
                denominator = float(input("Enter the denominator: "))
            except ValueError:
                print("Value error: Try again")
                continue
            try:
                raw = float(ans) / denominator
                result = raw * 100
                ans = result
                print(result)
            except (ValueError, TypeError):
                print("Error: Try again")
                continue
    else:
        print("Unknown input")
         
