number = input("Enter positive number [1,100]: ")

# If input not a number, raise a custom error
# If input is not positive, raise a custom error
# If input is not between 1 and 100, raise a custom error

class NotaNumberError(ValueError):
    pass
class NotPositiveNumberError(ValueError):
    pass
class NotWithingRangeError(ValueError):
    pass
user_input = input("Enter a number from [1,100]:")

if not user_input.isnumeric() and not user_input[1:].isnumeric():
    raise NotaNumberError()

number = int(user_input)
if number < 0:
    raise NotPositiveNumberError

if not (0<= number <=100):
    raise NotWithingRangeError()













