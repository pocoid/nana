# Import pustaka yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengimpor dataset Air Quality
data = pd.read_csv('air_quality.csv')

# Menyusun tampilan dashboard dengan Streamlit
st.title('Analisis Kualitas Udara')

# Menambahkan pilihan lokasi dan parameter
lokasi = st.selectbox('Pilih Lokasi:', data['station'].unique())
parameter = st.selectbox('Pilih Parameter:', data.columns[5:])  # Sesuaikan dengan kolom yang sesuai dengan parameter

# Menampilkan data terpilih
st.subheader(f'Data Kualitas Udara untuk {lokasi}')
filtered_data = data[data['station'] == lokasi]
st.write(filtered_data)

# Visualisasi data
st.subheader('Visualisasi Data')

# Time Series Plot untuk perubahan kualitas udara dari tahun ke tahun
plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y=parameter, data=filtered_data)
plt.title(f'Perubahan Kualitas Udara ({parameter}) di {lokasi} dari Tahun ke Tahun')
st.pyplot()

# Scatter Plot untuk korelasi antara polusi udara dan suhu udara
plt.figure(figsize=(10, 6))
sns.scatterplot(x='TEMP', y=parameter, data=filtered_data)  # Sesuaikan dengan kolom suhu
plt.title(f'Korelasi antara {parameter} dan Suhu Udara di {lokasi}')
st.pyplot()

# Kesimpulan
st.subheader('Kesimpulan')
st.write('Dalam analisis ini, kami telah menjawab dua pertanyaan bisnis:')
st.write('1. Bagaimana pola perubahan kualitas udara selama beberapa tahun terakhir?')
st.write('2. Apakah ada korelasi antara tingkat polusi udara dengan suhu udara?')

# Menjalankan Streamlit
if __name__ == '__main__':
    st.write('Proyek Analisis Data Air Quality')
