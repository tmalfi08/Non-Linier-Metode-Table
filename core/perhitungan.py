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
