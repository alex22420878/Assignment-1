import pandas as pd

df1= pd.read_csv('respondent_contact.csv')
df2= pd.read_csv('respondent_other.csv')

#merge
merge_file = pd.merge (df1, df2,
                        left_on='respondent_id',right_on='id',
                        how= 'outer')

#drop
df3=merge_file.drop (['id'],axis=1)
df4=merge_file.dropna(axis=0)
output_fite=df4[df4["job"].str.contains("insurance | Insurance")==False]
#export
output_fite.to_csv('output_file.csv',index=False)