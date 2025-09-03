'''Python Exception Handling handles errors that occur during the execution of a program.
Exception handling allows to respond the error, instead of crashing the running program.


n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Cant be divided by zero!")

try:
    n = 0
    res = 100/n
except ZeroDivisionError:
    print('You cant divide by zero')
except ValueError:
    print('Enter a Valid Number')
else:
    print('Result is:', res)
finally:
    print('Execution Completed')'''