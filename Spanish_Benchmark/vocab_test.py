import pandas as pd
data = pd.read_csv('./Spanish_Utils/new_combined.csv')

df_V = data[data['pos'] == 'V']
df_V_arg1 = df_V[['arg_1']]
print(list(df_V_arg1.arg_1.unique()))

nouns = data['expression'].loc[(data['noun'] == 1) & (data['arg_1'].isin(list(df_V_arg1.arg_1.unique())))]
print(nouns)
