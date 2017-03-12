
'''Implement a python class Queue which has a 'items' list to store the values that are put into the queue.
 The class has four methods namely put(),pop(),peek() and display().

 put(item):
     inserts the 'item' to the Queue
 pop():
     removes the element at the HEAD(start of the queue) of the queue
 peek():
     prints the element at the HEAD of the queue without removing the element
 display():
     prints the entire queue when called
     '''

'''
 The input format is as follows:
     when the script is executed, an input is to be done to initilise the number of test cases to be input.
     After that the user is expected to enter the desired commands to study the implementation of the QUEUE.
     The command syntax is as follows:
         <command> <argument>
         presently there are three commands 1(to put into the stack), 2(to pop from queue) , 3(to print HEAD of the queue)
         Command '1':
         Note: Only the command '1' accepts additional argument i.e. the element to be inserted into the queue
            usage:
                 1 42
                this will insert 42 into the queue
         Command '2','3','4':
            usage:
                2
            this pops the HEAD element of the queue
                3
            this print the HEAD element of the queue without removing it
                4
            this prints the entire queue

'''

class Queue:
    def __init__(self):#constructor for the class
        self.items = []
    def put(self,item):# put method for inserting element into the queue
        self.items.insert(0,item)
    def pop(self):# pop method for remove element at the HEAD(start of the queue)
        try:
            return self.items.pop()
        except:
            print "Queue is empty"
    def peek(self):# peek method for printing the element at the HEAD(start of the queue)
        try:
            return self.items[-1]
        except:
            pass
    def display(self):# prints the Queue
        print self.items

if __name__ =="__main__":
    q=Queue() # initialise the queue
    number = input()#input the number of iterations to be done
    for i in range(number):
        a = map(int,raw_input().strip().split(" "))#parse the input by the user into a list of integers
        ##----Checking the conditions for the command based upon the input from the user-----##
        if (a[0]==1):
            try:
                q.put(a[1])
            except:
                print "Enter valid command"
        elif (a[0]==2):
            q.pop()
        elif (a[0]==3):
            print q.peek()
        elif (a[0]==4):
            q.display()
