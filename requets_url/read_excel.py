import xlrd

def excel_to_list(data_file,sheet):
    data_list = []
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)
    header = sh.row_values(0)
    for i in range(1,sh.nrows):
        d = dict(zip(header,sh.row_values(i)))
        data_list.append(d)
    return data_list

if __name__ == '__main__':
    data_list = excel_to_list("D://PycharmProjects//url.xlsx","Sheet1")
    print(data_list)