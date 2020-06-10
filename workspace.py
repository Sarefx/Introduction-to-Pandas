import os
import numpy as np
import pandas as pd
import datetime

test_balance_data = {
    'pasan': 20.00,
    'treasure': 20.18,
    'ashley': 1.05,
    'craig': 42.42,
}

# series is a single dimension container

balances = pd.Series(test_balance_data)  # The Series constructor accepts any dict-like object
unlabeled_balances = pd.Series([20.00, 20.18, 1.05, 42.42])  # You can pass any iterable as the first argument. You can also add indexes too, otherwise indexes will be represted as ints

# Series behave like dictionaries

for label, value in balances.items():
    print("The label {} has a value of {}".format(label, value))

# Accessing a non-existent key raises a KeyError.

try:
    balances['kermit']
except KeyError:
    print('Accessing a non-existent key raises a `KeyError`.')

# Use get to safely access keys. None is returned if key not present.

if balances.get('kermit') is None:
    print('Use `get` to safely access keys. `None` is returned if key not present.')

# Use in to test the existence of a label.

if 'kermit' not in balances:
    print('Use `in` to test the existence of a label.')

# Accessing by Property

balances.ashley  # will return 1.05

import this  # will display zen of python

balances[-1]  # will return the last balance
balances['pasan']  # Since a series is labelled, you can also access it much like you would a standard dict.
balances.loc['pasan']  # A Series exposes a property named loc which can be used to explicitly lookup by label based indices only.
balances.iloc[0]  # will return the first value

test_balance_data = {
    'pasan': 20.00,
    'treasure': 20.18,
    'ashley': 1.05,
    'craig': 42.42,
}

test_deposit_data = {
    'pasan': 20,
    'treasure': 10,
    'ashley': 100,
    'craig': 55,   
}

balances = pd.Series(test_balance_data)
deposits = pd.Series(test_deposit_data)

balances -= deposits  # Undo the change using inplace subtraction
balances += deposits  # This is the same as the loop above using inplace addition
balances + 5  # 5 is brodacsted and added to each and every value. This returns a new Series.

coupons = pd.Series(1, ['craig', 'ashley', 'james'])
balances.add(coupons, fill_value=0)  # Returns a new Series. all empty values get 0 added otherwise it would give nan value

# dataframe is pandas version of matrix

test_users_list = [
    ['Craig', 'Dennis', 42.42],
    ['Treasure', 'Porth', 25.00]
]
pd.DataFrame(test_users_list)

pd.DataFrame(test_users_list, index=['craigsdennis', 'treasure'],
            columns=['first_name', 'last_name', 'balance'])

by_username = {
    'craigsdennis': {
        'first_name': 'Craig',
        'last_name': 'Dennis',
        'balance': 42.42
    },
    'treasure': {
        'first_name': 'Treasure',
        'last_name': 'Porth',
        'balance': 25.00
    }
}

pd.DataFrame.from_dict(by_username, orient='index')  # orient helps to specify keys are rows(index) or columns

test_user_data = {
    'first_name': ['Craig', 'Treasure', 'Ashley', 'Guil'],
    'last_name': ['Dennis', 'Porth', 'Boucher', 'Hernandez'],
    'balance': [42.42, 25.00, 2.02, 87.00]
}
test_user_names = ['craigsdennis', 'treasure', 'lindsay2000', 'guil']
users = pd.DataFrame(test_user_data, index=test_user_names)

balances = users['balance']  # will return a series
balances.name  # will return 'balance'

users_file_name = os.path.join('data', 'users.csv')

# Open the file and print out the first 5 lines
with open(users_file_name) as lines:
    for _ in range(5):
        # The `file` object is an iterator, so just get the next line 
        print(next(lines))

users = pd.read_csv(users_file_name, index_col=0)
users.head()  # shows top 5 entries

