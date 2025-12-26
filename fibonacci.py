import streamlit as st
import time

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

# ---------- ALGORITHMS ----------
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# ---------- TIMING HELPER ----------
def measure_time(func, n, trials=3):
    times = []
    for _ in range(trials):
        start = time.perf_counter()
        result = func(n)
        end = time.perf_counter()
        times.append((end - start) * 1000)
    return result, sum(times) / len(times)

# ---------- STREAMLIT APP ----------
st.set_page_config(page_title="Tubes - Analisis Kompleksitas Algoritma", layout="centered")
st.title("🌐 Aplikasi Perbandingan Algoritma Iteratif vs Rekursif")
st.markdown("### Studi Kasus: Menghitung Bilangan Fibonacci ke-n")

st.info("ℹ️ Aplikasi ini membandingkan efisiensi dua versi algoritma Fibonacci: iteratif (O(n)) dan rekursif (O(2ⁿ)).")

# Input widget (graphical)
n = st.number_input(
    "Masukkan ukuran masukan (n):",
    min_value=0,
    max_value=35,
    value=10,
    step=1,
    help="Nilai n > 35 akan menyebabkan rekursif sangat lambat atau crash."
)

# Run button
if st.button("Jalankan Algoritma"):
    try:
        # Iterative
        res_it, time_it = measure_time(fib_iterative, n)
        st.success(f"✅ **Iteratif**: F({n}) = {res_it} | Waktu = {time_it:.4f} ms")

        # Recursive
        if n > 35:
            st.warning("⚠️ Rekursif tidak disarankan untuk n > 35.")
        res_rec, time_rec = measure_time(fib_recursive, n)
        st.error(f"🔁 **Rekursif**: F({n}) = {res_rec} | Waktu = {time_rec:.4f} ms")

        # Bar chart
        st.subheader("📊 Perbandingan Waktu Eksekusi")
        fig, ax = plt.subplots()
        ax.bar(["Iteratif", "Rekursif"], [time_it, time_rec], color=["green", "red"])
        ax.set_ylabel("Waktu (milidetik)")
        ax.set_title(f"n = {n}")
        for i, v in enumerate([time_it, time_rec]):
            ax.text(i, v + max(time_it, time_rec) * 0.02, f"{v:.6f} ms", ha="center")
        st.pyplot(fig)

    except RecursionError:
        st.error("❌ Kedalaman rekursi terlampaui. Coba nilai n yang lebih kecil!")
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan: {e}")

# Optional full graph
st.markdown("---")
st.subheader("📈 Grafik Perbandingan untuk Berbagai Nilai n")
if st.checkbox("Tampilkan grafik runtime (n = 1 hingga 30)"):
    with st.spinner("Menghitung runtime... (mohon tunggu)"):
        ns = list(range(5, 31, 5))
        it_times = []
        rec_times = []

        for n_val in ns:
            _, t_it = measure_time(fib_iterative, n_val)
            try:
                _, t_rec = measure_time(fib_recursive, n_val)
            except RecursionError:
                t_rec = None
            it_times.append(t_it)
            rec_times.append(t_rec if t_rec is not None else 0)

        fig2, ax2 = plt.subplots(figsize=(8, 4))
        ax2.plot(ns, it_times, "o-", label="Iteratif", color="green")
        ax2.plot(ns, rec_times, "x--", label="Rekursif", color="red")
        ax2.set_xlabel("Nilai n")
        ax2.set_ylabel("Waktu (ms)")
        ax2.set_yscale("log")
        ax2.set_title("Runtime vs Input Size (Skala Logaritmik)")
        ax2.legend()
        ax2.grid(True, which="both", linestyle="--", linewidth=0.5)
        st.pyplot(fig2)
        st.caption("Catatan: Skala logaritmik digunakan agar perbedaan tetap terlihat jelas.")