largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        num=int(num)
    except:
        print('Invalid input')
    else:
        if smallest==None and largest==None:
            smallest=num
            largest=num
        elif num<=smallest:
            smallest=num
        elif num>=largest:
            largest=num
        elif num == "done":
            print('Maximum is',largest)
            print('Minnimum is',smallest) 
        break    
    

    
   
