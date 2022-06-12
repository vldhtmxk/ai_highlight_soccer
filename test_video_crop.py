from typing import IO


def readCSV():
    result = open('C:/Users/User/PycharmProjects/videoTotext/result.csv')
    highlights=[];
    compare = ""
    while True:
        time = result.readline()
        slice = time[19:-2]
        '''ex) bordeaux 0 1 paris sg 일때'''

        if slice != compare:
            print(time[:8])
            highlights.append((time[:8]))
            print(time[19:-2])
        compare = slice
        if time == "":
            break;

    return highlights

if __name__ == "__main__":
    readCSV()
    # vision_test('output/frames/frame308.jpg')
