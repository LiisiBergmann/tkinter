import xlrd
import matplotlib.pyplot as plt
import pandas as pd


df2 = pd.read_excel("Kodutöö.xlsx", "Leht4")

df2.plot(kind="line", x="Päev", y="Juhtumid",  color="green")
df2.plot(kind="line", x="Päev", y="surnud", color="orange")

plt.xlabel("Päevad")
plt.ylabel("Juhtumid / surnud")
plt.title("Hiina")


plt.show()