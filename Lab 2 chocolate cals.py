#male
weight = input("What is your weight?")
weight = int(weight)
height = input("What is your height?")
height = int(height)
age = input("How old are you?")
age = int(age)
bmrm = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
chocolate = bmrm/214
print(chocolate, "chocolate bars")

#female

bmrf = 66 + (6.2 * weight) + (12.7 * height) - (4.7 * age)
chocolate = bmrf/214
print(chocolate, "chocolate bars")
