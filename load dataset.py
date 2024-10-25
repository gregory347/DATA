import pandas as pd

def load_dataset(file_path):
    """Load a dataset from a CSV file."""
    try:
        df = pd.read_csv('/LINEAR REGRESSION/data/accidents-database-.csv')
        print(f"Data loaded successfully. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: The file {'/LINEAR REGRESSION/data/accidents-database-.csv'} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was an issue parsing the file.")
        return None

def explore_data(df):
    """Perform basic exploration of the dataset."""
    if df is not None:
        print("\nBasic Data Exploration:")
        print(f"Columns: {df.columns.tolist()}")
        print(f"Data Types:\n{df.dtypes}")
        print(f"First 5 Rows:\n{df.head()}")
        print(f"Missing Values:\n{df.isnull().sum()}")
        print(f"Summary Statistics:\n{df.describe()}")

def main():
    file_path = input("Enter the path to the CSV file: ")
    df = load_dataset(file_path)
    explore_data(df)

if __name__ == "__main__":
    main()

