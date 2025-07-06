fruits = ["apple","banana","orange","lichi"]

# How we can represent using arrays
arr1 = ["banana","orange","lichi"]
arr2 = ["apple","banana","orange","lichi"]
arr3 = ["banana","lichi"]
fruit_arrays = [arr1,arr2,arr3]

# How do we represent using bit mask 
num_bits = len(fruits)
bit_mask = 0b0000
dc_set_bit = {}

for f in range(len(fruits)):
    dc_set_bit[fruits[f]]=len(fruits)-1-f

dc_set_bit_reverse = {value: key for key, value in dc_set_bit.items()}

print(dc_set_bit)
# Represent individual arrays as bit masks and find intersection as well
intersection_bits = 0b1111
for arr in fruit_arrays:
    print("-----------------------")
    fruit_bit_array = "0000"
    for fruit in arr:
        fruit_bit_array = b_obj.set_bit(fruit_bit_array,dc_set_bit[fruit])
    print(f"Bit Set for array : {arr} ",fruit_bit_array)

    # Intersection result 
    intersection_bits = int(fruit_bit_array,2) & intersection_bits

intersection_bits = bin(intersection_bits)[2:]
print("Final Intersection Array : ",intersection_bits)

for i in range(len(intersection_bits)):
    if intersection_bits[i]==str(1):
        print(dc_set_bit_reverse[i])