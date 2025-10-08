numbers = [1,2,3]
print("original list:",numbers)

ref = numbers
cp  = numbers.copy()

ref[0] = 99
cp[1] = 77

print("after changing ref and cp:")
print("numbers:",numbers)
print("ref:",ref)
print("cp:",cp)

