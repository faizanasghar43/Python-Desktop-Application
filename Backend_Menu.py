# import openpyxl library
import pandas as pd

def listdel(a):

        data=pd.read_excel("Dummy File XYZ.xlsx")

        index = data.index[data['Customer No'] == a ].tolist()
        pd.DataFrame = data.drop(data.index[index])
        pd.DataFrame.to_excel('Dummy File XYZ.xlsx',index=False)
        print(data)
if __name__ == '__main__':
    b = 50
    listdel(b)
