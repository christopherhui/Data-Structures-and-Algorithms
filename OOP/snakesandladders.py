class SnakesLadders():

    def __init__(self):
        # Code Here
        self.positionZero = 0
        self.positionOne = 0
        self.playing = 1
        self.win = False
        self.special = [[2, 38], [7, 14], [8, 31], [15, 26], [21, 42], [28, 84], [36, 44], [51, 67], [71, 91], [78, 98],
                        [87, 94], [16, 6], [46, 25], [49, 11], [62, 19], [64, 60], [74, 53], [89, 68], [92, 88],
                        [95, 75], [99, 80]]

    def play(self, die1, die2):
        # Code Here
        if self.win:
            return "Game over!"

        else:
            distance = die1 + die2
            if self.playing == 1:
                old = self.playing
                self.positionZero = self.positionZero + distance

                if self.positionZero > 100:
                    self.positionZero = 100 - (self.positionZero - 100)

                if self.positionZero == 100:
                    self.win = True
                    return "Player " + str(self.playing) + " Wins!"

                for space in self.special:
                    if space[0] == self.positionZero:
                        self.positionZero = space[1]
                        break

                if die1 != die2:
                    self.playing = 2

                return "Player " + str(old) + " is on square " + str(self.positionZero)

            else:
                self.positionOne = self.positionOne + distance
                old = self.playing

                if self.positionOne > 100:
                    self.positionOne = 100 - (self.positionOne - 100)

                if self.positionOne == 100:
                    self.win = True
                    return "Player " + str(self.playing) + " Wins!"

                for space in self.special:
                    if space[0] == self.positionOne:
                        self.positionOne = space[1]
                        break

                if die1 != die2:
                    self.playing = 1

                return "Player " + str(old) + " is on square " + str(self.positionOne)