# swap two elements in a list

# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]

# Swap function
# --------------
def swappositions(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2], list[pos1]
    return list
# Driver function
list = [23,65,19,90]
pos1,pos2 = 1,3

print(swappositions(list,pos1 -1 , pos2 -1))

print('# --------------------------------------------------\n')

def swappositions(list,pos1,pos2):
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2-1)

    list.insert(pos1,second_ele)
    list.insert(pos2,first_ele)

    return list

list = [23,65,19,90]
pos1,pos2 = 2,4

print(swappositions(list,pos1-1,pos2-1))
print('# -----------------------------\n')
def swapposition(list,pos1,pos2):
    get = list[pos1], list[pos2]

    list[pos2], list[pos1] = get

    return list

list = [23,65,19,90]

pos1, pos2 =1,3

print(swapposition(list,pos1-1,pos2-1))
print('# ----------------------------\n')

def swapposition(lis,pos1,pos2):
    temp = lis[pos1]
    lis[pos1] = lis[pos2]
    lis[pos2] = temp
    return lis

list = [23,65,19,90]
pos1,pos2 = 2,4

print(swapposition(list,pos1-1,pos2-1))
print('# -------------------------------\n')

def swapposition(lis,pos1,pos2):
    for i, x in enumerate(lis):
        if i == pos1:
            elem1 = x

        if i == pos2:
            elem2 = x

    lis[pos1] = elem2
    lis[pos2] = elem1

    return lis

list = [23,65,19,90]
pos1, pos2 = 1,4
print(swapposition(list,pos1-1, pos2-1))
print('# -----------------------------\n')




































    
