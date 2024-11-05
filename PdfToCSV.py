import pdfplumber
import csv

pdf_file = "C:/Users/Aced/Downloads/input.pdf"
csv_file = "output.csv"

with pdfplumber.open("C:/Users/Aced/Downloads/input.pdf") as pdf:
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Extract data from every page
        for page in pdf.pages:
            table = page.extract_table()

            # If the table is available, enter the Row -based CSV file
            if table:
                for row in table:
                    writer.writerow(row)

