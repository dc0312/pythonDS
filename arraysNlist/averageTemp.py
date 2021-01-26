# Program will take a input from user and will ask user to enter temperature and then will calculate the average.
# Author : DC

class AverageTemp:

    def getTempFromUser(self):
        numberOfDays = int(input("How many day's temperature?"))
        tempList = list()
        for i in range(0, int(numberOfDays)):
            temp = int(input("Day " + str(i + 1) + "'s high temp :"))
            tempList.append(temp)

        return tempList

    def average(self,templist):
        sum = 0
        for i in templist:
            sum+=i
        return sum/len(templist)

    def findAboveAverage(self,templist,avg):
        count =0
        for i in templist:
            if int(i) > avg:
                count+=1
        return count


if __name__ == '__main__':
    a = AverageTemp()
    templist  = a.getTempFromUser()
    print(templist)
    avg = a.average(templist)
    print("Average = "+str(avg))
    count = a.findAboveAverage(templist,avg)
    print(str(count)+"day(s) above average")


