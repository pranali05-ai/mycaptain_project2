# Python program to print all positive Numbers in a range

#note : I'm using two different codes for two different list

#1] list of numbers using for loop
list1 = [12, -7, 5, 64,-14]

# iterating each number in list
for num in list1:
	
# checking condition
    if num >= 0:
       print(num,end = " "):

    

#2] list of numbers
list2 = [12, 14, -95, 3]
num = 0

# using while loop	
while(num < len(list2)):
	
	# checking condition
	if list2[num] >= 0:
	   print(list2[num], end = " ")
	
	# increment num
	num += 1

	
