import pandas as pd


df = pd.read_csv('LabeledDataCCG.csv')
df_prediction = pd.read_csv('prediction.csv')

data_info = df.dtypes.to_frame(name='DataType')
data_info['MissingValues'] = df.isnull().sum()
data_info['UniqueValues'] = df.nunique()
print(data_info)

j = 0
for i in range(len(df)):
    if j >= len(df_prediction):
        break
    if i == df_prediction.loc[j, 'X']:
        df.loc[i, 'Directors102b7'] = 'Y' if df_prediction.loc[j, 'Directors102b7'] == 2 else 'N'
        j += 1

# Save the updated dataframe to a new CSV file
df.to_csv('modified_data.csv', index=False)


# data_dict = {row['Unnamed: 0']: {
#         'CIK': row['CIK'],
#         'Charter_ID': row['Charter_ID'],
#         'Date_Coded': row['Date_Coded'],
#         'Date_Filing': row['Date_Filing'],
#         'CompanyName': row['CompanyName'],
#         'State': row['State'],
#         'FullRestate': row['FullRestate'],
#         'EntityType': row['EntityType'],
#         'MultComm': row['MultComm'],
#         'MultCommUnequal': row['MultCommUnequal'],
#         'MultPreferred': row['MultPreferred'],
#         'PreferredVote': row['PreferredVote'],
#         'PreferredVoteLimited': row['PreferredVoteLimited'],
#         'BlankCheck1': row['BlankCheck1'],
#         'BustBankSHVote': row['BustBankSHVote'],
#         'BustBankBoD': row['BustBankBoD'],
#         'ReallocateComPref': row['ReallocateComPref'],
#         'UnequalVote': row['UnequalVote'],
#         'WCterm': row['WCterm'],
#         'WCCond': row['WCCond'],
#         'WCProhibit': row['WCProhibit'],
#         'SMTerm': row['SMTerm'],
#         'SMCond': row['SMCond'],
#         'SMProhibit': row['SMProhibit'],
#         'StaggeredBd': row['StaggeredBd'],
#         'StaggeredBdPhaseOut': row['StaggeredBdPhaseOut'],
#         'CumulativeVoting': row['CumulativeVoting'],
#         'CharterSupMaj': row['CharterSupMaj'],
#         'MergerSupMaj': row['MergerSupMaj'],
#         'CorpOppDirector': row['CorpOppDirector'],
#         'CorpOppOfficer': row['CorpOppOfficer'],
#         'CorpOppSH': row['CorpOppSH'],
#         'Directors102b7': row['Directors102b7'],
#         'Officers102b7': row['Officers102b7'],
#         'IndemnityDirector': row['IndemnityDirector'],
#         'IndemnityOfficer': row['IndemnityOfficer'],
#         'AdvancementDirector': row['AdvancementDirector'],
#         'AdvancementOfficer': row['AdvancementOfficer'],
#         'InsuranceDirector': row['InsuranceDirector'],
#         'InsuranceOfficer': row['InsuranceOfficer']
#     } for index, row in df.iterrows()}


# count_Y = 0
# count_N = 0
# for i in range(len(data_dict)):
#     if data_dict[i]["Directors102b7"] == 'Y' :
#         count_Y = count_Y+1
#     if data_dict[i]["Directors102b7"] == 'N' :
#         count_N = count_N+1

# print(count_Y)
# print(count_N)
# print(count_Y+count_N)
