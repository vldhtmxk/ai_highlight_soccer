from typing import IO

# 결과값을 불러와 필요한 텍스트 추출
def readCSV():
    result = open('C:/Users/User/PycharmProjects/videoTotext/result.csv')
    highlights=[];
    compare = ""
    while True:
        time = result.readline()
        slice = time[21:-2]
        '''ex) bordeaux 0 1 paris sg 일때'''

        if slice != compare:
            print(time[:8])
            highlights.append((time[:8]))
            print(time[20:-2])
        compare = slice
        if time == "":
            break;

    return highlights

if __name__ == "__main__":
    readCSV()
    # vision_test('output/frames/frame308.jpg')
