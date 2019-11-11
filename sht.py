import pandas as pd
import os
entries=os.listdir('xls')
for entry in entries:
    print(entry)
    fA=pd.read_excel('xls/'+entry)
    data=fA.loc[(fA['队长所在单位'] == '上海科技大学')|(fA['队友所在单位'] == '上海科技大学')|(fA['队友所在单位.1'] == '上海科技大学')]
    print(data) 