import os

dir_path = r"./my_dataset/test/"
out_path = r"./my_dataset/test.list"
base_path = "test"

for root, dirs, files in os.walk(dir_path):
    label_list = []
    for file in files:
        if file.endswith(".txt"):
            label_path = os.path.join(base_path, file)
            image_path = os.path.join(base_path, file.replace(".txt", ".jpg"))
            out_str = image_path + " " + label_path
            print("out_str: ", out_str)
            label_list.append(out_str)

with open(out_path, 'w') as f:
    for line in label_list:
        f.write(line+"\n")
print("write successfully!")