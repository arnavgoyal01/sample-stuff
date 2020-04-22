from openpyxl import Workbook
from datetime import datetime
import os 

wb=Workbook()
wb.save('Balance.xlsx')

ws1=wb.active 
ws1.title= "Balance"
ws1['A1']="Date"
ws1['B1']="Time"
ws1['C1']="Category"
ws1['D1']="Description"
ws1['E1']="Income"
ws1['F1']="Expense"
ws1['G1']="Overall Balance"
counter = 1 

f= (input("Would you like to add a new entry into balance sheet")).upper()
if f=='Y': 
    entry()
else : 
    exit() 

def entry ():
    counter++ 
    