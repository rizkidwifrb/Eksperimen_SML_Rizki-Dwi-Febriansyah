import pandas as pd
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# LOAD DATA
def load_data(path):
    df = pd.read_csv(path)
    return df


# PREPROCESSING
def preprocessing(df):

    # Handle missing value
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Encoding categorical column
    le = LabelEncoder()
    cat_cols = df.select_dtypes(include='object').columns

    for col in cat_cols:
        df[col] = le.fit_transform(df[col])

    # Scaling numerical data
    scaler = StandardScaler()
    num_cols = df.select_dtypes(include='number').columns

    df[num_cols] = scaler.fit_transform(df[num_cols])

    return df


# SAVE DATA
def save_data(df, output_path):

    os.makedirs(os.path.dirname(output_path),
                exist_ok=True)

    df.to_csv(output_path, index=False)


# MAIN PIPELINE
def main():

    input_path = "dataset_raw/data.csv"
    df = pd.read_csv(input_path)

    print(df.head())
    output_path = "dataset_preprocessing/data_clean.csv"

    df = load_data(input_path)

    df_clean = preprocessing(df)

    save_data(df_clean, output_path)

    print("✅ Preprocessing selesai!")
    print(f"Dataset tersimpan di: {output_path}")
    print("Workflow preprocessing berhasil dijalankan!")


if __name__ == "__main__":
    main()