def number_of_combination(group, member):

    cb_up = 1
    cb_down_1 = 1
    cb_down_2 = 1

    for mem in range(1, group+1):
        cb_up *= mem

    for mem in range(1, member+1):
        cb_down_1 *= mem

    for mem in range(1, (group-member)+1):
        cb_down_2 *= mem

    output = cb_up/(cb_down_1 * cb_down_2)
    return int(output)

print(number_of_combination(6, 2))
