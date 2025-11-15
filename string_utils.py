def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


def split_at_first_digit(formula):
  digit_location = None
  for i in range(len(formula)):
    if formula[i].isdigit():
      digit_location = i 
      break
    
  if digit_location is None:
    return(formula,1)

  return(formula[:digit_location],int(formula[digit_location:]))
       
