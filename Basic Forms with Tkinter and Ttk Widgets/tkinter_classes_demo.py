import tkinter as tk
import json

class JSONVar(tk.StringVar):
    #A Tk variable that can hold dicts and lists
    def __init__(self, *args, **kwargs):
        kwargs["value"] = json.dumps(kwargs.get("value"))
        super().__init__(*args, **kwargs)

    def set(self, value, *args, **kwargs):
        string = json.dumps(value)#converts python object to json
        super().set(string, *args, **kwargs)
    
    def get(self, *args, **kwargs):
        string = super().get(*args, **kwargs)
        return json.loads(string)

root = tk.Tk()
var1 = JSONVar(root)
var1.set([1, 2, 3])
var2 = JSONVar(root, value={"a": 10, "b":15})

print("Var1: ", var1.get()[1])

print("Var2: ", var2.get()["b"])