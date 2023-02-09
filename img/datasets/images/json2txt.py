import json
import os

jsons_path = r"./image2/"
txt_dir = r"./txt_labels"
W, H = 3840, 2160

if not os.path.exists(txt_dir):
    os.makedirs(txt_dir)

for root, dirs, files in os.walk(jsons_path):
    for file in files:
        if file.endswith("json"):
            json_path = os.path.join(root, file)
            # read the json file and convert it into txt format
            points_label = []
            with open(json_path, 'r') as load_f:
                load_dict = json.load(load_f)
                for label in load_dict['shapes']:
                    tmp = label['points']
                    tmp = str(tmp[0][0]) + " " + str(tmp[0][1])
                    points_label.append(tmp)
            txt_path = os.path.join(txt_dir, file.replace("json", "txt"))
            with open(txt_path, "w") as write_f:
                for point_label in points_label:
                    write_f.write(point_label+'\n')
            print("write file {} done!".format(txt_path))
