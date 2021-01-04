import pandas as pd
import datetime

t = datetime.datetime.now()
y = t.year
m = t.month
d = t.day
date = str(y)+'-'+str(m)+'-'+str(d)

def save_to_file(result1, result2, keyword):
    filename = f'./[{date}]Jobs({keyword}).xlsx'
    My_Job = pd.concat([result1,result2])
    return My_Job.to_excel(filename)