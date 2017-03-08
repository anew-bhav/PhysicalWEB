
number_input = input()
list = []

for i in range(number_input):
    number = input()
    list.append(number)
    list=sorted(list)
    length = len(list)
    if(length%2==0):
        print (list[(length/2)-1]+list[length/2])/float(2)

    else:
        print list[(length/2)]


