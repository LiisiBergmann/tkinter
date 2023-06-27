

import xlrd
import matplotlib.pyplot as plt

fail = ("Kontroll.xlsx")

excelDokument = xlrd.open_workbook(fail)                # salvestan lehekülje, kust andmeid hakkan võtma
sheet = excelDokument.sheet_by_index(0)


veerg = sheet.col_values(0)
rida = sheet.row_values(0)
lahter = sheet.cell_value(0,0)

print(veerg,rida,lahter)



x = sheet.col_values(0) # listid
y = sheet.col_values(1)


plt.plot(x,y) # üks joon, argumentisk kindlasti list
#nimede teljed
plt.xlabel("X-telg")
plt.ylabel("y-telg")

plt.title("Graaf")
plt.show() #Loob graafi"""