import numpy as np

arr = np.array([2, 5, 9, 14])

difference = np.diff(arr)

print(f"\nOriginal array: {arr}")

print(f"Differences: {difference}\n")

arr1 = np.array([4, 8, 12])
arr2 = np.array([6, 9, 15])

lcm = np.lcm.reduce(arr1)
gcd = np.gcd.reduce(arr2)

print(f"Array A: {arr1}")
print(f"LCM of Array A: {lcm}\n")

print(f"Array B: {arr2}")
print(f"GCD of Array B: {gcd}\n")

deg_val = np.array([0, 90, 360])

rad_val = np.deg2rad(deg_val)

print(f"Angles (radians): {rad_val}")

sin = np.sin(rad_val)
cos = np.cos(rad_val)
tan = np.tan(rad_val)

print(f"Sin: {sin}")
print(f"Cos: {cos}")
print(f"Tan: {tan}\n")

sin = np.sinh(rad_val)
cos = np.cosh(rad_val)
tan = np.tanh(rad_val)

print(f"Sinh: {sin}")
print(f"Cosh: {cos}")
print(f"Tanh: {tan}\n")

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

uni = np.union1d(set1, set2)
print(f"Union: {uni}")

inter = np.intersect1d(set1, set2)
print(f"Intersection: {inter} ")

diff = np.setdiff1d(set1, set2)
print(f"Difference (A - B): {diff}")
