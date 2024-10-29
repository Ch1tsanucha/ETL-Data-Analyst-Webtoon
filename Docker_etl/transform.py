import pandas as pd

df = pd.read_csv('data.csv')

df.head()

Author =df["Author"]

substring_to_remove = 'author info'
Author = Author.str.replace(substring_to_remove, '', regex=False).str.strip()



Read_Number = df["Read_Number"]

def convert_value(value):
    if 'B' in value:
        return float(value.replace('B', '')) * 1_000_000_000
    elif 'M' in value:
        return float(value.replace('M', '')) * 1_000_000
    else:
        return float(value)
    
remove1 = 'view '
remove2 = ','

# Remove the substring
Read_Number = Read_Number.str.replace(remove1, '', regex=False).str.strip()
Read_Number = Read_Number.str.replace(remove2, '', regex=False).str.strip()
Read_Number = Read_Number.apply(convert_value)


Subscribe_Number = df["Subscribe_Number"]
remove1 = 'subscribe '
remove2 = ','

# Remove the substring
Subscribe_Number = Subscribe_Number.str.replace(remove1, '', regex=False).str.strip()
Subscribe_Number = Subscribe_Number.str.replace(remove2, '', regex=False).str.strip()
Subscribe_Number = Subscribe_Number.apply(convert_value)
Subscribe_Number.head()

Rate_Number = df["Rate_Number"]

remove1 = 'grade '
remove2 = ' RATE'

# Remove the substring
Rate_Number = Rate_Number.str.replace(remove1, '', regex=False).str.strip()
Rate_Number = Rate_Number.str.replace(remove2, '', regex=False).str.strip()

Date_First = df["Date_First"]

def convert_to_timestamp(date_str):
    return pd.to_datetime(date_str, format='%b %d %Y')


remove1 = ','

# Remove the substring
Date_First = Date_First.str.replace(remove1, '', regex=False).str.strip()
Date_First = Date_First.apply(convert_to_timestamp)


Like_First =df["Like_First"]


remove1 = 'like'
remove2 = ','

# Remove the substring
Like_First = Like_First.str.replace(remove1, '', regex=False).str.strip()
Like_First = Like_First.str.replace(remove2, '', regex=False).str.strip()


new_df = df
new_df["Author"] = Author
new_df["Read_Number"] = Read_Number
new_df["Subscribe_Number"] = Subscribe_Number
new_df["Rate_Number"] = Rate_Number
new_df["Date_First"] = Date_First
new_df["Like_First"] = Like_First

print(df)
new_df.to_csv('data.csv', index=False)
