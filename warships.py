def desk_null():# Создание пустого игрового поля 
    global lines
    lines="ABCDEFGHIJ"
    global column
    column=("1","2","3","4","5","6","7","8","9","10")
    global desk_dict
    desk_dict={}
    for i in lines:
        for j in column:
            desk_dict[i+j]="."       
    # print(desk_dict)
    return desk_dict
desk_null()
def near_coord(KEY):
    for i in  desk_dict:
        if i[0]==KEY[0] and abs(column.index(i[1:])-column.index(KEY[1:]))==1 and desk_dict[i]==desk_dict[KEY]:
            print(column.index(i[1:])-column.index(KEY[1:]))
            print(KEY,i)
        if i[1:]==KEY[1:] and abs(lines.index(i[0])-lines.index(KEY[0]))==1 and desk_dict[i]==desk_dict[KEY]:
            print(lines.index(i[0])-lines.index(KEY[0]))
            print(KEY,i)    
def CRD():  # Метод вывода игрового поля на консоль
    j = 1
    print(" ",end="  ")
    for i in column:
        print(int(i), end="  ") 
    print("")
    for i in desk_dict.keys():
        if int(i[1:]) == 1:
            print(i[0], end="  ")
        if int(i[1]) == j:
            print(desk_dict[i], end="  ")
            j += 1
        else:
            j = 1
            print(desk_dict[i])
CRD()
import random
n=1
before_letter=lambda x: lines[lines.index(x)-1] 
after_letter=lambda x: lines[lines.index(x)+1] 
before_number=lambda x: column[column.index(x)-1]
after_number=lambda x: column[column.index(x)+1]
while n<5:
    coord1 = random.choice(lines) + random.choice(column)#ввод координат 4-х палубного корабля 
    if n==1 and coord1 in desk_dict and desk_dict[coord1]==".":
        desk_dict[coord1]="o"
        print(coord1)
        if coord1[0] in lines[1:]:
            if desk_dict[before_letter(coord1[0])+coord1[1:]]==".":
                desk_dict[before_letter(coord1[0])+coord1[1:]]="+"
        if coord1[0] in lines[:-1]:
            if desk_dict[after_letter(coord1[0])+coord1[1:]]==".":
                desk_dict[after_letter(coord1[0])+coord1[1:]]="+"
        if coord1[1:] in column[1:]:
            if desk_dict[coord1[0]+before_number(coord1[1:])]==".":
                desk_dict[coord1[0]+before_number(coord1[1:])]="+"
        if coord1[1:] in column[:-1]:
            if desk_dict[coord1[0]+after_number(coord1[1:])]==".":
                desk_dict[coord1[0]+after_number(coord1[1:])]="+"
        n+=1
    if n==2:
        ship_list=[]
        for i in desk_dict:
            if desk_dict[i]=="+":
                ship_list.append(i)
        print(ship_list)
        coord2 = random.choice(ship_list)
        print(coord2)
        desk_dict[coord2]="o"
        n+=1
    if n==3:
        new_list=[]
        for_random_list=[]
        for i in desk_dict:
            if desk_dict[i]=="o": 
                new_list.append(i) 
        if new_list[0][0]==new_list[-1][0]: 
            if before_letter(new_list[0][0]) in desk_dict:
                for_random_list.append(before_letter(new_list[0][0]))
            if after_letter(new_list[-1][0]) in desk_dict: 
                for_random_list.append(after_letter(new_list[-1][0]))
        if new_list[0][1:]==new_list[-1][1:]: 
            if before_number(new_list[0][1:]) in desk_dict:
                for_random_list.append(before_number(new_list[0][1:]))
            if after_number(new_list[-1][1:]) in desk_dict: 
                for_random_list.append(after_number(new_list[-1][1:]))
        n+=1
    else:
        n+=1
    # if n==3:
        
# print(desk_dict)
CRD()

# i=1
# before_letter=lambda x: lines[lines.index(x)-1] 
# after_letter=lambda x: lines[lines.index(x)+1] 
# before_number=lambda x: column[column.index(x)-1]
# after_number=lambda x: column[column.index(x)+1]
# while i<5:
#     coord1 = random.choice(lines) + random.choice(column)#ввод координат 4-х палубного корабля 
#     if coord1 in desk_dict and desk_dict[coord1]==".":
#         desk_dict[coord1]="o"
#         print(coord1)
#         if coord1[0] in lines[1:]:
#             if desk_dict[before_letter(coord1[0])+coord1[1:]]==".":
#                 desk_dict[before_letter(coord1[0])+coord1[1:]]="+"
#         if coord1[0] in lines[:-1]:
#             if desk_dict[after_letter(coord1[0])+coord1[1:]]==".":
#                 desk_dict[after_letter(coord1[0])+coord1[1:]]="+"
#         if coord1[1:] in column[1:]:
#             if desk_dict[coord1[0]+before_number(coord1[1:])]==".":
#                 desk_dict[coord1[0]+before_number(coord1[1:])]="+"
#         if coord1[1:] in column[:-1]:
#             if desk_dict[coord1[0]+after_number(coord1[1:])]==".":
#                 desk_dict[coord1[0]+after_number(coord1[1:])]="+"
#         i+=1
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 