import pandas as pd

es_df = pd.read_csv('./ES_2020.tsv', sep="\t", header=None, names=["Id", "Content"])
polarity_df = pd.read_csv('./es_polarity_2020.tsv',  sep="\t", header=None, names=["Id", "Polarity"])

merged_df = pd.merge(es_df, polarity_df, on="Id")
merged_df['Polarity'] = merged_df['Polarity'].replace({'P': 'POS', 'N': 'NEG'})
merged_df = merged_df.sort_values(by="Id")
merged_df = merged_df.iloc[:500]
merged_df.to_excel("Spain_test_2020.xlsx", index=False)