import streamlit as st
import pandas as pd

# 1. Dataset Sederhana (Bisa dikembangkan ke CSV/Database)
gym_data = {
    "Otot Target": ["Dada", "Dada", "Punggung", "Punggung", "Kaki", "Kaki", "Bahu", "Bahu", "Lengan", "Lengan"],
    "Latihan": ["Bench Press", "Cable Fly", "Lat Pulldown", "Seated Row", "Leg Press", "Squat", "Overhead Press", "Lateral Raise", "Bicep Curl", "Tricep Pushdown"],
    "Alat Gym": ["Barbell/Bench", "Cable Machine", "Lat Machine", "Row Machine", "Leg Press Machine", "Smith Machine/Barbell", "Dumbbell/Barbell", "Dumbbell", "EZ Bar/Dumbbell", "Cable Machine"],
    "Tingkat Kesulitan": ["Menengah", "Pemula", "Pemula", "Pemula", "Pemula", "Lanjut", "Menengah", "Pemula", "Pemula", "Pemula"]
}

df = pd.DataFrame(gym_data)

# 2. Konfigurasi Halaman
st.set_page_config(page_title="AI Gym Recommender", page_icon="🏋️‍♂️")

st.title("🏋️‍♂️ Smart Gym Guide")
st.subheader("Rekomendasi Latihan Berdasarkan Target Otot")

# 3. Sidebar untuk Input Pengguna
st.sidebar.header("Pilih Profil Kamu")
target = st.sidebar.selectbox("Otot mana yang ingin dilatih?", df["Otot Target"].unique())
level = st.sidebar.radio("Level Pengalaman:", ["Pemula", "Menengah", "Lanjut"])

# 4. Logika Rekomendasi
# Memfilter data berdasarkan pilihan pengguna
rekomendasi = df[(df["Otot Target"] == target)]

# 5. Tampilan Utama
st.write(f"Menampilkan rekomendasi untuk otot **{target}**:")

if not rekomendasi.empty:
    for index, row in rekomendasi.iterrows():
        # Memberikan highlight jika level sesuai
        is_match = "✅ Sesuai Level" if row["Tingkat Kesulitan"] == level else "⚠️ Perlu Pendamping"
        
        with st.expander(f"Latihan: {row['Latihan']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Alat:** {row['Alat Gym']}")
            with col2:
                st.write(f"**Kesulitan:** {row['Tingkat Kesulitan']}")
            st.info(f"Status: {is_match}")
else:
    st.warning("Maaf, belum ada data untuk kombinasi tersebut.")

# 6. Fitur Tambahan: Kalkulator BMI (Sistem Cerdas Sederhana)
st.divider()
st.subheader("🔢 Cek Status Tubuh (BMI)")
with st.container():
    berat = st.number_input("Berat Badan (kg)", min_value=30.0, value=70.0)
    tinggi = st.number_input("Tinggi Badan (cm)", min_value=100.0, value=170.0)
    
    if st.button("Hitung BMI"):
        bmi = berat / ((tinggi/100) ** 2)
        st.write(f"Skor BMI Anda: **{bmi:.2f}**")
        if bmi < 18.5:
            st.error("Kategori: Kekurangan Berat Badan")
        elif 18.5 <= bmi < 25:
            st.success("Kategori: Normal (Ideal)")
        else:
            st.warning("Kategori: Kelebihan Berat Badan")