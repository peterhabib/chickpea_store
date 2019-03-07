import django
django.setup()
import xlrd
import os
from database.models import Data_set


loc = ("/home/peter/Desktop/Django_videos/Tawfik_database/data_set/Chickpea seed in barrels(Terbol).xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)


# For row 0 and lumn 0
row = 1
for i in range(9803):
    try:

        # Reading......
        Barrel_No = sheet.cell_value(int(row), 0)
        Barrel_type = sheet.cell_value(int(row), 1)
        Trial_Name = sheet.cell_value(int(row), 2)
        Plot_No = sheet.cell_value(int(row), 3)

        # Adding...

        name = 'a' + str(i)
        name = Data_set(Barrel_No=Barrel_No, Barrel_type=Barrel_type, Plot_No=Plot_No, Trial_Name=Trial_Name)
        name.save()
        row += 1
        print('DONE!', row)
    except:
        pass
print('Done!')
