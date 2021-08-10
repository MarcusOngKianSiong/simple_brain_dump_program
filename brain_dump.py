import json
# TOOLS TO GATHER INPUTS
# Make sure that initial input only contains 1,2,3, or 4
def get_correct_initial_input(memory):
    user_input = 20
    while user_input not in [1,2,3,4]:
        try:
            user_input = int(input("What would you like to do?\n1. Append\n2. Delete item\n3. Clear all\n4. Exit program\nInput: """))
            if (user_input == 2 or user_input == 3) and memory.number_of_comments() == 0:
                print("\n----------Error: Zero comments----------\n")
                continue
        except:
            print("\n----------Error: Invalid input----------\n")
            continue
        else:
            if user_input not in [1,2,3,4]:
                print("\n----------Error: Invalid input----------\n")
                continue
            
            

        return user_input

# Obtain new comment to append to the list from the user
def get_new_commet():
    new_comment = input("Write new comment: ")
    return new_comment

# Obtain the existing index of the comment to delete  (INCOMPLETE!!!!! CHECK IF THE INDEX EXIST)
def comment_to_delete(processing_object):

    while True:
        # ADDITIONAL CONSIDERATION: ANY INPUT THAT IS NOT A NUMBER -> SOLUTION: USE TRY EXCEPT ELSE BLOCK AS ANY INPUT THAT IS NOT A NUMBER WILL GIVE AN ERROR DUE TO int()
        try:
            index = int(input("comment's index: "))
        except:
            print("\n----------Error: Invalid input----------\n")
        else:
            if processing_object.existence_of_comment_by_Index(index):
                return index
            else:
                print("\n----------Error: Index does not exist. Please try again.----------\n")

# Organize the inputs into an array (e.g. [1,"something here"]) to be processed
def prepare_user_inputs(memory):

    # Hold two 
    prepared_user_input = []

    prepared_user_input.append(get_correct_initial_input(memory)) 

    if prepared_user_input[0] in [1,2]:

        # Deleting a single comment using it's index (2)
        if prepared_user_input[0] == 2:
                     
            index_to_delete = comment_to_delete(memory)                   
            prepared_user_input.append(index_to_delete)

        # Appending new comment (1)    
        else:
            # Append value....
            new_comment = get_new_commet()
            prepared_user_input.append(new_comment)

    return prepared_user_input

# TOOLS TO PROCESS INPUTS
class processing:
    def __init__(self,user_inputs):
        self.user_inputs = user_inputs

# Functions that represents processing of user inputs

    def append(self):
        
        if self.user_inputs[0] == 1:
            comments = []
            with open("storage.json",'r') as file:
                comments = json.load(file)

            with open("storage.json",'w') as file:
                comments.append(self.user_inputs[1])
                json.dump(comments,file)
            
            return True
        else:
            return False

    def remove_a_comment(self):
        if self.user_inputs[0] == 2:
            
            comments = []
            with open("storage.json","r") as file:
                comments = json.load(file)
            
            del comments[self.user_inputs[1]-1]
            
            with open("storage.json","w") as file:
                json.dump(comments,file)

            return True
        else:
            return False

    def delete_all(self):
        if self.user_inputs[0] == 3:

            comments = []
            with open("storage.json","r") as file:
                comments = json.load(file)

            comments.clear()

            with open("storage.json","w") as file:
                json.dump(comments,file)

            return True

        else:

            return False

    def exit_program(self):
        if self.user_inputs[0] == 4:
            exit()

# Functions that assist in operations

    def number_of_comments(self):
        with open("storage.json",'r') as file:
            comments = json.load(file)
            return len(comments)

    def existence_of_comment_by_Index(self,index):

        try:
            comments = []

            with open("storage.json",'r') as file:
                comments = json.load(file)

            comments[index-1]

        except:
            return False
        else:
            return True

    def display_comments(self):
        with open("storage.json") as file:
            comments = json.load(file)
            print("\n-----------------Comments---------------------")
            for index,comment in enumerate(comments):
                print(f"{index+1}: {comment}")
            print("----------------------------------------------\n")

memory = processing([])
while True:
    memory.display_comments()
    memory.user_inputs = prepare_user_inputs(memory)
    if memory.user_inputs[0] == 4:
        memory.exit_program()
    elif memory.user_inputs[0] == 3:
        memory.delete_all()
    elif memory.user_inputs[0] == 2:
        memory.remove_a_comment()
    elif memory.user_inputs[0] == 1:
        memory.append()