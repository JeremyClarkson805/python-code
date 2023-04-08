import win32com.client as client
from win32com.client import constants
import os
print('Run')
# 新建一个Excel的应用程序
xl_app = client.gencache.EnsureDispatch("Excel.Application")

xl_app.Visible = True
curr_path = os.getcwd()
#打开第一个excel
path1 = r'%s\demo1.xlsx'%curr_path
wb = xl_app.Workbooks.Open(path1)
#打开第二个excel
path2 = r'%s\demo2.xlsx'%curr_path
wb2 = xl_app.Workbooks.Open(path2)
#选择要拷贝的excel内容
target_sht = wb2.Worksheets(1)
for sht in wb.Worksheets:
	if(sht.Name == 'Sheet1'):
		rng = sht.Range('A1:B55').Copy()#需要复制的表格的对角
		target_sht.Paste(Destination=target_sht.Range('C1'))#这里对应上面的第一个角
#关闭文档
wb.Close()
wb2.Save()
wb2.Close()