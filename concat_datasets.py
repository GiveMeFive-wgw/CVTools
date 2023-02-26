import json
import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--base_dataset', type=str, help='Base dataset')
    parser.add_argument('--add_dataset', type=str, help='Additional dataset')
    parser.add_argument('--save_path', type=str, help='Save path')
    
    args = parser.parse_args()
    
    with open(args.base_dataset, 'r', encoding='utf-8') as f:
        base_dataset = json.load(f)
    with open(args.add_dataset, 'r', encoding='utf-8') as f:
        add_dataset = json.load(f)
    
    # base_dataset['images'] += add_dataset['images']
    # base_dataset['annotations'] += add_dataset['annotations']
    max_image_id = 0
    max_id = 0
    for base_it in base_dataset['images']:
        if base_it['id'] > max_image_id:
            max_image_id = base_it['id']
    print("max_image_id: ", max_image_id)
    for base_it in base_dataset['annotations']:
        if base_it['id'] > max_id:
            max_id = base_it['id']
    print("max_id: ", max_id)
    for i in range(len(add_dataset['images'])):
        add_dataset['images'][i]['id'] += max_image_id+2
    for i in range(len(add_dataset['annotations'])):
        add_dataset['annotations'][i]['id'] += max_id+2
        add_dataset['annotations'][i]['image_id'] += max_image_id+2
    
    base_dataset['images'] += add_dataset['images']
    base_dataset['annotations'] += add_dataset['annotations']

    print("length of images: ", len(base_dataset['images']))
    l1 = [it['id'] for it in base_dataset['images']]
    print("duplicated id: ", [x for x in l1 if l1.count(x) > 1])
    
    with open(args.save_path, 'w', encoding='utf-8') as f:
        json.dump(base_dataset, f, indent=4, ensure_ascii=False)
