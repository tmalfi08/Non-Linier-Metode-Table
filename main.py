import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Penyimpanan hasil perhitungan
hasil = {"tabel": []}

# Evaluasi fungsi dengan namespace numpy
def eval_fungsi(x):
    try:
        expr = input_fungsi.get()
        return eval(expr, {"np": np, "x": x})
    except Exception as e:
        messagebox.showerror("Error Evaluasi", f"Kesalahan evaluasi fungsi:\n{e}")
        return None

# Fungsi utama perhitungan metode tabel
def jalankan_perhitungan():
    try:
        N = int(entry_n.get())
        bawah = float(entry_bawah.get())
        atas = float(entry_atas.get())
        h = (atas - bawah) / N

        hasil["tabel"].clear()
        iterasi_terpilih, x_terpilih = None, None

        for i in range(N + 1):
            xi = bawah + i * h
            fxi = eval_fungsi(xi)
            fxi_next = eval_fungsi(xi + h) if i < N else None
            perkalian = fxi * fxi_next if fxi_next is not None else None

            hasil["tabel"].append([xi, fxi, fxi_next, perkalian])

            if iterasi_terpilih is None and fxi is not None and fxi_next is not None:
                if abs(fxi) < abs(fxi_next):
                    iterasi_terpilih, x_terpilih = i, xi

        df = pd.DataFrame(hasil["tabel"], 
                          columns=["xi", "f(xi)", "f(x(i+1))", "f(xi)*f(x(i+1))"])

        # Tampilkan hasil di TextBox
        box_hasil.delete(1.0, tk.END)
        tabel_str = tabulate(df, headers="keys", floatfmt=".5f", numalign="center")
        box_hasil.insert(tk.END, tabel_str)

        if iterasi_terpilih is not None:
            box_hasil.insert(tk.END, f"\n\nDitemukan pada iterasi ke-{iterasi_terpilih}, x ≈ {x_terpilih:.5f}")
        else:
            box_hasil.insert(tk.END, "\n\nTidak ada iterasi yang memenuhi kondisi |f(xk)| < |f(xk+1)|.")

    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# Plot hasil
def tampilkan_grafik():
    if not hasil["tabel"]:
        messagebox.showwarning("Peringatan", "Belum ada data! Silakan hitung dulu.")
        return

    x_vals = [row[0] for row in hasil["tabel"]]
    y_vals = [row[1] for row in hasil["tabel"]]

    plt.figure(figsize=(9, 5))
    plt.plot(x_vals, y_vals, "o-b", label="f(x)")
    plt.axhline(0, color="red", linestyle="--")
    plt.axvline(0, color="black", linestyle="--", linewidth=0.7)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Grafik Fungsi")
    plt.grid(True)
    plt.legend()
    plt.show()

# ================= GUI =================
root = tk.Tk()
root.title("Metode Tabel - Kelompok 1")
root.geometry("650x750")
root.configure(bg="#ECECEC")

judul = tk.Label(root, text="Kalkulator Metode Tabel", 
                 font=("Arial", 18, "bold"), bg="#ECECEC", fg="#222")
judul.pack(pady=15)

frame = tk.Frame(root, bg="white", relief="groove", borderwidth=2)
frame.pack(padx=15, pady=10, fill="x")

tk.Label(frame, text="f(x):", bg="white").grid(row=0, column=0, sticky="w", padx=5, pady=5)
input_fungsi = tk.Entry(frame, width=35)
input_fungsi.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Jumlah Langkah (N):", bg="white").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_n = tk.Entry(frame, width=10)
entry_n.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Batas Bawah:", bg="white").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_bawah = tk.Entry(frame, width=10)
entry_bawah.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Batas Atas:", bg="white").grid(row=3, column=0, sticky="w", padx=5, pady=5)
entry_atas = tk.Entry(frame, width=10)
entry_atas.grid(row=3, column=1, padx=5, pady=5)

btn_hitung = tk.Button(root, text="Proses Perhitungan", command=jalankan_perhitungan, 
                       bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
btn_hitung.pack(pady=8)

btn_plot = tk.Button(root, text="Tampilkan Grafik", command=tampilkan_grafik, 
                     bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
btn_plot.pack(pady=5)

frame_hasil = tk.Frame(root, bg="white", relief="solid", borderwidth=1)
frame_hasil.pack(padx=15, pady=15, fill="both", expand=True)

box_hasil = tk.Text(frame_hasil, font=("Consolas", 10), bg="#FDFDFD")
box_hasil.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()
