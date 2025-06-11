
import xml.etree.ElementTree as ET
import pandas as pd

#Cargamos el archivo XML
tree = ET.parse('Spain_train_set.xml')
root = tree.getroot()

data = []
for tweet in root.findall('tweet'):
    tweet_id = tweet.find('tweetid').text
    content = tweet.find('content').text
    polarity = tweet.find('sentiment').find('polarity').find('value').text
    if polarity != 'NONE':
        data.append([tweet_id, content, polarity])

df = pd.DataFrame(data, columns=['ID', 'Content', 'Polarity'])

df['Polarity'] = df['Polarity'].replace({'N': 'NEG', 'P': 'POS'})

df.to_excel('Spain_train_set_2019.xlsx', index=False)

df.to_csv('Spain_train_set_2019.csv', index=False)