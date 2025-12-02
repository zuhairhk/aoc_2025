def invalid_ids(list_of_ids):
    list_of_ids = list_of_ids.split(',') # input parsing
    list_of_invalids, sum_of_invalids = [], 0 # empty list of ids
    for id_set in list_of_ids:
        ids = id_set.split('-')
        first_id, last_id = int(ids[0]), int(ids[1])
        for i in range(first_id, last_id+1):
            f_id_str = str(i) # monke
            curr_id_len = len(f_id_str)
            for seq_len in range(1, (curr_id_len//2) + 1):
                if curr_id_len % seq_len != 0:
                    continue # can only use values where string of ID can be split evenly
                sequence = f_id_str[0:seq_len]
                repeated_counter = curr_id_len // seq_len
                if (sequence*repeated_counter) == f_id_str:
                    list_of_invalids.append(i)
                    sum_of_invalids += i
                    break # so that it doesnt go into next check when this ones been satisfied
    #return(list_of_invalids, '\n',sum_of_invalids)
    return(sum(list_of_invalids))


with open('input.txt', 'r') as file:
    data_input = file.readlines()

result = invalid_ids(data_input[0])
print(result)
#print('Repeats detected as a list: ', result[0])
#print('Sum of all repeats: ', result[1])

### Checking for invalid new logic
# create a chunk with just first char.
# loop through array with this chunk size so if size = 1, every char should match chunk.
# if miss, increment chunk size by 1, loop again this time comparing chunk with 2 chars at a time
# if miss increment once more and repeat process
# if entire string is put into chunk, there are no repeats.
'''
    chunk_size = 1
            chunk = ''
            buffer = ''
            seq_counter = 0
            # while True:
            for j in range(len(f_id_str)):
                chunk += f_id_str[chunk_size-1]
                buffer+=(f_id_str[j])
                print('chunk: ', chunk, chunk_size)
                print('buffer: ', buffer)
                if len(buffer) == chunk_size:
                    if chunk == buffer: 
                        seq_counter += 1
                else:
                    chunk_size += 1
                if len(buffer) == len(f_id_str): print('no repeats')
'''

# start at left most char
# append this char to empty sequence str
# move right by 1
# if same num, increment repeat counter , dont touch sequence str
# if diff, move right by 1 and append new char to sequence str
# repeat
# if same num, increment repeat counter , dont touch sequence str
# if diff, move right by 1 and append new char to sequence str
# do until you reach end