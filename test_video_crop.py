from typing import IO


def readCSV():
    result = open('C:/Users/User/PycharmProjects/ai_highlight_soccer/result.csv')
    highlights=[];
    compare = ""
    while True:
        time = result.readline()
        if time == "":
            break;
        slice = time[19:-2]
        '''ex) bordeaux 0 1 paris sg 일때'''

        if slice != compare:
            highlights.append((time[:8]))
            aa = time[:8][6:]
            print(int(aa))
        compare = slice

    return highlights

if __name__ == "__main__":
    readCSV()
    # vision_test('output/frames/frame308.jpg'