import os
import argparse

"""
Concatenate labels with the same image name.
"""

def main():
    args = argparse.ArgumentParser()
    args.add_argument('--label1_dir', type=str, default='labels')
    args.add_argument('--label2_dir', type=str, default='labels')
    args.add_argument('--save_dir', type=str, default='labels')
    args = args.parse_args()
    l1_dir = args.label1_dir  # small dataset
    l2_dir = args.label2_dir  # large dataset
    save_dir = args.save_dir
    l1_files = os.listdir(l1_dir)
    l2_files = os.listdir(l2_dir)
    for l1_file in l1_files:
        l1_file_path = os.path.join(l1_dir, l1_file)
        l2_file_path = os.path.join(l2_dir, l1_file)
        print("concat labels: {} and {}".format(l1_file_path, l2_file_path))
        with open(l1_file_path, 'r') as f:
            l1_lines = f.readlines()
        with open(l2_file_path, 'r') as f:
            l2_lines = f.readlines()
        with open(os.path.join(save_dir, l1_file), 'w') as f:
            f.writelines(l1_lines)
            f.writelines(l2_lines)
