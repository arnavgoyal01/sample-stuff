from openpyxl import Workbook
from datetime import datetime
import os 
wb=Workbook()

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
ob = 0 
i1 = 0
e1 = 0 

def entry (counter,ob,i1,e1):
    counter=counter + 1 
    c=str(counter)
    now=datetime.now()
    ws1["".join(["A", c])]= now.strftime("%d/%m/%Y")
    ws1["".join(["B", c])]= now.strftime("%H/%M/%S")
    ws1["".join(["C", c])]= input("What is the category?")
    ws1["".join(["D", c])]= input("What is the description?")
    i= int(input("What is the income? (Press 0 if none)"))
    i1=i1+i 
    ws1["".join(["E", c])]= i
    e = int(input("What is the expense? (Press 0 if none)"))
    e1=e1+e 
    ws1["".join(["F", c])]= e
    ob=ob+i-e 
    ws1["".join(["G", c])]= ob
    d= str(counter +1)
    y= str(counter +4)
    z= str(counter + 5)
    w= "A{}:G{}".format(d,y)
    for row in ws1[w]:
        for cell in row: 
            cell.value =None 
    ws1["".join(["D", z])]= "Overall:"
    ws1["".join(["E", z])]= i1 
    ws1["".join(["F", z])]= e1
    ws1["".join(["G", z])]= ob 
    if (input("Enter New Entry?").upper())=="Y": 
        entry()
    else: 
        wb.save('Balance.xlsx')
        exit()  

f= (input("Would you like to add a new entry into balance sheet?\n")).upper()
if f=='Y': 
    entry (counter,ob,i1,e1)
else : 
    wb.save('Balance.xlsx')
    exit() 





