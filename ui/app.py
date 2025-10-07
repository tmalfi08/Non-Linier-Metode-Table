import tkinter as tk
from tkinter import messagebox
from core.perhitungan import hitung_metode_tabel, hasil
from core.grafik import tampilkan_grafik
from tabulate import tabulate

def start_app():
    root = tk.Tk()
    root.title("Metode Tabel - Kelompok 1")
    root.geometry("650x750")
    root.configure(bg="#ECECEC")

     def jalankan():
        try:
            expr = input_fungsi.get()
            N = int(entry_n.get())
            bawah = float(entry_bawah.get())
            atas = float(entry_atas.get())

            df, iterasi, x_terpilih = hitung_metode_tabel(expr, N, bawah, atas)

            box_hasil.delete(1.0, tk.END)
            tabel_str = tabulate(df, headers="keys", floatfmt=".5f", numalign="center")
            box_hasil.insert(tk.END, tabel_str)

            if iterasi is not None:
                box_hasil.insert(tk.END, f"\n\nDitemukan pada iterasi ke-{iterasi}, x ≈ {x_terpilih:.5f}")
            else:




