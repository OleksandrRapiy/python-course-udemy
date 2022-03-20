import pandas

CSV_FILE_PATH = 'files/tems_data.csv'

CSV_FILE_PATH_MONEY_MANAGER = 'files/spent_money.csv'

csv_file = pandas.read_csv(CSV_FILE_PATH)
# print(csv_file.mean())

csv_file_money = pandas.read_csv(CSV_FILE_PATH_MONEY_MANAGER)
print(f'Balance: {csv_file_money.sum(numeric_only=True)["Amount"]}')