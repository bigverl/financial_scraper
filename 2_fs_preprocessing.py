import os
import tika
import openpyxl
from tika import parser

# Part 1: Create and configure excel workbook
# Change current working directory to file location
absPath = os.path.abspath(__file__)
dirName = os.path.dirname(absPath)
os.chdir(dirName + '\\Financial_Scraper\\final_xlsx_output')

print(os.getcwd())

# Open workbook
wb = openpyxl.Workbook()

# Alter default sheet
rSheet = wb['Sheet']
rSheet.title = 'Revenues'
rSheet['A1'] = 'Date'
rSheet['B1'] = 'Description'
rSheet['C1'] = 'Deposit Amount'

# Create and name sheet
eSheet = wb.create_sheet()
eSheet.title = 'Expenses'
eSheet['A1'] = 'Date'
eSheet['B1'] = 'Description'
eSheet['C1'] = 'Charge Amount'

# Format amount column ‘Currency’
col = eSheet.column_dimensions['C']
col.number_format = 'General'

col = rSheet.column_dimensions['C']
col.number_format = 'General'

# Save newly-created spreadsheet
wb.save('final_output.xlsx')

# Part 2: Combine PDFs
# Change directory to pdf location
os.chdir('..\\put_pdfs_here')

# Pull text from pdf
text = ''
for i in range(1,13):
    raw = parser.from_file('wc' + str(i) + '.pdf')
    text = text + raw['content']

# Part 3: Write all data to text file
# Change directory to text file data folder
os.chdir('..\\text_file_data')

# Save text to .txt file
file = open("data.txt", "w+", encoding='UTF-8')

for chars in text:
    file.write(chars)

file.close()