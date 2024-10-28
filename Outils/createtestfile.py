import openpyxl
import os
import win32com.client as win32

# Step 1: Create an Excel file with openpyxl
data_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Data'))
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Test file"
sheet["A1"] = "Mot de passe trouvé."

# Save the Excel file without a password
temp_file = "temp_testfile.xlsx"
workbook.save(temp_file)

# Step 2: Add password protection using pywin32
excel = win32.Dispatch('Excel.Application')
wb = excel.Workbooks.Open(os.path.abspath(temp_file))
wb.SaveAs(os.path.join(data_folder_path, "testfile.xlsx"), Password='Cacatombes18')
wb.Close()
excel.Quit()

# Optional: Remove the temporary file
os.remove(temp_file)

print("Excel file 'testfile.xlsx' created with password protection.")
