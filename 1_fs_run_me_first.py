import os

# Change current working directory to file location
absPath = os.path.abspath(__file__)
dirName = os.path.dirname(absPath)
os.chdir(dirName)

# Create file structure
try:
    os.makedirs('.\\Financial_Scraper\\put_pdfs_here')
    os.chdir(os.getcwd() + '\\Financial_Scraper')
    os.mkdir('.\\text_file_data')
    os.mkdir('.\\final_xlsx_output')
except:
    print('Files already exist.')
