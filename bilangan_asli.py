import streamlit as st
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# ---------- ALGORITHMS ----------
def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_recursive(n):
    if n == 1:
        return n
    else:
        return n + sum_recursive(n - 1)

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
st.title("🧮 Kajian Efisiensi Proses Akumulasi Bilangan Asli Berurutan Menggunakan Pendekatan Iteratif dan Rekursif")

# ---------- TEAM SECTION ----------
st.subheader("👥 Anggota Tim IF-48-05")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Nama:** ANNISA ROSLINA ANWAR")
    st.write("**NIM:** 103012430064")

with col2:
    st.write("**Nama:** HASNAT FERDIANANDA")
    st.write("**NIM:** 103012430038")

with col3:
    st.write("**Nama:** RASYID RIDLO")
    st.write("**NIM:** 103012400042")

st.markdown("---")

st.markdown("### Studi Kasus: 💼 Penyelesaian Sprint dalam Manajemen Proyek")
st.code('''
Proyek software dengan sprint bertambah kompleksitas:
- Sprint 1: 1 fitur selesai
- Sprint 2: 2 fitur selesai
- Sprint 3: 3 fitur selesai
...
- Sprint n: n fitur selesai

Total fitur setelah n sprint = 1 + 2 + 3 + ... + n
    ''', language='comment')
st.markdown("Contoh: Setelah 12 sprint = 78 fitur delivered")

st.markdown("---")

st.info("ℹ️ Membandingkan efisiensi dua versi algoritma penjumlahan bilangan asli iteratif (O(n)) dan rekursif (O(n)).")

# Input widget (graphical)
n = st.number_input(
    "Masukkan ukuran masukan (n):",
    min_value=1,
    value=500,
    step=1,
    help="Nilai n > 5000 dapat menyebabkan stack overflow pada rekursif."
)

# Run button
if st.button("Jalankan Algoritma"):
    # Validate input before running
    if n > 5000:
        st.error("❌ Nilai n terlalu besar! Maksimal n = 5000 untuk menghindari stack overflow pada rekursif.")
        st.warning("💡 Tip: Gunakan nilai n ≤ 5000 untuk hasil yang optimal.")
    else:
        try:
            # Iterative
            res_it, time_it = measure_time(sum_iterative, n)
            st.success(f"✅ **Iteratif**: Σ(1 hingga {n}) = {res_it} | Waktu = {time_it:.4f} ms")
            
            # Recursive
            res_rec, time_rec = measure_time(sum_recursive, n)
            st.error(f"🔁 **Rekursif**: Σ(1 hingga {n}) = {res_rec} | Waktu = {time_rec:.4f} ms")
            
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
if st.checkbox("Tampilkan grafik runtime (n = 1 hingga 500)"):
    with st.spinner("Menghitung runtime... (mohon tunggu)"):
        ns = list(range(1, 501, 50))  # 1, 51, 101, 151, ..., 451
        it_times = []
        rec_times = []
        
        for n_val in ns:
            _, t_it = measure_time(sum_iterative, n_val)
            try:
                _, t_rec = measure_time(sum_recursive, n_val)
            except RecursionError:
                t_rec = None
            it_times.append(t_it)
            rec_times.append(t_rec if t_rec is not None else 0)
        
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        ax2.plot(ns, it_times, "o-", label="Iteratif", color="green")
        ax2.plot(ns, rec_times, "x--", label="Rekursif", color="red")
        ax2.set_xlabel("Nilai n")
        ax2.set_ylabel("Waktu (ms)")
        ax2.set_title("Runtime vs Input Size")
        ax2.legend()
        ax2.grid(True, which="both", linestyle="--", linewidth=0.5)
        st.pyplot(fig2)

# Show algorithm code
st.markdown("---")
st.subheader("💻 Source Code Algoritma")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Algoritma Iteratif**")
    st.code('''
def iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
    ''', language='python')

with col2:
    st.markdown("**Algoritma Rekursif**")
    st.code('''
def recursive(n):
    if n == 1:
        return n
    else:
        return n + recursive(n - 1)
    ''', language='python')