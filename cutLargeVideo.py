import subprocess
import os

def cut_video(begin : str, end : str, video_path : str, id: int):
    tmp = video_path.split(".")
    video_name, suffix = tmp[0], tmp[1]
    outpath = video_name + "_" + str(id) + "." + suffix
    cmd = "ffmpeg -i " + video_path + " -ss " + begin + " -to " + end + " -c copy " + outpath

    subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    video_path = r"03.mp4"
    for i in range(15, 1200, 15):
        # 将开始和结束时间转为str格式
        begin = i - 15
        end = i
        begin_minutes = int(begin / 60)
        begin_seconds = begin % 60
        end_minutes = int(end / 60)
        end_seconds = end % 60
        begin = "00:" + str(begin_minutes) + ":" + str(begin_seconds)
        end = "00:" + str(end_minutes) + ":" + str(end_seconds)
        print("begin: {}, end: {}".format(begin, end))
        cut_video(begin=begin, end=end, video_path=video_path, id = int(i / 15))
