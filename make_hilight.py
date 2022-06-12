import os
import test_video_crop as tvc


def make_highlight():
    highlight_result_array = tvc.readCSV()

    while True:
        for i in highlight_result_array:
            with open(list, 'a') as f:
                form = 'test_video/video_clip_{}.mp4'.format(i)
                f.write("file " + form)
            startTime = time.fromisoformat(highlight_result_array[i] * 100 - 60)
            endTime = time.fromisoformat(startTime + 60)
            os.system(
                "ffmpeg -i Fullvideo.mp4 -ss " + startTime + " -to " + endTime + " -c copy test_video/video_clip{}.mp4")
            if highlight_result_array[i + 1] is None:
                break
    os.system("ffmpeg -f concat -safe 0 -i list.txt -c copy highlightvideo.mp4")


if __name__ == "__main__":
    main()
