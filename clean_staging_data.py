import pandas as pd
from project import STAGING_DATA_PATH, DATA_DIR


def clean_data(filepath):
    """
    Remove commas & whitespace in salary column:
    """
    df = pd.read_csv(filepath)
    df = df.copy()
    # change columns to lowercase
    df.columns = df.columns.str.lower()
    # remove commas
    df['salary'] = df['salary'].apply(lambda row: row.replace(',', ''))
    return df


def save_dataframe(df, path_to_save):
    """
    Save the clean dataframe to appropriate path
    """
    df.to_csv(path_to_save, index=False)


def main():
    """
    Remove commas in salary column & save to data directory
    """
    df = clean_data(STAGING_DATA_PATH)
    save_dataframe(df, DATA_DIR/'clean_hr_data.csv')


if __name__ == '__main__':
    main()
