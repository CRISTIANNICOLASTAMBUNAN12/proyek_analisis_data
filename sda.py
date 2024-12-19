import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Fungsi untuk menampilkan Descriptive Statistics
def display_descriptive_statistics(df):
    st.subheader("Descriptive Statistics")
    desc_stats = df[["jml_penyaluran", "jml_outstanding", "rencana_kredit", "jml_debitur"]].describe()
    st.write(desc_stats)

# Fungsi untuk menampilkan Missing Values
def display_missing_values(df):
    st.subheader("Missing Values")
    missing_values = df.isnull().sum()
    st.write(missing_values)

# Fungsi untuk membuat grafik penyaluran per bulan
def plot_penyaluran_per_bulan(df):
    st.subheader("Grafik Jumlah Penyaluran per Bulan")
    penyaluran_per_bulan = df.groupby("bulan")["jml_penyaluran"].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(penyaluran_per_bulan.index, penyaluran_per_bulan.values, color="skyblue", edgecolor="black")
    ax.set_title("Jumlah Penyaluran per Bulan di Tahun 2024")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penyaluran")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

# Fungsi untuk membuat scatter plot
def plot_scatter(df):
    st.subheader("Scatter Plot: Penyaluran vs Outstanding")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["jml_penyaluran"], df["jml_outstanding"], color="green")
    ax.set_title("Penyaluran vs Outstanding")
    ax.set_xlabel("Penyaluran")
    ax.set_ylabel("Outstanding")
    st.pyplot(fig)

# Fungsi untuk membuat grafik penyaluran per skema
def plot_penyaluran_per_skema(df):
    st.subheader("Grafik Penyaluran per Skema")
    penyaluran_per_skema = df.groupby("skema")["jml_penyaluran"].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(penyaluran_per_skema.values, labels=penyaluran_per_skema.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Distribusi Penyaluran per Skema Kredit")
    plt.tight_layout()
    st.pyplot(fig)

# Fungsi untuk membuat histogram
def plot_histogram(df):
    st.subheader("Histogram: Distribusi Penyaluran Kredit")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df["jml_penyaluran"], bins=20, color="skyblue", edgecolor="black")
    ax.set_title("Distribusi Penyaluran Kredit")
    ax.set_xlabel("Jumlah Penyaluran")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)

def display_outlier_analysis(df):
    st.subheader("Analisis Outlier Penyaluran Kredit")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x="jml_penyaluran", ax=ax, color="orange")
    ax.set_title("Identifikasi Outlier Penyaluran Kredit")
    st.pyplot(fig)

def display_top_5_wilayah(df):
    st.subheader("Top 5 Wilayah dengan Penyaluran Tertinggi")
    top_5_wilayah = df.groupby("nama_wilayah")["jml_penyaluran"].sum().sort_values(ascending=False).head(5)
    st.bar_chart(top_5_wilayah)


def display_ratio_penyaluran_outstanding(df):
    st.subheader("Rasio Penyaluran terhadap Outstanding")
    df["ratio_penyaluran_outstanding"] = df["jml_penyaluran"] / df["jml_outstanding"]
    st.dataframe(df[["nama_wilayah", "jml_penyaluran", "jml_outstanding", "ratio_penyaluran_outstanding"]])

# Fungsi untuk membuat boxplot
def plot_boxplot(df):
    st.subheader("Boxplot: Distribusi Penyaluran Kredit")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x="jml_penyaluran", color="lightgreen", ax=ax)
    ax.set_title("Distribusi Penyaluran Kredit (Boxplot)")
    st.pyplot(fig)

def plot_penyaluran_geografis(df):
    st.subheader("Penyaluran Kredit Berdasarkan Wilayah (Peta)")
    fig = px.scatter_geo(
        df,
        locations="kode_provinsi",
        locationmode="ISO-3",
        size="jml_penyaluran",
        color="nama_provinsi",
        hover_name="nama_provinsi",
        title="Penyaluran Kredit Berdasarkan Provinsi",
    )
    st.plotly_chart(fig)

def plot_penyaluran_per_bank(df):
    st.subheader("Distribusi Penyaluran Kredit per Bank")
    penyaluran_per_bank = df.groupby("nama_bank")["jml_penyaluran"].sum()
    fig, ax = plt.subplots(figsize=(12, 6))
    penyaluran_per_bank.plot(kind="bar", color="purple", edgecolor="black", ax=ax)
    ax.set_title("Distribusi Penyaluran Kredit per Bank")
    ax.set_xlabel("Bank")
    ax.set_ylabel("Jumlah Penyaluran")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
def plot_trend_penyaluran_per_provinsi(df):
    st.subheader("Trend Penyaluran Kredit per Provinsi")
    trend_penyaluran = df.groupby(["nama_provinsi", "bulan"])["jml_penyaluran"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=trend_penyaluran, x="bulan", y="jml_penyaluran", hue="nama_provinsi", ax=ax)
    ax.set_title("Trend Penyaluran Kredit per Provinsi")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penyaluran")
    plt.legend(title="Provinsi", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(fig)
# Fungsi untuk membuat heatmap korelasi
def plot_heatmap(df):
    st.subheader("Heatmap Korelasi Antar Variabel")
    corr = df[["jml_penyaluran", "jml_outstanding", "rencana_kredit", "jml_debitur"]].corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax, fmt=".2f", linewidths=0.5)
    ax.set_title("Korelasi Antar Variabel")
    st.pyplot(fig)


# Menampilkan header aplikasi
st.write(
    """
    # Analisis Penyaluran Kredit
    Aplikasi ini menampilkan grafik analisis penyaluran kredit berdasarkan data yang dimiliki.
    """
)

# Load data dari file Excel
df = pd.read_excel("workhome.xlsx")

# Ganti nama kolom menjadi huruf kecil untuk konsistensi
df.columns = df.columns.str.lower()

# Filter data berdasarkan tahun 2024
df_filtered = df[df["tahun"] == 2024]

# Menampilkan tabel untuk referensi
st.dataframe(df_filtered)

# Menampilkan Descriptive Statistics
display_descriptive_statistics(df_filtered)

# Menampilkan Missing Values
display_missing_values(df_filtered)

# Menampilkan grafik Jumlah Penyaluran per Bulan
plot_penyaluran_per_bulan(df_filtered)

# Scatter Plot untuk EDA lebih lanjut
plot_scatter(df_filtered)

display_outlier_analysis(df_filtered)

display_ratio_penyaluran_outstanding(df_filtered)

plot_penyaluran_per_bank(df_filtered)

plot_penyaluran_geografis(df_filtered)

# Filter interaktif berdasarkan Provinsi
st.subheader("Filter berdasarkan Provinsi")
provinsi_selected = st.selectbox("Pilih Provinsi", df_filtered["nama_provinsi"].unique())
df_provinsi_filtered = df_filtered[df_filtered["nama_provinsi"] == provinsi_selected]
st.dataframe(df_provinsi_filtered)

# Menampilkan grafik Penyaluran per Skema
plot_penyaluran_per_skema(df_filtered)

# Menampilkan grafik Histogram
plot_histogram(df_filtered)

display_top_5_wilayah(df_filtered)

plot_trend_penyaluran_per_provinsi(df_filtered)

# Menampilkan grafik Boxplot
plot_boxplot(df_filtered)

# Menampilkan grafik Heatmap Korelasi
plot_heatmap(df_filtered)

# Menampilkan informasi nama pengguna
st.text("Nama: Cristian Nicolas Tambunan")
