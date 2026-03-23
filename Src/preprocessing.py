import pandas as pd


def load_data(path):
    df = pd.read_csv(path, sep="\t", header=None, names=["label", "message"])
    return df

def save_cleaned_data(df, path):
    df.to_csv(path, index=False)

    