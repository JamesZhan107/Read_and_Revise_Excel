import xlrd
import xlwt

data = xlrd.open_workbook('待修改.xls（/xlsx）')

table = data.sheets()[0]
nrows = table.nrows  #行数
ncols = table.ncols  #列数

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')

for i in range(0,nrows):
    rowValues= table.row_values(i)  # 第i行数据
    for item in rowValues:
        item = str(item)
        newitem = 'PartA_'+ item
        sheet.write(i,1,newitem) #在1行1列写入bit

wbk.save('修改后.xls')
