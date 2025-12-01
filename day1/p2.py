start_pos = 50
instruct = ''
zero_counter = 0


curr_pos = start_pos

with open('input1.txt', 'r') as file:
    for line in file:
        instruct = line.strip()
        if instruct[0].lower() == 'l':
            rotations = int(instruct[1:])
            for i in range(rotations): # i am well aware this is a monkey way of doing it but gotta study for exams too
                curr_pos = curr_pos - 1
                if curr_pos < 0: # tryna say if dial is turned left past 0:
                    curr_pos = curr_pos % 100
                if curr_pos == 0: zero_counter += 1
        elif instruct[0].lower() == 'r':
            rotations = int(instruct[1:])
            for i in range(rotations):
                curr_pos = curr_pos + 1
                if curr_pos > 99: # tryna say if dial is turned right past 99:
                    curr_pos = curr_pos % 100
                if curr_pos == 0: zero_counter += 1
        
print('Secret code is: ', zero_counter)