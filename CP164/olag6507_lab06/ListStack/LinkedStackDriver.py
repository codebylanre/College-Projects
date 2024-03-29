from LinkedStack import LinkedStack

if __name__=="__main__":
    
    S1=LinkedStack()
    
    # S1.push(12)
    # S1.push(20)
    # S1.push(33)
    # S1.push(49)
    # S1.push(33)
    # S1.push(31)
    # S1.push(49)
    for i in range(1,6):
        S1.push(i)
        print(i)
    print()
    print(f"The length is: {S1.len()}")
    
    print(f"The top is: {S1.top()}")
    print(S1.pop())
    print(S1.pop())
    print(S1.pop())
    print()
    print(f"The length is: {S1.len()}")
    print(S1.max())
    
    print()
    
    S2 = LinkedStack()
    for i in range(1, 11):
        S2.push(i)
        print(i)
    print()
    print(S2.max())
    # print(S2.max_stack())

        
    
    

