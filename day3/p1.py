def max_joltage(bank):
    best = 0
    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            best = max(best, int(bank[i] + bank[j]))
    return best

joltages = []
with open('input.txt', 'r') as file:
    data_input = [line.rstrip() for line in file]
    for i in range(len(data_input)):
        joltages.append(max_joltage(data_input[i]))
print(len(joltages), sum(joltages))



''' Tried this way
def max_joltage(bank):
    max, max_2, largest_index= 0, 0, 0
    for i in range(len(bank)-1):
        if int(bank[i]) >= max: max, largest_index = int(bank[i]), i
    for i in range(largest_index+1, len(bank)):
        if int(bank[i]) >= max_2: max_2 = int(bank[i])
    return(int(str(max)+''+str(max_2)))
'''