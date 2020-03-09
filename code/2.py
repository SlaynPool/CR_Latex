def occurence():
    i=0
    with open("authwebmmi.log", "r") as log_file:
        for line in log_file.readlines():
            if "Failed password for invalid user" in line:
                i+=1
    print("Le Fichier contient "+str(i)+" Failed password for invalid user")
occurence()

#[slaynpool@MiniZbeub]code$ python 2.py 
#Le Fichier contient 4219 Failed password for invalid user

