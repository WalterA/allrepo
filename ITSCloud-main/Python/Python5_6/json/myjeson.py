import sys, json
path='ITSCloud-main/Python/Python5_6/json/esempio.json'
thisdict={"brend":"ford",
          "electric":False,
          "year":1964,
          "colors":["red", "white", "blue"]}
thisdict2 = "{\"brand\":\"ford\",\"electric\":false,\"year\":1964,\"colors\":[\"red\", \"white\", \"blue\"]}"

def Serializza(thisdict, path):
    str=json.dumps(thisdict)
    try:
        with open(path,'w') as f:
            
            f.write(str)            
        return True
    except Exception as e:
        return False

def Deserializza(path):
    try:
        with open(path,'r') as f:
            
            return json.load(f)
    
    except Exception as e:
        print(e)
        return None

print(Serializza(thisdict,path))
print(Deserializza(path))