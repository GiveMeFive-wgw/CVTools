"""
    Show some tracks line of a video
"""
import cv2
import numpy as np
import argparse
import os
import shutil


class VideoIter(object):
    def __init__(self, video_name):
        self.cap = cv2.VideoCapture(video_name)
        self.size = [int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                     int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))]
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        assert self.cap.isOpened(), FileNotFoundError
        self.num_frame = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.index = -1

    def __iter__(self):
        return self 
    
    def __next__(self):
        # while True:
        if self.index < self.num_frame:
            ret, frame = self.cap.read()
            if ret:
                self.index += 1
                return frame
            else:
                return None
        else:
            return None
    
    def __len__(self):
        return self.num_frame
    
    def release(self):
        self.cap.release()


def arg_parse():
    """
        Parse arguements to the detect module

    """
    parser = argparse.ArgumentParser(description='draw tracks line of a video through a txt file')
    parser.add_argument("--video", type=str, default='../tracking_annotations/03_cut_small.mp4', help='path to video file')
    parser.add_argument("--label_path", type=str, default='../tracking_annotations/03_cut_small.txt', help='path to label file')
    parser.add_argument("--WH", type=str, default='1920, 1080', help='width and height of video file')
    parser.add_argument("--save_path", type=str, default='../tracking_annotations/03_cut_small_track.mp4', help='path to save video file')
    parser.add_argument("--select_height", type=str, default='780,1380', help='select height of video file')
    parser.add_argument("--select_width", type=str, default='1620,2220', help='select width of video file')
    parser.add_argument("--select_class", type=int, default=1, help='select class of detection object')
    parser.add_argument("--select_track", type=int, default=300, help="select track id of detection object")
    parser.add_argument("--out_fps", type=int, default=5, help="output video fps")
    parser.add_argument("--save_mode", type=str, default='video', help="save mode: video or image")
    return parser.parse_args()


def get_labels(lines):
    """
    get lablel list from str type label lines
    args:
        lines(list): list of str type label lines
    return:
        label_dict(frame_id: list[dict{frame_id, track_id, left,top,right,down cls_id}]): list of label list
    """
    label_dict = {}
    for line in lines:
        line = line.strip().split(",")
        frame_id, track_id, x, y, w, h, _, cls_id, _, _ = [int(float(x)) for x in line]
        l, t, r, d = x, y, x+w, y+h
        tmp_dict = {'frame_id': frame_id, 'track_id': track_id, 'left':l, 'top':t, 'right':r, 'down':d, 'cls_id': cls_id}
        if frame_id not in label_dict:
            label_dict[frame_id] = [tmp_dict]
        else:
            label_dict[frame_id].append(tmp_dict)
    return label_dict


def is_in_select_area(label, select_height, select_width):
    """
    check if a label is in select area
    args:
        label(dict{frame_id, track_id, left,top,right,down cls_id}): label dict
        select_height(tuple): select height of video file
        select_width(tuple): select width of video file
    return:
        bool: True or False
    """
    print('bbox: ', label['left'], label['right'], label['top'], label['down'])
    print('sh: {}, sw: {}'.format(select_height, select_width))
    if (label['left'] > select_width[0] and label['right'] < select_width[1]) or (label['top'] > select_height[0] and label['down'] < select_height[1]):
        return True
    else:
        return False


def main():
    args = arg_parse()
    # cap = cv2.VideoCapture(args.video)
    cap = VideoIter(args.video)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # WH = args.WH.split(',')
    WH = cap.size
    WH = (int(WH[1]), int(WH[0]))
    print("WH: ", WH)
    fps = args.out_fps
    if args.save_mode == "video":
        out = cv2.VideoWriter(args.save_path, fourcc, fps, WH)
    else:
        out = None
        save_dir = args.save_path
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
    with open(args.label_path, 'r') as f:
        lines = f.readlines()
    labels = get_labels(lines)
    
    track_dict = {}
    count_draw = 0
    for i, frame in enumerate(cap):
        if frame is None:
            break
        # print(frame.shape)
        # print("dealing with frame {}".format(i))
        for label in labels[i+1]:
            if (count_draw <= args.select_track or label['track_id'] in track_dict) and label['cls_id'] == args.select_class:
                # if is_in_select_area(label, select_height, select_width):
                color = (0, 255, 0) if label['cls_id'] >= 1 else (0, 0, 255)
                # draw bbox
                cv2.rectangle(frame, (label['left'], label['top']), (label['right'], label['down']), color, 2)
                
                # draw track line
                if label['track_id'] not in track_dict:
                    track_dict[label['track_id']] = [((label['left']+label['right'])//2, (label['top']+label['down'])//2)]
                    count_draw += 1
                else:
                    track_dict[label['track_id']].append(((label['left']+label['right'])//2, (label['top']+label['down'])//2))
                for j in range(len(track_dict[label['track_id']])-1):
                    cv2.line(frame, track_dict[label['track_id']][j], track_dict[label['track_id']][j+1], color, 2)
        
        print("draw {} tracks".format(count_draw))
        # print(frame.shape)
        if args.save_mode == "video":
            out.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            cv2.imwrite(os.path.join(save_dir, "frame_{}.jpg".format(i)), frame)
    
    cap.release()
    if args.save_mode == "video":
        out.release()


if __name__ == '__main__':
    main()