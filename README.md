# CVTools
some computer vision algorithm tools
包含以下脚本：
1. keyframe.py：抓取关键帧脚本
2. cutLargeVideo.py: 将大视频剪切成小视频的脚本
3. json2txt.py：将labelme标注的关键点注释文件（json格式）转化为常用的txt格式（class, x,y)
4. concat_labels.py:将在相同数据集上标注的不同class的标注文件合并
5. convet.py: convert label [small, car, truck, bus] t0 [car, bus, truck]
6. get_list.py: 获取数据集中所有txt格式标注文件的文件列表，并保存至新文件中
