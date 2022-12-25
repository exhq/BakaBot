import os
def addalias(x, lmao):
    os.system(f"echo '{x} {lmao}' >> alias")
def getalias(a):
    a =a.replace(".", "").replace(" ", "")
    with open("./alias", "r") as myfile:
        x = myfile.read()
        for item in x.split("\n"):
            if a in item:
               return (item.split(" ")[1])

