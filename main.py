import pandas as pd
from rich.tree import Tree
from rich.console import Console
from rich.table import Table
from rich.progress import track
import rich.prompt

data = pd.read_csv('questions.csv', delimiter='.')
q = data['Questions']
answers = []
range_str = list(range(1,8))
# print(q[3])

for i in range(len(q)):
    answer = rich.prompt.IntPrompt.ask(q[i], choices=str(range_str), show_choices=True)  
    answers.append(answer)
a = pd.read_csv('answers.csv', delimiter=',')

a.loc[len(a)] = answers
a.to_csv('answers.csv',index=False)

ext_int = ['Extroversion - Introversion',a.loc[:,'q1':'q4'].sum().mean()]
fee_thi = ['Feeling - Thinking',a.loc[:,'q5':'q8'].sum().mean()]
per_jud = ['Perceiving - Judging',a.loc[:,'q9':'q12'].sum().mean()]
sen_int = ['Sensing - Intuition',a.loc[:,'q13':'q16'].sum().mean()]

# new_row1 = pd.DataFrame({'Extroversion - Introversion': ext_int},index=True)
# new_row2 = {'Feeling - Thinking': fee_thi}
# new_row3 = {'Perceiving - Judging': per_jud}
# new_row4 = {'Sensing - Intuition': sen_int}


mean_a = pd.read_csv('mean_answers.csv',delimiter=',')

mean_a.loc[len(a)] = ext_int
mean_a.loc[len(a)] = fee_thi
mean_a.loc[len(a)] = per_jud
mean_a.loc[len(a)] = sen_int
mean_a.to_csv('mean_answers.csv',index=False)


#mean_adf = pd.concat([mean_a,new_row1],axis=0,ignore_index=True)
#print(mean_a)




# spara mean i kategorier 