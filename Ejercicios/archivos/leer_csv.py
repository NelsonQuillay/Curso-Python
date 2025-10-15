import csv

with open("Ejercicios\\archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)

#PARA LEER ARCHIVOS MAS GRANDES
'''def read_csv_in_chunks(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for i, chunk in enumerate(reader):
            print("Chunk #{}".format(i))
            print(chunk)

read_csv_in_chunks('Big_file.csv')'''