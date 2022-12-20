coord_dict = {}
alfit = ["A","B","C","D","E","F","G","H","I","J"]
for i in alfit:
    j = 1
    while j < 11:
        key_for_pole = 0
        key_for_pole = i+str(j)
        coord_dict[key_for_pole] = "."
        j += 1
# print(coord_dict)
print('Расположите ваши корабли!')


def CRD():# Метод вывода игрового поля на консоль
    j = 1
    for i in coord_dict.keys():
        if int(i[1]) == j:
            print(coord_dict[i], end="  ")
            j += 1
        else:
            j = 1
            print(coord_dict[i])

def proverka(a):# Метод проверка периметра вокруг введеных координат
    if alfit.index(a[0]) > 0 :
        coord_list.append(alfit[alfit.index(a[0])-1]+a[1:])#1
    if alfit.index(a[0]) < 10:
        coord_list.append(alfit[alfit.index(a[0])+1]+a[1:])#2
    if int(a[1:]) > 0:
        coord_list.append(a[0]+str(int(a[1:])-1))#3
    if int(a[1:]) < 10:
        coord_list.append(a[0]+str(int(a[1:])+1)) #4
    if alfit.index(a[0]) > 0 and int(a[1:]) > 0:
        coord_list.append(alfit[alfit.index(a[0])-1]+str(int(a[1:])-1))#5
    if alfit.index(a[0]) <10 and int(a[1:]) > 0:
        coord_list.append(alfit[alfit.index(a[0])+1]+str(int(a[1:])-1))#6
    if alfit.index(a[0]) > 0 and int(a[1:]) <10:
        coord_list.append(alfit[alfit.index(a[0])-1]+str(int(a[1:])+1))#7
    if alfit.index(a[0]) <10 and int(a[1:]) <10:
        coord_list.append(alfit[alfit.index(a[0])+1]+str(int(a[1:])+1))#8
    return coord_list

CRD()
coord_list = []
coord = None
n = 1
while n < 5:
    coord = input(f"Введите координаты {n}-го однопалубного корабля: ")
    if coord == "":
        break
    if coord in coord_list:
        continue
    coord_dict[coord] = "o"
    coord_list.append(coord)
    proverka(coord)
    n += 1
CRD()
coord = None
n = 1
m = 1
while n < 4:

    coord = input(f"Введите {m}-ую координату {n}-го двухпалубного корабля: ")
    if coord == "":
        break
    if coord in coord_list:
        continue
    if m==1:
        coord1=coord
    if m==2:
        coord2=coord
    coord_dict[coord] = "o"
    coord_list.append(coord)
    if m % 2 == 0:
        n += 1
        m = 0
        proverka(coord1)
        proverka(coord2)
    m += 1

CRD()
