import xlrd
import matplotlib.pyplot as plt
import pandas as pd


df2 = pd.read_excel("Kodutöö.xlsx", "Leht2")

df2.plot(kind="line", x="Päev", y="Juhtumid",  color="green")

plt.xlabel("Päevad")
plt.ylabel("Juhtumid")
plt.title("Bangladesh")

df2.plot(kind="line", x="Päev", y="surnud", color="yellow")

plt.xlabel("Päevad")
plt.ylabel("surnud")
plt.title("Bangladesh")


plt.show()