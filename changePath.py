import json
import os

path = r'data/tiny_set_v2/anns/release/corner/rgb_valid_w640h640ow100oh100.json'

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for i in range(len(data['images'])):
    a = data['images'][i]['file_name'].split('\\')
    data['images'][i]['file_name'] = os.path.join(a[0], a[1])
    print(data['images'][i])

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f)