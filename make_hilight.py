import os
import test_video_crop as tvc
from datetime import time
import datetime


def make_highlight():
    highlight_result_array = tvc.readCSV()
    list = "C:/Users/User/PycharmProjects/ai_highlight_soccer/list.txt"
    i = 0
    while len(highlight_result_array)-1:
        with open(list, 'a') as f:
            form = "'test_video/video_clip{}.mp4'".format(i)
            f.write("file " + "'" + form + "'" +"\n")

        t= int(highlight_result_array[i][6:])
        startTime = datetime.timedelta(seconds=(t-180))
        endTime = datetime.timedelta(seconds=(t+180))
        os.system( "ffmpeg -i Fullvideo.mp4 -ss " + str(startTime) + " -to " + str(endTime) + " -c copy test_video/video_clip{}.mp4".format(i))
        i += 1

os.system("ffmpeg -f concat -safe 0 -i list.txt -c copy highlightvideo.mp4")


if __name__ == "__main__":
    make_highlight()