def calculate(weight, height):
    bmi = (weight * 703) / (height * height)
    if bmi < 18.5:
      return 'Underweight'
    elif 18.5 <= bmi <= 24.9:
      return 'Normal'
    return None
