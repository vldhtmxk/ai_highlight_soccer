from typing import IO


def readCSV():
    result = open('C:/Users/User/PycharmProjects/videoTotext/result.csv')
    highlights=[];
    compare = ""
    while True:
        time = result.readline()
        slice = time[22:-2]
        '''bordeaux 0 1 paris sg 일때'''
        print(time[3:10])
        if slice != compare:
            highlights.append((time[3:10]))
        compare = slice
        if time == "":
            break;

    return highlights

if __name__ == "__main__":
    readCSV()
    # vision_test('output/frames/frame308.jpg')
