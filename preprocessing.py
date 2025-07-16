import pandas as pd

def preview_data(filepath = "data/fraudTrain.csv"):
    df = pd.read_csv(filepath)
    print("Data for training are loaded.", df.shape)
    print("Sample rows: ")
    print(df.head())
    return df

train_df = pd.read_csv('data/fraudTrain.csv')
test_df = pd.read_csv('data/fraudTest.csv')

