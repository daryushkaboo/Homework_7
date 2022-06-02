import os

file_list = ['1.txt', '2.txt', '3.txt']

def merge_files():
    lenght_dict = {}
    for file in file_list:
        lines_ammount = 0
        with open (file) as f:
            for line in f:
                lines_ammount +=1
            lenght_dict[file] = lines_ammount
    sorted_dict = {}
    sorted_keys = sorted(lenght_dict, key=lenght_dict.get)
    for k in sorted_keys:
        sorted_dict[k] = lenght_dict[k]
    
    with open('result.txt', 'w', encoding='utf-8') as f:
        for i, j in sorted_dict.items():
            with open(i, encoding='utf-8') as general:
                f.write(i + '\n' + str(j) + '\n')
                for k in general:
                    f.write(k)
                f.write('\n')

merge_files()