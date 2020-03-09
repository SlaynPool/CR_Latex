import matplotlib.pyplot as plt
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

x=[stats["authentication failure"] ,stats["Failed password for invalid user"]]
labels=["auth failed","Failed PASSWD"]
plt.pie(x, labels = labels, shadow=False)
plt.legend()
plt.savefig("stats.png")
plt.close()
#[slaynpool@MiniZbeub]code$ python 4.py 
#authentication failure:7149
#Failed password for invalid user:4219
#Warning: QT_DEVICE_PIXEL_RATIO is deprecated. Instead use:
#   QT_AUTO_SCREEN_SCALE_FACTOR to enable platform plugin controlled per-screen factors.
#   QT_SCREEN_SCALE_FACTORS to set per-screen DPI.
#   QT_SCALE_FACTOR to set the application global scale factor.

