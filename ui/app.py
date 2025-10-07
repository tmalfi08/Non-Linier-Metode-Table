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



