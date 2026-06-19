# two list one is mutable and other is immutable
#[] banana brackets, String values,
# When we want to store multiple values in a single variable we use list, it is mutable

fruits=["apple","banana","grapes"]
#pre defined function
fruits.extend(['orange','watermellon','pineapple'])
print(f" fruit list: {fruits}")
print(f"First food value is {fruits[:1]}")
print(f"Third food value is {fruits[-1]}")
# tuples=once declared we cannot change the values, it is immutable, Append is not possible, we cannot delete the values, we cannot change the values
colors=("red","blue","green")
print(f"Color list: {colors}")
print(f"Third color value is {colors[2]}")