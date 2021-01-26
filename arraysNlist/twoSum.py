# Program to find all pairs of integers whose sum is equal to a given number
# Author : DC

class TwoSum:

    def findPairs(self,arr, param):

        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    pass
                elif arr[i] + arr[j] == param:
                    print(str(i), str(j) + " ==> "+str(arr[i]),str(arr[j]))


if __name__ == '__main__':
    t = TwoSum()
    arr = [1, 2, 3, 2, 3, 4, 5, 6]
    t.findPairs(arr, 6)
    my_dict = {}
    my_dict[1] = 1
    my_dict['1'] = 2
    my_dict[1.0] = 4
    print(my_dict)
    sum = 0
    for k in my_dict:
        sum += my_dict[k]

    print(sum)

    rec = {"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}
    id1 = id(rec)
    del rec
    rec = {"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}
    id2 = id(rec)
    print(id1 == id2)