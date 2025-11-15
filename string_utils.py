def split_before_each_uppercases(formula):
    split_formula = []
    start = 0

    for i in range(1, len(formula)):
        if formula[i].isupper():
            end = i
            split_formula.append(formula[start:end])
            start = i

    split_formula.append(formula[start:])

    return split_formula


def split_at_first_digit(formula):
  digit_location = None
  for i in range(len(formula)):
    if formula[i].isdigit():
      digit_location = i 
      break
    
  if digit_location is None:
    return(formula,1)

  return(formula[:digit_location],int(formula[digit_location:]))
       
