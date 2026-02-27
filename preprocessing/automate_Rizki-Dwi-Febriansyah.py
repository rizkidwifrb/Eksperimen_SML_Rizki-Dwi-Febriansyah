import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_data(path):
    return pd.read_csv(path)


def preprocessing(df):

    df.fillna(df.mean(numeric_only=True), inplace=True)

    le = LabelEncoder()
    cat_cols = df.select_dtypes(include='object').columns

    for col in cat_cols:
        df[col] = le.fit_transform(df[col])

    scaler = StandardScaler()
    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = scaler.fit_transform(df[num_cols])

    return df


def save_data(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)


def main():

    BASE_DIR = os.getcwd()

    input_path = os.path.join(BASE_DIR,
                              "dataset_raw",
                              "data.csv")

    output_path = os.path.join(BASE_DIR,
                               "preprocessing",
                               "dataset_preprocessing",
                               "data_clean.csv")

    df = load_data(input_path)
    df_clean = preprocessing(df)
    save_data(df_clean, output_path)

    print("✅ Workflow preprocessing berhasil!")


if __name__ == "__main__":
    main()