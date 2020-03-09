def occurence():
    i=0
    with open("authwebmmi.log", "r") as log_file:
        for line in log_file.readlines():
            if "authentication failure" in line:
                i+=1
    print("Le Fichier contient "+str(i)+" echec d'autentification")
occurence()


#[slaynpool@MiniZbeub]code$ python 1.py 
#Le Fichier contient 7149 echec d'autentification

