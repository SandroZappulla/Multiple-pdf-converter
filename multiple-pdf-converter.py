# Python Multiple PDF Converter
# Author: Sandro Zappulla
# version: v0.1

# IMPORT
# Installation:
#  python -m pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org docx2pdf
from docx2pdf import convert

# create array-list for multiple files
array_filename = []
# start value for the two counters
counter = 0
counter2 = 0

# Multiple PDF Converter > Main Part
print("Wie viele Dateien möchten Sie Konvertieren?")
number_of_files = int(input())
print("WICHTIG: Es wird nur der Dateiname ohne Dateiendung erwartet!")

# counter for the array-list with user input for the filenames
while counter < number_of_files:
    print("Bitte den Namen für die Datei Nummer " + str(counter+1) + " eingeben: " )
    input_array = input()
    array_filename.append(input_array)
    counter+=1

# second counter to convert the .docx file to the .pdf file
while counter2 < number_of_files:
    file_input = array_filename[counter2] + ".docx"
    file_output = array_filename[counter2] + ".pdf"
    convert(file_input, file_output)
    counter2+=1

# finish output
print("Dateinamen welche Konvertiert wurden: ")
print(array_filename)
