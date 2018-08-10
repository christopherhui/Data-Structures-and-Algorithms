def validSolution(board):
    hashTable = [None] * (300)
    startX = 10
    countColumn = 0
    startG = 200
    for row in board:

        startY = 100
        countRow = 0

        for pos in row:

            locationX = (pos + startX) % 300
            locationY = (pos + startY) % 300
            locationG = (pos + startG) % 300

            if hashTable[locationX] != None or hashTable[locationY] != None or hashTable[locationG] != None or pos == 0:
                return False

            else:
                hashTable[locationX] = pos
                hashTable[locationY] = pos
                hashTable[locationG] = pos

            startY = startY + 10
            countRow = countRow + 1

            if countRow % 3 == 0:
                startG = startG + 10

        startX = startX + 10
        countColumn = countColumn + 1

        if countColumn % 3 == 0:
            startG = 200 + int((countColumn / 3) * 30)

        else:
            startG = startG - int((countRow / 3) * 10)

    return True