len(users)  # shows the total amount of rows in the file
users.shape  # shows the shape of the DataFrame
users.count()  # will count how many non empty values we have per column
# DataFrame has the ability to contain multiple data types or dtypes
users.dtypes  # shows dtype of each column. Some of the data will be assumed from csv
users.describe()  # shows statistics about the data
users.mean()  # shows mean or everage per column
users.std()  # shows standard diviation per column
users.min()  # shows the minimum per column
users.max()  # shows the maximum per column
users.email_verified.value_counts()  # will count each True and False per that column
users.first_name.value_counts().head()  # will show the most frequevent 5 names in that column
users.sort_values(by='balance', ascending=False).head()  # sorts values by the balance column and will show top 5 entries
users.sort_values(by=['last_name', 'first_name'], inplace=True)  # permanenly changes the DataFrame with the new sort
users.sort_index(inplace=True)  # sorts the data back to original scheme and saves it

# This vectorized comparison returns a new `Series` ... 
no_referrals_index = users['referral_count'] < 1  # shows False for no referrals and True for more than 1 referral and saves it in a new Series
users[no_referrals_index].head()  # will return all rows that didnt take advantage of referral program
~no_referrals_index.head()  # shows inverse. ~ is the key symbol
users[~no_referrals_index].head()  # will show all users that did take advantage of referral program
users.loc[no_referrals_index, ['balance', 'email']].head()  # Select rows where there are no referrals, and select only the following ordered columns
users[users['referral_count'] == 0].head()  # It is also possible to do the comparison inline, without storing the index in a variable.
users[(users['referral_count'] == 0) & (users['email_verified'] == True)].head()  # Select all users where they haven't made a referral AND their email has been verified

## CHALLENGE - Find the top referrers ##
# TODO: Select users that have a referral count greater than or equal to 5 and have verified emails

top_referral_users = users[(users['referral_count'] >= 5) & (users['email_verified'] == True)]
print(top_referral_users)
# CHALLENGE completed

transactions = pd.read_csv(os.path.join('data', 'transactions.csv'), index_col=0)

users[(users.first_name == "Adrian") & (users.last_name == "Fang")]['balance']  # shows balance for the user Adrian Fang

# the code below will give an error SettingWithCopyWarning
#users[(users.first_name == "Adrian") & (users.last_name == "Fang")]['balance'] = 35.00

users.loc[(users.first_name == "Adrian") & (users.last_name == "Fang"), 'balance'] = 35.00  # the correct way to set a new value

users.at['adrian', 'balance'] = 35.00  # this is a quick way to set a scalar value

record = dict(sender=np.nan, receiver='adrian', amount=4.99, sent_date=datetime.datetime.now().date())  # building a new record

transactions.append(record, ignore_index=True).tail()  # will return a copy with a new row "record". Method tail shows last 5 rows. ignore_index set to True, so it will autogenerate index for the row

next_key = transactions.index.max() + 1  # another way to add a row
transactions.loc[next_key] = record

latest_id = transactions.index.max()
transactions.at[latest_id, 'notes'] = 'Adrian called customer support to report billing error.'  # adds a new column for the last id

transactions['large'] = transactions.amount > 70  # adds a new column and set it to True if amount is greater than 70
transactions.rename(columns={'large': 'big_sender'}, inplace=True)  # will rename column 'large' to 'big_sender'
transactions.drop(columns=['notes'], inplace=True)  # deletes a column 'notes'
transactions.drop(['big_sender'], axis='columns', inplace=True)  # deletes a column 'big_sender'
last_key = transactions.index.max()  # selects index for the last row
transactions.drop(index=[last_key], inplace=True)  # removes the last row. inplace=True makes sure the removal is permanent

## CHALLENGE - Update users ##

# TODO: Update kimberly@yahoo.com to have the last name of "Deal"

user = users.index[users['email']=='kimberly@yahoo.com']
target = user[0]
users.loc[target,'last_name']='Deal'

# TODO: Update the username jeffrey to jefrey (only one f)

users.rename(index={'jeffrey':'jefrey'},inplace=True)

print(users.loc[target])
print(users.loc['jefrey'])

# CHALLENGE completed

requests = pd.read_csv(os.path.join('data', 'requests.csv'), index_col=0)

transactions.head(2)  # returns top 2 rows
requests.head(2)

# merges transactions onto requests
successful_requests = requests.merge(
    transactions,
    left_on=['from_user', 'to_user', 'amount'], 
    right_on=['receiver', 'sender', 'amount']
)

