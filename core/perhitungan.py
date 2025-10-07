import numpy as np
import pandas as pd
from tabulate import tabulate

hasil = {"tabel": []}

def eval_fungsi(expr, x):
    return eval(expr, {"np": np, "x": x})

def hitung_metode_tabel(expr, N, bawah, atas):
    h = (atas - bawah) / N
    hasil["tabel"].clear()

    iterasi_terpilih, x_terpilih = None, None
    
    for i in range(N + 1):

    for i in range(N + 1):
        xi = bawah + i * h
        fxi = eval_fungsi(expr, xi)
        fxi_next = eval_fungsi(expr, xi + h) if i < N else None
        perkalian = fxi * fxi_next if fxi_next is not None else None

        hasil["tabel"].append([xi, fxi, fxi_next, perkalian])
