import sys, json
path='ITSCloud-main/Python/Python5_6/json/esempio.json'
thisdict={"brend":"ford",
          "electric":False,
          "year":1964,
          "colors":["red", "white", "blue"]}
thisdict2 = "{\"brand\":\"ford\",\"electric\":false,\"year\":1964,\"colors\":[\"red\", \"white\", \"blue\"]}"

def Serializza(thisdict, path):
    str=(json.dumps(thisdict))
    try:
        with open(path,'a') as f:
            f.write("\n")
            f.write(str)
            return True
    except Exception as e:
        return False

def Deserializza(thisdict2):
    try:
        diz= json.loads(thisdict2)
        return diz
    except Exception as e:
        return None

print(Serializza(thisdict,path))
print(Deserializza(thisdict2))