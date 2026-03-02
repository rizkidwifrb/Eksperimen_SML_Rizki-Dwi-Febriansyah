import pandas as pd
from sklearn.preprocessing import StandardScaler
import os


def preprocess_data(input_path, output_path):
    """
    Fungsi untuk memuat, melakukan preprocessing,
    dan menyimpan dataset Student Performance
    """

    # Membuat folder output jika belum ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # ======================
    # LOAD DATA
    # ======================
    df = pd.read_csv(input_path)

    print("Dataset berhasil dimuat")
    print(df.head())

    # ======================
    # DATA CLEANING
    # ======================
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # ======================
    # ENCODING DATA KATEGORIKAL
    # ======================
    df["Extracurricular Activities"] = df[
        "Extracurricular Activities"
    ].map({
        "Yes": 1,
        "No": 0
    })

    # ======================
    # FEATURE ENGINEERING
    # ======================
    df["study_efficiency"] = (
        df["Hours Studied"] /
        (df["Sleep Hours"] + 1)
    )

    # ======================
    # SCALING DATA NUMERIK
    # ======================
    scaler = StandardScaler()

    numerical_cols = [
        "Hours Studied",
        "Previous Scores",
        "Sleep Hours",
        "Sample Question Papers Practiced",
        "study_efficiency"
    ]

    df[numerical_cols] = scaler.fit_transform(
        df[numerical_cols]
    )

    # ======================
    # SAVE HASIL
    # ======================
    df.to_csv(output_path, index=False)

    print(f"\nData preprocessing berhasil disimpan di: {output_path}")


# ======================
# MAIN PROGRAM
# ======================
if __name__ == "__main__":

    raw_data_path = "../Student_Performance raw/Student_Performance.csv"

    processed_data_path = (
        "Student_Performance_preprocessing/"
        "student_performance_processed.csv"
    )

    preprocess_data(raw_data_path, processed_data_path)