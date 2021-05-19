import pandas as pd
import xlsxwriter
import csv

path=""

def Convert():
    try:
        # Convert CSV to XLSX
        head_file = pd.read_csv(r''+path+'.csv',delimiter=';')
        head_file.to_excel(r''+path+'.xlsx',index=None)

    except OSError as e:
        print(e)
        print("Error!!")
    finally:
        return 0

if __name__=="__main__":
    print("Entre com o caminho do arquivo a ser convertido:")
    path=input("Path->")
    Convert()
    print("Finalizado!")
    