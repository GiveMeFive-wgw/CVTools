"""
    convert label [small, car, truck, bus] t0 [car, bus, truck]
"""
import os

path = r'labels'

convert_dict = {1:'0', 3:'1', 2:'2'}

for file in os.listdir(path):
    if file == 'classes.txt':
        continue
    print("deal with file: {}".format(file))
    with open(os.path.join(path, file), 'r') as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        line = line.replace(line[0], convert_dict[int(line[0])], 1)
        new_lines.append(line)
    with open(os.path.join('convert_labels',file), 'w') as f:
        f.writelines(new_lines)
