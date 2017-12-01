# Handle the exceptions thrown by the code below in try and except blocks.

def problem1_squareString():
    try:
        for i in ['a', 'b', 'c']:
            print i ** 2

    except:
        print "You can't square strings. Python does not rope."


def problem2_xyz():
    x = 5
    y = 0

    try:
        z = x/y

    except:
        print "You can't divide by zero."

    finally:
        print 'All done!'



def problem3_ask_squared():
    while True:
        try:
            n = input('Input an integer: ')

        except:
            print('An error occurred! Please try again: ')
            continue

        else:
            print("Correct! That's an integer!")
            break

        finally:
            'Finally block executed!'

    print ('Your integer squared equals:'), n**2



problem1_squareString()
problem2_xyz()
problem3_ask_squared()
