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


plt.show()