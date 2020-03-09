stats = {
    "authentication failure" : 0,
    "Failed password for invalid user" : 0,
}

def occurence(recherche):
    i=0
    with open("authwebmmi.log", "r") as log_file:
        for line in log_file.readlines():
            if recherche in line:
                i+=1
    return i


res=occurence("authentication failure")
for key in stats:
    stats[key]=occurence(key)
    print(key+":" + str(stats[key]))
#[slaynpool@MiniZbeub]code$ python 3.py 
#authentication failure:7149
#Failed password for invalid user:4219

