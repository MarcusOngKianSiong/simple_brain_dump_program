# Make sure that initial input only contains 1,2,3, or 4
def get_correct_initial_input():
    
    user_input = 20
    
    while user_input not in [1,2,3,4]:
        try:
            user_input = int(input("What would you like to do?\n1. Append\n2. Delete item\n3. Clear all\n4. Exit program\nInput: """))
        except:
            print("\nInvalid input\n")
            continue
        else:
            if user_input not in [1,2,3,4]:
                print("\nInvalid input\n")
                continue
        
        return user_input

# Obtain new comment to append to the list from the user
def get_new_commet():
    new_comment = input("Write new comment: ")
    return new_comment

# Obtain the index of the comment to delete (INCOMPLETE!!!!! CHECK IF THE INDEX EXIST)
def comment_to_delete():
    
    index = input("comment's index: ")
    return index

# Organize the inputs into an array (e.g. [1,"something here"]) to be processed
def prepare_user_inputs():
    
    # Hold two 
    prepared_user_input = []
    
    prepared_user_input.append(get_correct_initial_input()) 
    
    if prepared_user_input[0] in [1,2]:
        
        # Deleting a single comment using it's index (2)
        if prepared_user_input[0] == 2:                          
            index_to_delete = comment_to_delete()                   
            print("Delete a single comment!!!!")
            
        # Appending new comment (1)    
        else:
            # Append value....
            new_comment = get_new_commet()
            prepared_user_input.append(new_comment)
            
    else:
        print("Unknown error")
        
    return prepared_user_input
        