successful_requests.dtypes  # returns dtypes of columns. All columns except amount are 'object'
successful_requests['request_date'] = pd.to_datetime(successful_requests['request_date'])  # changes dtype from 'object' to 'datetime'
successful_requests['sent_date'] = pd.to_datetime(successful_requests['sent_date'])
successful_requests['time_passed'] = successful_requests.sent_date - successful_requests.request_date  # stores the difference between dates in 'time_passed' column
successful_requests.sort_values(by='time_passed', ascending=False).head(5)  # returns the longest 5 requests
message = "Wow! ${:,.2f} has passed through the request system in {} transactions!!!".format(
    successful_requests.amount.sum(),
    len(successful_requests),
)
print(message)

# Create a boolean Series of records that are duplicated.
dupes = requests[requests.duplicated(('from_user', 'to_user', 'amount'), keep=False)]  # Note that `keep=False` marks all that are duplicated
# Order by requester and the date of request.
dupes.sort_values(['from_user', 'request_date'])  # Note that `request_date` in this case is a string, but this string date format sorts properly still.

successful_requests.sort_values('request_date', inplace=True)  # Let's get our records sorted chronologically
successful_requests.drop_duplicates(('from_user', 'to_user', 'amount'), keep='last', inplace=True)  # And then we'll drop dupes keeping only the last one.
message = "Wow! ${:,.2f} has passed through the request system in {} transactions!!!".format(
    successful_requests.amount.sum(),
    len(successful_requests),
)
print(message)

made_request_index = users.index.isin(requests.from_user)  # Create a boolean array where we check to see if the label (username)
users[made_request_index].head()  # This will get us a list of all users who **have** made a request
users[~made_request_index].head()  # returns users who have no made a request yet
users[users.last_name.isna()].head()  # returns users that have missing data
users_with_unknown = users.fillna('Unknown')  # returns a new DataFrame with missing data replated with "Uknown"
users_with_unknown[users_with_unknown.last_name.isna()]  # checks if there are any users left with missing data. Should return nothing
users_with_last_names = users.dropna()  # this will drop users with missing data

transactions[transactions.sender.str.startswith('$')]  # will checks for any sender that has name starts with $
transactions.sender = transactions.sender.str.replace('$', '')   # replaces $ with nothing
transactions[transactions.receiver.str.isupper()]  # returns users that have all upper case names
transactions.loc[transactions.receiver.str.isupper(), 'receiver'] = transactions.receiver.str.lower()  # changes the case back to lower
len(transactions[transactions.receiver.str.isupper()])  # verifies that all names changed to lower

print("Challenge begins")
## CHALLENGE - Verified email list ##

# TODO: Narrow list to those that have email verified.
#  The only columns should be first, last and email
email_list = users[users.email_verified == True]
email_list.drop(columns=['email_verified', 'signup_date', 'referral_count', 'balance'], inplace=True)  # deletes a columns

# TODO: Remove any rows missing last names
email_list = email_list[~email_list.last_name.isna()]
email_list = email_list.dropna()  # this an alternative

# TODO: Ensure that the first names are the proper case
email_list.loc[~email_list.first_name.str.istitle(), 'first_name'] = email_list.first_name.str.title()

# Return the new sorted DataFrame..last name then first name ascending
print(email_list)

grouped_by_receiver = transactions.groupby('receiver')

type(grouped_by_receiver)  # will return data type DataFrameGroupBy
grouped_by_receiver.size()  # Returns a Series of total number of rows
grouped_by_receiver.count()
grouped_by_receiver.sum()
users['transaction_count'] = grouped_by_receiver.size()  # Create a new column in users called transaction count, and set the values to the size of the matching group
len(users[users.transaction_count.isna()])  # Not every user has made a transaction, let's see what kind of missing data we are dealing with
users.transaction_count.fillna(0, inplace=True)  # Set all missing data to 0, since in reality, there have been 0 received transactions for this user
users.transaction_count = users.transaction_count.astype('int64')  # Convert from the default type of float64 to int64 (no precision needed)

# Sort our values by the new field descending (so the largest comes first), and then by first name ascending
users.sort_values(
    ['transaction_count', 'first_name'],
    ascending=[False, True],
    inplace=True
)
users.loc[:, ['first_name', 'last_name', 'email', 'transaction_count']].head(10)  # Take a look at our top 10 receivers, showing only the columns we want
