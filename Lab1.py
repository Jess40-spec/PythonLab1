import math

r = 5
a = math.pi * r**2
v = (4 / 3) * math.pi * r**3
a_side = 3
b_side = 4
c_side_sq = a_side**2 + b_side**2
pyt = math.sqrt(c_side_sq)
first_name = "Jessica"
last_name = "Griffith"
full_name = first_name + " " + last_name
name_len = len(full_name)

print(a, v, pyt, name_len, full_name, full_name.upper(), full_name.lower())

age = 24
weight = 190
height = 5.0
inches = 12 * height

print(type(age), type(weight), type(height))
bmi = (weight / inches**2) * 703
print(bmi)