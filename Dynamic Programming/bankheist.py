# 1. setting up for leastValue
# 2. taking every knapsack weight (i)
# 3. taking every weight (j)
# 4. creating maxValue per weight (i)
# 5. determines if adding a specific j will increase value than leastValue, using previous determined maxValue
# leastValue -> maxValue when True

def maxWeightProfit(weightList, valueList, knapsack, maxValue):
    for i in range(knapsack + 1):
        leastValue = int(i // 2) * 3

        for j in range(len([w for w in weightList if w <= i])):
            if i == 0 or i == 1:
                break

            elif maxValue[i - weightList[j]] + valueList[j] > leastValue:
                leastValue = maxValue[i - weightList[j]] + valueList[j]

        maxValue[i] = leastValue

    return maxValue[knapsack]


def main():
    weightList = [2, 3, 4, 5, 9]
    valueList = [3, 4, 8, 8, 10]
    knapsack = 20
    maxValue = [0] * (knapsack + 1)
    print(maxWeightProfit(weightList, valueList, knapsack, maxValue))


main()
