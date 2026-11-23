def clean_data(df):
    df = df.drop_duplicates()
    return df.reset_index(drop=True)