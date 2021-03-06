'''
Create a program lets users store comments on it. 

Features: 
    1. List down what they have written
    2. Add things to the list
    3. Delete items from the list
    4. Delete everything from the list

What do I need:
    1. A file
    2. Memory
    3. Controls
    4. Display

'''


Step 1: Acquire all relevant inputs and perform the necessary checks on the inputs              - Checking of one value requires one to look into memory
Step 2: Create the class that processes the inputs from step 1 (processing all four initial inputs)                            
Step 3: Fix all additional consideration brought up in step 1
Step 4: Ensure that input gathering component is working perfectly: 
    - gathering the initial inputs, 
    - making sure incorrect inputs are processed, 
    - gathering additional inputs based on the initial inputs, 
    - and produce an output that is given to the processing component.
Step 5: Ensure changes are being implemented to the data (storage.json) such that it reflects the initial input.
Step 6: Step 6: Refine the display and correct errors
    Errors:
    - Delete item: If there is nothing there, then it will be stuck in a loop
        - Put the logic into the first initial input check.
    - Delete item: Input that is not a number
        - Put the logic into the comment_to_delete function.