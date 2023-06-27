import xlrd
import matplotlib.pyplot as plt
import pandas as pd


df2 = pd.read_excel("Kodutöö.xlsx", "Leht3")

df2.plot(kind="line", x="Päev", y="Juhtumid",  color="blue")

plt.xlabel("Päevad")
plt.ylabel("Juhtumid")
plt.title("Brazil")


df2.plot(kind="line", x="Päev", y="surnud", color="red")

plt.xlabel("Päevad")
plt.ylabel("surnud")
plt.title("Brazil")


plt.show()