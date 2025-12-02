def invalid_ids(list_of_ids):
    list_of_ids = list_of_ids.split(',') # input parsing
    list_of_invalids, sum_of_invalids = [], 0 # empty list of ids
    for id_set in list_of_ids:
        ids = id_set.split('-')
        first_id, last_id = int(ids[0]), int(ids[1])
        while first_id <= last_id:
            f_id_str = str(first_id) # monke
            halfpoint = len(f_id_str) // 2
            if (f_id_str[:halfpoint] == f_id_str[halfpoint:]): # if string is mirrored
                list_of_invalids.append(first_id)
                sum_of_invalids += first_id
            first_id += 1
    return(sum(list_of_invalids))

with open('input.txt', 'r') as file:
    data_input = file.readlines()

print(invalid_ids(data_input[0]))