import pandas as pd

def check_missing_data(file_path):
    """Check for missing data in the given CSV file."""
    try:
        df = pd.read_csv(file_path)

        print(f"Data loaded successfully. Shape: {df.shape}")
     
        missing_data = df.isnull().sum()
       
        missing_summary = missing_data[missing_data > 0]

        if not missing_summary.empty:
            print("\nMissing Data Summary:")
            print(missing_summary)
        else:
            print("\nNo missing data found.")

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: There was an issue parsing the file.")

def main():
    file_path = input("Enter the path to the CSV file: ")
    check_missing_data(file_path)

if __name__ == "__main__":
    main()
