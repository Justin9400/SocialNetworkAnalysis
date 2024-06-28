import pandas as pd 
import numpy as np

df = pd.read_csv('enron.csv')

def clean_data(path):
    df = pd.read_csv(path)
    df['subject'].replace(to_replace=['', '#NAME?', 'RE:'], value=np.nan, inplace=True)

    df.dropna(subset=['subject'], inplace=True)
    df = df[~df.duplicated(subset=['subject'])]
    return df

def extract_source_emails(data):
    source_emails = pd.DataFrame()
    count = df['subject'].str.contains('Re:', case=False).sum()
    print(count)

    
def main(): 
    cleaned_data = clean_data('enron.csv')
    extract_source_emails(cleaned_data)

main()