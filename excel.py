import openpyxl
from openpyxl import Workbook, load_workbook

wb = load_workbook('C2-W3-Practice-Challenge.xlsx')
ws = wb.active
print(ws)




