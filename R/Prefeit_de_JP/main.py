tot_wv = 0
tot_ri = 0
tot_ra = 0
tot_rc = 0
tot_nf = 0
tot_ja = 0
tot_an = 0
tot_cm = 0
tot_rf = 0
tot_rm = 0
tot_ed = 0
tot_cc = 0


with open('C:\\Users\\Usuario\\Documents\\Allan\\Dados\\p_jp_Todos_0.csv', newline='', encoding="UTF-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    c = 0
    for row in spamreader:
        if c < 1:
            c += 1
            pass
        else:
            a = row[0].split(",")
            tot_wv += int(a[1])
            tot_ri += int(a[2])
            tot_ra += int(a[3])
            tot_rc += int(a[4])
            tot_nf += int(a[5])

with open('C:\\Users\\Usuario\\Documents\\Allan\\Dados\\p_jp_Todos_1.csv', newline='', encoding="UTF-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    c = 0
    for row in spamreader:
        if c < 1:
            c += 1
            pass
        else:
            a = row[0].split(",")
            tot_rf += int(a[1])
            tot_rm += int(a[2])
            tot_ed += int(a[3])
            tot_cc += int(a[5])

with open('C:\\Users\\Usuario\\Documents\\Allan\\Dados\\p_jp_Todos_2.csv', newline='', encoding="UTF-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    c = 0
    for row in spamreader:
        if c < 1:
            c += 1
            pass
        else:
            a = row[0].split(",")
            tot_ja += int(a[1])
            tot_cm += int(a[2])
            tot_an += int(a[3])
            tot_cm += int(a[5])

#tot_wv = 0
#tot_ri = 0
#tot_ra = 0
#tot_rc = 0
#tot_nf = 0
#tot_ja = 0
#tot_an = 0
#tot_cm = 0
#tot_rf = 0
#tot_rm = 0
#tot_ed = 0
#tot_cc = 0
ing = [['Wallber Virgolino', 'Ricardo Coutinho', 'Raoni', 'Ruy Carneiro', 'Nilvan Ferreira', 'Rafael Freire', 'Rama Dantas','Edilma Freire', 'Cicero Lucena', 'João Almeida', 'Camilo Duarte', 'Anísio Maia', 'Carlos Monteiro'], [tot_wv,tot_ri,tot_ra,tot_rc,tot_nf, tot_rf,tot_ra,tot_ed, tot_cc, tot_ja, tot_cm, tot_an, tot_cm]]

ing.sort(key=lambda x)
colors = ['green', 'gold',  'mediumblue', 'darkviolet', 'darkmagenta', 'black', 'red', 'greenyellow', 'navy', 'olivedrab', 'darkred', 'red', 'lightcoral']

plt.pie(ing[1], labels=ing[0], colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

def mve(n, x):
    a = [labels[n], sizes[n], colors[n]]
    labels.pop(n)
    size.pop(n)
    colors.pop(n)
    labels.insert(x, a[0])
    size.insert(x, a[1])
    colors.insert(x, a[2])

ing = []
for c in range(len(labels)):
    ing.append([labels[c], sizes[c]])

ing.sort(key=lambda x: x[1])
sizes=[]
labels=[]
for c in range(len(ing)):
    sizes.append(ing[c][1])
    labels.append(ing[c][0])
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

import numpy as np
y_pos = np.arange(len(labels1))
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, labels1)
plt.ylabel('Pesquisas')
plt.title('Candidatos à Prefeito de João Pessoa')
plt.show()
['RC', 'AM', 'RF', 'CD', 'CM', 'JA', 'WV', 'EF', 'Ra', 'RD', 'NF', 'RCO', 'CC']
