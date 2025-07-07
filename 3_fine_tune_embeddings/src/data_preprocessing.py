import pandas as pd

def load_data(file_path):
    """
    Loads data from a CSV file.
    In a real scenario, this would involve more complex preprocessing.
    """
    print(f"Loading data from {file_path}...")
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None

if __name__ == '__main__':
    # Example of how to use this module
    df = load_data('data/dummy_sales_calls.csv')
    if df is not None:
        print("First 5 rows of the data:")
        print(df.head()) 