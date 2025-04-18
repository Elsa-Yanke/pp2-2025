def unique_list(list):
    new_list = []
    for i in list:       
        if i not in new_list:
            new_list.append(i)
    print(new_list)
list = list(map(int(input().split())))
unique_list(list)