import matplotlib.pyplot as plt
from pdflatex import PDFLaTeX


stats = {
    "authentication failure" : 0,
    "Failed password for invalid user" : 0,
    "Failed password for root" : 0,
}
def genLatex():
    rapport = open("rapport.tex", "w")
    rapport.write('\\documentclass[10pt,a4paper]{article}\n')
    rapport.write('\\usepackage[utf8]{inputenc}\n')
    rapport.write('\\usepackage[french]{babel}\n')
    rapport.write('\\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}\n')
    rapport.write('\\usepackage{hyperref}\n')
    rapport.write('\\usepackage{graphicx}\n')
    rapport.write('\\title{Rapport de log}\n')
    rapport.write('\\author{Votre serviable Crontab}\n')
    rapport.write('\\begin{document}\n')
    rapport.write('\\maketitle\n')
    rapport.write('\\url{Machine.int:/fichierAnalysee}\n')
    rapport.write('\\section{Nombres derreur Importante} \n')
    rapport.write('\\begin{itemize}\n')
    for key in stats:
        rapport.write('\\item '+key+' '+ str(stats[key])+'\n')
    rapport.write('\\end{itemize}\n')
    rapport.write('\\begin{figure}[h!]\n')
    rapport.write('\\centering\n')
    rapport.write('\\includegraphics[width=0.9\\textwidth]{stats.jpg}\n')
    rapport.write('\\caption{Some statistics}\n')
    rapport.write('\\label{fig:universe}\n')
    rapport.write('\\end{figure}\n')
    rapport.write('\\end{document}\n')
def pdflatex():
    pdfl = PDFLaTeX.from_texfile('rapport.tex')
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
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

x=[stats["authentication failure"] ,stats["Failed password for invalid user"],stats["Failed password for root"]]
labels=["auth failed","Failed PASSWD","Connection failed AS ROOT"]
plt.pie(x, labels = labels, shadow=False)
plt.legend()
plt.savefig("stats.jpg")
plt.close()
genLatex()
pdflatex()
