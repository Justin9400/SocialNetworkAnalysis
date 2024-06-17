import pandas as pd 

df = pd.read_csv('enron.csv')

def clean_data():
    removed_duplicates_data = df.drop_duplicates()
    removed_nan_data = removed_duplicates_data.dropna()
    # removed_nan_data.to_csv('temp.csv')
    return removed_nan_data

def extract_source_emails(data):
    source_emails = pd.DataFrame()
    for i in range(len(data.index)):
        if "RE:" in data['subject'].iloc[i]:
            source_emails.
def main(): 
    cleaned_data = clean_data()
    extract_source_emails(cleaned_data)
    # print(cleaned_data)
    # for i in range(len(cleaned_data.index)):
    #     print(df['subject'][i])



main()