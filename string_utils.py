def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


def split_at_first_digit(formula):
  digit_loction = 1
  for i in range(len(formula)):
    if formula[i].isdigit():
      digit_location = i
      break
  return(formula[0:digit_location], formula[digit_location:])

