# financial_scraper
Python script to pull usable data out of bank statements

## Goal:
The goal of this project is to become more comfortable using Python to work with .pdf, .txt., .xlsx file operations\n
as well as using regex to pull usable data patterns out of raw text

## Project Structure
This program consists of several dependent scripts:
1. **1_fs_run_this_first** creates a folder structure that isolates specific data to be used by the following scripts.
2. **2_fs_preprocessing** creates and formats an .xlsx workbook, extracts data from the given .pdf files, and writes the data to a central .txt document.
3. **3_fs_scraper extracts** data from the data.txt file, separates usable portions, and writes them to precreated .xlsx workbook separated by revenues and expenses.
