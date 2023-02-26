import os
import argparse

def is_train_label(name, flag='B'):
    """
    judge whether the label is train or test

    Args:
        flag (str): Judgment marker
        name (str): Label name
    """
    return flag in name


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--dataset_path', type=str, default='./datasets/large_tiny_dataset')
    args.add_argument('--train_label', type=str, default='B')
    args.add_argument('--train_label_2', type=str, default='')
    args = args.parse_args()

    train_list = []
    test_list = []

    for root, dirs, files in os.walk(os.path.join(args.dataset_path, 'images')):
        for i, file in enumerate(files):
            if is_train_label(file, args.train_label):
                test_list.append(os.path.join(root, file))
            else:
                if args.train_label_2:
                    if is_train_label(file, args.train_label_2):
                        test_list.append(os.path.join(root, file))
                    else:
                        train_list.append(os.path.join(root, file))
                else:
                    train_list.append(os.path.join(root, file))


    with open(os.path.join(args.dataset_path,'train.txt'), 'w') as f:
        f.write('\n'.join(train_list))

    with open(os.path.join(args.dataset_path,'val.txt'), 'w') as f:
        f.write('\n'.join(test_list))




