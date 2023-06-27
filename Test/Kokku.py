# Vabandan, et ei teinud tsükliga, sest see oli praegu liiga keeruline
# Tõstsin riigid eraldi lehtedele ja lugesin sealt andmed välja



import xlrd
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("Kodutöö.xlsx", "Leht1")

df.plot(kind="line", x="Päev", y="Juhtumid",  color="blue")

plt.xlabel("Päevad")
plt.ylabel("Juhtumid")
plt.title("Autsria")

df.plot(kind="line", x="Päev", y="surnud", color="yellow")
#df.plot(kind="line", x="Päev", y="surnud", color="red")


plt.xlabel("Päevad")
plt.ylabel("surnud")
plt.title("Autsria")

df2 = pd.read_excel("Kodutöö.xlsx", "Leht3")

df2.plot(kind="line", x="Päev", y="Juhtumid",  color="blue")

plt.xlabel("Päevad")
plt.ylabel("Juhtumid")
plt.title("Brazil")


df2.plot(kind="line", x="Päev", y="surnud", color="red")

plt.xlabel("Päevad")
plt.ylabel("surnud")
plt.title("Brazil")


df3 = pd.read_excel("Kodutöö.xlsx", "Leht2")

df3.plot(kind="line", x="Päev", y="Juhtumid",  color="green")

plt.xlabel("Päevad")
plt.ylabel("Juhtumid")
plt.title("Bangladesh")

df3.plot(kind="line", x="Päev", y="surnud", color="yellow")

plt.xlabel("Päevad")
plt.ylabel("surnud")
plt.title("Bangladesh")




df4 = pd.read_excel("Kodutöö.xlsx", "Leht4")

df4.plot(kind="line", x="Päev", y="Juhtumid",  color="green")

plt.xlabel("Päevad")
plt.ylabel("Juhtumid")
plt.title("Hiina")


df4.plot(kind="line", x="Päev", y="surnud", color="orange")

plt.xlabel("Päevad")
plt.ylabel("surnud")
plt.title("Hiina")


df5 = pd.read_excel("Kodutöö.xlsx", "Leht5")

df5.plot(kind="line", x="Päev", y="Juhtumid",  color="green")

plt.xlabel("Päevad")
plt.ylabel("Juhtumid")
plt.title("Eesti")


df5.plot(kind="line", x="Päev", y="surnud", color="blue")

plt.xlabel("Päevad")
plt.ylabel("surnud")
plt.title("Eesti")


plt.show()