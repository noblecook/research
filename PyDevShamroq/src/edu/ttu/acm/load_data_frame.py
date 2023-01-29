import time
import pandas as pd
fileName = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/src/edu/ttu/acm/gold-data-set/dataset-TEMP-cfr_16_312_005.csv"


def main():
    # Read the Excel file and store the data in a dataframe
    # df = pd.read_excel('file.xlsx')
    df = pd.read_csv(fileName)

    # Retrieve a completion column and store the values in a list
    column_name = 'completion'
    column_values = df[column_name].tolist()
    for line in column_values:
        print(type(line))
        time.sleep(2000)


if __name__ == '__main__':
    main()