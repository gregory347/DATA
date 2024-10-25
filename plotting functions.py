import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data('/LINEAR REGRESSION/data/accidents-database-.csv'):
    """Load CSV data into a pandas DataFrame."""
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

def plot_histogram(df, column):
    """Plot a histogram of the specified column."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], bins=30, kde=True)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig(f"{column}_histogram.png")
    plt.show()

def plot_boxplot(df, column):
    """Plot a boxplot of the specified column."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(y=df[column])
    plt.title(f"Boxplot of {column}")
    plt.ylabel(column)
    plt.grid(True)
    plt.savefig(f"{column}_boxplot.png")
    plt.show()

def plot_correlation_matrix(df):
    """Plot a correlation matrix of the DataFrame."""
    plt.figure(figsize=(12, 10))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    plt.title("Correlation Matrix")
    plt.savefig("correlation_matrix.png")
    plt.show()

def main():
    file_path = input("Enter the path to the CSV file: ")
    df = load_data(file_path)
    
    if df is not None:
        print("\nAvailable columns:")
        print(df.columns.tolist())

        column = input("\nEnter a column name for the histogram: ")
        if column in df.columns:
            plot_histogram(df, column)
        else:
            print(f"Error: '{column}' is not a valid column.")

        column = input("\nEnter a column name for the boxplot: ")
        if column in df.columns:
            plot_boxplot(df, column)
        else:
            print(f"Error: '{column}' is not a valid column.")

        plot_correlation_matrix(df)

if __name__ == "__main__":
    main()
