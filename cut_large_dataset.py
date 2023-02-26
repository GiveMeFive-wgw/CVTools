from crop import slidingWindowCrop as SW
from crop import randomCenterCrop as RC

sw = SW(windowSize=(960, 960))

img_path = 'datasets/large_tiny_dataset/images'
label_path = 'datasets/large_tiny_dataset/labels'

CLASSES = {0: 'small'}
sw.inputImage(img_path)
sw.inputLabel(label_path, CLASSES, coordinates='yolo')

nums = 0

for i in range(len(sw.dataSet)):
    nums += sw.saveSubImageAndTxt(i, 'sub_imgs', 'sub_labels', overlap=0.2, resize=(960, 960))
print(f'nums: {nums}')