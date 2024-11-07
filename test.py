class BullsAndCows:
    possibilities = {}
    number = "6379"
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def initPossibilities(self):
        for i in range(1000, 10000):
            char_seen = []
            for char in str(i):
                if char in char_seen:
                    break
                char_seen.append(char)

            if len(char_seen) == 4:
                self.possibilities[str(i)] = 1

    def getHighestPossibilityNumber(self):
        highestPossbility = 0
        highestPossbilityKey = ""
        for possibility in self.possibilities:
            if self.possibilities[possibility] > highestPossbility:
                highestPossbilityKey = possibility
                highestPossbility = self.possibilities[possibility]

        return highestPossbilityKey

    def findNumberOfMatches(self, guess):
        numOfExactPlaceMatches, numOfNonPlaceMatches = 0, 0
        for char in str(guess):
            if self.number[guess.index(char)] == char:
                numOfExactPlaceMatches += 1
                continue
            if char in self.number:
                numOfNonPlaceMatches += 1
                continue

        return numOfExactPlaceMatches, numOfNonPlaceMatches

    def findNumberOfMatchesBetweenTwonumbers(self, guess, secondNumber):
        numOfExactPlaceMatches, numOfNonPlaceMatches = 0, 0
        for char in str(guess):
            if secondNumber[guess.index(char)] == char:
                numOfExactPlaceMatches += 1
                continue
            if char in secondNumber:
                numOfNonPlaceMatches += 1
                continue

        return numOfExactPlaceMatches, numOfNonPlaceMatches

    def runOneRound(self, highestPossibiltyKey, numOfExactMatches, numOfWrongPlaceMatches):
        self.calculatePossibilities(highestPossibiltyKey, numOfExactMatches, numOfWrongPlaceMatches)

    def guessNumber(self):
        highestPossibiltyKey = self.getHighestPossibilityNumber()
        return highestPossibiltyKey
    def calculatePossibilities(self, number, numOfExactMatches, numOfWrongPlaceMatches):
        if numOfExactMatches == 0 and numOfWrongPlaceMatches == 0:
            for possibleNumber in self.possibilities:
                for digit in number:
                    if digit in possibleNumber:
                        self.possibilities[possibleNumber] = 0

        if numOfExactMatches == 1 and numOfWrongPlaceMatches == 0:
            for index in range(4):
                for possibleNumber in self.possibilities:
                    num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                    if self.possibilities[possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                        continue
                    if possibleNumber[index] == number[index]:
                        self.possibilities[possibleNumber] += 1

        if numOfExactMatches == 2 and numOfWrongPlaceMatches == 0:
            for index in range(4):
                for secondIndex in range(index + 1, 4):
                    for possibleNumber in self.possibilities:
                        num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                        if self.possibilities[possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                            continue
                        if possibleNumber[index] == number[index] and possibleNumber[secondIndex] == number[secondIndex]:
                            self.possibilities[possibleNumber] += 1

        if numOfExactMatches == 3 and numOfWrongPlaceMatches == 0:
            for possibleNumber in self.possibilities:
                num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                if self.possibilities[possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                    continue
                if possibleNumber[0] != number[0] and possibleNumber[1] == number[1] and possibleNumber[2] == number[2] and possibleNumber[3] == number[3]:
                    self.possibilities[possibleNumber] += 1
                if possibleNumber[0] == number[0] and possibleNumber[1] != number[1] and possibleNumber[2] == number[2] and possibleNumber[3] == number[3]:
                    self.possibilities[possibleNumber] += 1
                if possibleNumber[0] == number[0] and possibleNumber[1] == number[1] and possibleNumber[2] != number[2] and possibleNumber[3] == number[3]:
                    self.possibilities[possibleNumber] += 1
                if possibleNumber[0] == number[0] and possibleNumber[1] == number[1] and possibleNumber[2] == number[2] and possibleNumber[3] != number[3]:
                    self.possibilities[possibleNumber] += 1

        if numOfExactMatches == 1 and numOfWrongPlaceMatches == 1:
            for index in range(4):
                for secondIndex in range(4):
                    if index == secondIndex:
                        continue

                    for possibleNumber in self.possibilities:
                        num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                        if self.possibilities[
                            possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                            continue
                        if possibleNumber[index] != number[index]:
                            continue
                        if number[secondIndex] in possibleNumber and possibleNumber.index(number[secondIndex]) != secondIndex:
                            self.possibilities[possibleNumber] += 1

        if numOfExactMatches == 1 and numOfWrongPlaceMatches == 2:
            for index in range(4):
                for secondIndex in range(4):
                    if index == secondIndex:
                        continue
                    for thirdIndex in range(4):
                        if thirdIndex == index or thirdIndex == secondIndex:
                            continue

                        for possibleNumber in self.possibilities:
                            num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                            if self.possibilities[
                                possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                                continue
                            if possibleNumber[index] != number[index]:
                                continue
                            if number[secondIndex] in possibleNumber and possibleNumber.index(number[secondIndex]) != secondIndex:
                                if number[thirdIndex] in possibleNumber and possibleNumber.index(
                                        number[thirdIndex]) != thirdIndex:
                                    self.possibilities[possibleNumber] += 1

        if numOfExactMatches == 1 and numOfWrongPlaceMatches == 3:
            for index in range(4):
                for secondIndex in range(4):
                    if index == secondIndex:
                        continue
                    for thirdIndex in range(4):
                        if thirdIndex == index or thirdIndex == secondIndex:
                            continue
                        for fourthIndex in range(4):
                            if fourthIndex == index or fourthIndex == secondIndex or fourthIndex == thirdIndex:
                                continue

                            for possibleNumber in self.possibilities:
                                num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                                if self.possibilities[
                                    possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                                    continue
                                if possibleNumber[index] != number[index]:
                                    continue
                                if number[secondIndex] in possibleNumber and possibleNumber.index(
                                        number[secondIndex]) != secondIndex:
                                    if number[thirdIndex] in possibleNumber and possibleNumber.index(
                                            number[thirdIndex]) != thirdIndex:
                                        if number[fourthIndex] in possibleNumber and possibleNumber.index(
                                                number[fourthIndex]) != fourthIndex:
                                            self.possibilities[possibleNumber] += 1

        if numOfExactMatches == 2 and numOfWrongPlaceMatches == 1:
            for index in range(4):
                for secondIndex in range(4):
                    if index == secondIndex:
                        continue
                    for thirdIndex in range(4):
                        if thirdIndex == index or thirdIndex == secondIndex:
                            continue
                        for possibleNumber in self.possibilities:
                            num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                            if self.possibilities[
                                possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                                continue
                            if possibleNumber[index] != number[index]:
                                continue
                            if possibleNumber[secondIndex] != number[secondIndex]:
                                continue
                            if number[thirdIndex] in possibleNumber and possibleNumber.index(
                                    number[thirdIndex]) != thirdIndex:
                                self.possibilities[possibleNumber] += 1

        if numOfExactMatches == 2 and numOfWrongPlaceMatches == 2:
            for index in range(4):
                for secondIndex in range(4):
                    if index == secondIndex:
                        continue
                    for thirdIndex in range(4):
                        if thirdIndex == index or thirdIndex == secondIndex:
                            continue
                        for fourthIndex in range(4):
                            if fourthIndex == index or fourthIndex == secondIndex or fourthIndex == thirdIndex:
                                continue
                            for possibleNumber in self.possibilities:
                                num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                                if self.possibilities[
                                    possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                                    continue
                                if possibleNumber[index] != number[index]:
                                    continue
                                if possibleNumber[secondIndex] != number[secondIndex]:
                                    continue
                                if number[thirdIndex] in possibleNumber and possibleNumber.index(
                                        number[thirdIndex]) != thirdIndex:
                                    if number[fourthIndex] in possibleNumber and possibleNumber.index(
                                            number[fourthIndex]) != fourthIndex:
                                        self.possibilities[possibleNumber] += 1

        if numOfExactMatches == 3 and numOfWrongPlaceMatches == 1:
            for index in range(4):
                for secondIndex in range(4):
                    if index == secondIndex:
                        continue
                    for thirdIndex in range(4):
                        if thirdIndex == index or thirdIndex == secondIndex:
                            continue
                        for fourthIndex in range(4):
                            if fourthIndex == index or fourthIndex == secondIndex or fourthIndex == thirdIndex:
                                continue
                            for possibleNumber in self.possibilities:
                                num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                                if self.possibilities[
                                    possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                                    continue
                                if possibleNumber[index] != number[index]:
                                    continue
                                if possibleNumber[secondIndex] != number[secondIndex]:
                                    continue
                                if possibleNumber[thirdIndex] != number[thirdIndex]:
                                    continue
                                if number[fourthIndex] in possibleNumber and possibleNumber.index(
                                        number[fourthIndex]) != fourthIndex:
                                    self.possibilities[possibleNumber] += 1

        if numOfExactMatches == 0 and numOfWrongPlaceMatches == 1:
            for index in range(4):
                for possibleNumber in self.possibilities:
                    num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                    if self.possibilities[
                        possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                        continue
                    if number[index] in possibleNumber and possibleNumber.index(number[index]) != index:
                        self.possibilities[possibleNumber] += 1

        if numOfExactMatches == 0 and numOfWrongPlaceMatches == 2:
            for index in range(4):
                for secondIndex in range(4):
                    if index == secondIndex:
                        continue
                    for possibleNumber in self.possibilities:
                        num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                        if self.possibilities[
                            possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                            continue
                        if number[index] in possibleNumber and possibleNumber.index(number[index]) != index:
                            if number[secondIndex] in possibleNumber and possibleNumber.index(
                                    number[secondIndex]) != secondIndex:
                                self.possibilities[possibleNumber] += 1

        if numOfExactMatches == 0 and numOfWrongPlaceMatches == 3:
            for index in range(4):
                for secondIndex in range(4):
                    if index == secondIndex:
                        continue
                    for thirdIndex in range(4):
                        if thirdIndex == index or thirdIndex == secondIndex:
                            continue
                        for possibleNumber in self.possibilities:
                            num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                            if self.possibilities[
                                possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                                continue
                            if number[index] in possibleNumber and possibleNumber.index(number[index]) != index:
                                if number[secondIndex] in possibleNumber and possibleNumber.index(
                                        number[secondIndex]) != secondIndex:
                                    if number[thirdIndex] in possibleNumber and possibleNumber.index(
                                            number[thirdIndex]) != thirdIndex:
                                        self.possibilities[possibleNumber] += 1

        if numOfExactMatches == 0 and numOfWrongPlaceMatches == 4:
            for index in range(4):
                for secondIndex in range(4):
                    if index == secondIndex:
                        continue
                    for thirdIndex in range(4):
                        if thirdIndex == index or thirdIndex == secondIndex:
                            continue
                        for fourthIndex in range(4):
                            if fourthIndex == index or fourthIndex == secondIndex or fourthIndex == thirdIndex:
                                continue
                            for possibleNumber in self.possibilities:
                                num1, num2 = self.findNumberOfMatchesBetweenTwonumbers(number, possibleNumber)
                                if self.possibilities[
                                    possibleNumber] == 0 or num1 != numOfExactMatches or num2 != numOfWrongPlaceMatches:
                                    continue
                                if number[index] in possibleNumber and possibleNumber.index(number[index]) != index:
                                    if number[secondIndex] in possibleNumber and possibleNumber.index(
                                            number[secondIndex]) != secondIndex:
                                        if number[thirdIndex] in possibleNumber and possibleNumber.index(
                                                number[thirdIndex]) != thirdIndex:
                                            if number[fourthIndex] in possibleNumber and possibleNumber.index(
                                                    number[fourthIndex]) != fourthIndex:
                                                self.possibilities[possibleNumber] += 1

obj = BullsAndCows()
obj.initPossibilities()

def runGame():
    lastGuess = ""
    counter = 0
    while lastGuess != obj.number:
        tahmin = obj.runOneRound()
        lastGuess = tahmin
        counter += 1

    print("found in " + str(counter) +" steps")
    return counter

while True:
    guessed_number = obj.guessNumber()
    print("guessed " + guessed_number)
    exact_match = input("Exact match: ")
    if exact_match == "x":
        exit(0)

    wrong_place_match = input("Wrong place match: ")
    if wrong_place_match == "x":
        exit(0)

    obj.runOneRound(guessed_number, int(exact_match), int(wrong_place_match))

# statistics = {}
#
# for i in range(20):
#     statistics[i] = 0
#
# for i in range(6000, 7000):
#
#     char_seen = []
#     for char in str(i):
#         if char in char_seen:
#             break
#         char_seen.append(char)
#
#     if len(char_seen) == 4:
#         print("step num: " + str(i))
#         obj.initPossibilities()
#         obj.number = str(i)
#         statistics[runGame()] += 1
#
# print(statistics)