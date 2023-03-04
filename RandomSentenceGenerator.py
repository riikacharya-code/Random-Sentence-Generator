from random import random
import sys

# My sources:
# https://blog.finxter.com/how-to-execute-a-file-with-arguments-in-python/#:~:text=In%20summary%2C%20the%20steps%20to%20execute%20a%20file,pass%20it%20the%20argument%20list%20as%20a%20parameter
# https://www.tutorialkart.com/python/python-read-file-as-string/#:~:text=Python%20%E2%80%93%20Read%20File%20as%20String%201%20Open,calling%20close%20%28%29%20method%20on%20the%20file%20object.
# https://www.askpython.com/python/string/remove-character-from-string-python
# https://www.pythonpool.com/python-remove-newline-from-list/

if len(sys.argv) != 2:
    print("Usage: %s -f" % sys.argv[0])
    exit()

# function for replacing non-terminal with terminal
def go_to_next_non_terminal(non_terminal):
    
    new_random_string = ""
    
    j = 0
    
    for line in data:
        
        # finds out the starting non-terminal and matches it with the one entered.
        before_start = line[0: line.index('->')]
        if non_terminal in before_start:
            
            # finds whatever is after the starting non_terminal
            new_after_start = line[line.index('->') + 3: len(line)]
            
            # splits it into three choices to be chosen at random
            choices = new_after_start.split(' | ')
            
            random_choice_index = int(random() * len(choices))
            random_choice_string = choices[random_choice_index] + " "

            # for each non-terminal in random_choice_string, puts it through function again
            while j < len(random_choice_string):
            
                if random_choice_string[j] == '<':
                    random_choice_string = random_choice_string.replace('<', '', 1)
                    new_non_terminal = random_choice_string[j:after_start.index('>')]
                    
                    new_random_string += go_to_next_non_terminal(new_non_terminal)
                    
                    j = random_choice_string.index('>')
                    random_choice_string = random_choice_string.replace('>', '', 1)
                    
                else:
                    new_random_string += random_choice_string[j]
                    
                j += 1
        else:
            pass
    
    # returns terminal string to replace non-terminal that was passed in
    return new_random_string



random_string = ""

cfg = open(sys.argv[1], "r") 

data = []

# filters out all the comments in the txt and gets rid of '\n' characters
for line in cfg.readlines():
    if (line[0] != '#') and (line.rstrip() != ''):
        data.append(line.rstrip())
    

# gets the string after the start non-terminal
after_start = data[0][data[0].index('->') + 3: len(data[0])]

i = 0

# loops through after_start looking for non-terminals
while i < len(after_start):

    # if it finds non-terminal, puts it through function and gets rid of '<' and '>'
    if after_start[i] == '<':
        after_start = after_start.replace('<', '', 1)
        non_terminal = after_start[i:after_start.index('>')]

        random_string += go_to_next_non_terminal(non_terminal)
        
        i = after_start.index('>')
        after_start = after_start.replace('>', '', 1)

    else:
        random_string += after_start[i]
        
    i += 1

# prints randomly generated string
print(random_string)




