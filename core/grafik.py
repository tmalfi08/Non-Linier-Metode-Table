import matplotlib.pyplot as plt

def tampilkan_grafik(hasil):
    x_vals = [row[0] for row in hasil]
      y_vals = [row[1] for row in hasil]

    plt.figure(figsize=(9, 5))
    plt.plot(x_vals, y_vals, "o-b", label="f(x)")
 plt.axhline(0, color="red", linestyle="--")
    plt.axvline(0, color="black", linestyle="--", linewidth=0.7)

