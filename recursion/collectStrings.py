# Program which takes an object and returns an array of all values in the object that have a type string
# Author : DC

class CollectString:

    def collectString(self,obj):
        string = []
        for key in obj:
            if type(obj[key]) is dict:
                string.extend(self.collectString(obj[key]))
            elif type(obj[key]) is str:
                string.append(obj[key])
        return string


if __name__ == '__main__':
    obj = {
        "stuff":"foo",
        "data":{
            "val":{
                "thing":{
                    "info":"bar",
                    "moreInfo":{
                        "evenMoreInfo":{
                            "weMadeIt":"baz"
                        }
                    }
                }
            }
        }
    }
    c = CollectString()
    print(c.collectString(obj))