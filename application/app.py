import pandas as pd


def csv_converter():
    df = pd.read_json(r'test_data.json')
    df.to_csv(r'test_data.csv', header=['Product Name', "Access Location", "Search Engine"])


if __name__ == '__main__':
    csv_converter()
