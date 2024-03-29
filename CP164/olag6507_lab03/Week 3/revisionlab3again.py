from ArrayStack import ArrayStack

def equals(stacks_int, stacks_int2):

    if (len(stacks_int) != len(stacks_int2)):
        return False
    while not stacks_int2.isEmpty():
        if (stacks_int.pop() != stacks_int2.pop()):
            return False
    return True
        
def pythonlist_to_stack(list, empty_stack):
    empty_stack = ArrayStack()

    for items in list:
        empty_stack.push(items)
    print(empty_stack.pop())
    return empty_stack

def append_stack(int_stack1, int_stack2):
    newstack = ArrayStack()


    while not int_stack1.isEmpty():
        newstack.push(int_stack1.pop())

    while not int_stack2.isEmpty():
        newstack.push(int_stack2.pop())

    # Reverse the order 

    reversedstack = ArrayStack()
    while not newstack.isEmpty():
        reversedstack.push(newstack.pop())




    return reversedstack

def stutter(stack_int):
    double_stack_int = ArrayStack()

    while not stack_int.isEmpty():
        content = stack_int.pop()

        double_stack_int.push(content)
        double_stack_int.push(content)
     
    # We have to reverse it to maintain prev order
    reversed_double_stack = ArrayStack()
    while not double_stack_int.isEmpty():
        reversed_double_stack.push(double_stack_int.pop())
    
    return reversed_double_stack
    

if __name__ == "__main__":
    def lol():
        stack_int  = ArrayStack()
        stack_int2 = ArrayStack()
        for i in range(5):
            stack_int.push(i)
        for i in range(5):
            stack_int2.push(i)

        result = equals(stack_int, stack_int2)
        print(result)

    def ptyhontooeasy():
        empty_stack = ArrayStack()
        list = [1, 2, "hello", 3]
        result = pythonlist_to_stack(list, empty_stack)
        print(result)

    def comecheckagain():
        """
        Write a method append_stack, that takes two integer stack as arguments and returns a third stack
        object. The method appends the content of second stack to the contents of the first stack in such a
        way that the content of first stack are at the top and second stack come after it. Test your method
        """

        int_stack1 = ArrayStack()
        int_stack2 = ArrayStack()

        for i in range(4):
            int_stack1.push(i)

        for i in range(4, 9):
            int_stack2.push(i)
        result = append_stack(int_stack1, int_stack2)
        print(result)

    def had_me_in_the_first_half():
        stack_int = ArrayStack()
        school = [3, 7, 1, 14, 9]
        for i in school:
            stack_int.push(i)

        result = stutter(stack_int)
        print(result)

comecheckagain()