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
            box_hasil.insert(tk.END, "\n\nTidak ada iterasi yang memenuhi kondisi.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def tampilkan():
        if not hasil["tabel"]:
            messagebox.showwarning("Peringatan", "Belum ada data! Silakan hitung dulu.")
        else:
            tampilkan_grafik(hasil["tabel"])
# UI
    judul = tk.Label(root, text="Kalkulator Metode Tabel", font=("Arial", 18, "bold"), bg="#ECECEC", fg="#222")
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

    


