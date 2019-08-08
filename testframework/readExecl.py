import xlrd

path = "testdata.xlsx"


with xlrd.open_workbook(path) as workbook:
    print(workbook.sheet_names())
    Data_sheet = workbook.sheets()[0]
    print(Data_sheet.name)
    print(Data_sheet.nrows)
    print(Data_sheet.ncols)