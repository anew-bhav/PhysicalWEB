# Run the program  on terminal using 'python RunningMedian.py'#
number_input = input()# Take the number of input to be taken 
list = []#list for storing the values which are input

#loop runs until the limit is reached
#in every iteration a number is taken as input
#and appended to the list. After appending new number, the list is sorted in ascending order
#after sorting length of the list is calculated
#if the length is even then mean of two middle most values is printed
#else the middle most element in the list is printed
for i in range(number_input):
    number = input()
    list.append(number)
    list=sorted(list)
    length = len(list)
    if(length%2==0):
        print (list[(length/2)-1]+list[length/2])/float(2)

    else:
        print list[(length/2)]


