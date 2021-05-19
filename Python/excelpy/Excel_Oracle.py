import cx_Oracle as cxo
import pandas as pd
import xlsxwriter

def Connect():
    try:
        DBconn = cxo.connect('SYSTEM/21169500g@@//localhost:1521/XE')
        print('oracle v.', DBconn.version)
        output = pd.read_sql("SELECT * FROM SYS.LOGGER", con=DBconn)
        output.to_excel(r'I:\\Códigos\\Python\\excelpy\\relatorio.xlsx',index=None)
    except(cxo.DatabaseError,IOError) as error:
        print(error)
    finally:
        DBconn.close()
        return 0


if __name__ == '__main__':
  
    print("Digite a senha do BD:")
    print ("Coloque o caminho para salvar o arquivo")
    print(Connect())