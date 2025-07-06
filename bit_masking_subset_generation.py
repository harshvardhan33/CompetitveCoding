# Generation of subsets
arr = [2,4,5]
subsets = []

# run for number of subsets time
for mask in range(1<<len(arr)):
    print("Mask : ",mask)
    subset = []
    for i in range(len(arr)):
        if (mask & (1<<i))!=0:
            subset.append(arr[i])
    subsets.append(subset)

print(subsets)