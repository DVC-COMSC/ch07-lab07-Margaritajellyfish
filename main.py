
inputvalues = input('Enter all elements values: ')
numbers1 = inputvalues.split() 
for i in range(len(numbers1)):
	numbers1[i] = int(numbers1[i]) 
# The following line is the same as the for-loop
# numbers1 = list(map(int, numbers))

# print ("The original list: ", numbers1)

# ******************************
# Make your Code
# ******************************
evenlist = []
number = []
copy = numbers1
for j in range(len(copy)):
    x = numbers1.pop()
    if j % 2 == 0:
        number.append(x)
    else: 
        evenlist.append(x)
number.reverse()
evenlist.reverse()
print("The list numbers \n", number)
print("The list for even index elements \n", evenlist)
