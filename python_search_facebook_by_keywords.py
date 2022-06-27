####################################################################################################################
# ** Set up section. No need to modify.
#   - See below from " ** 여기만 변경하시면 돼요!".

import pandas as pd

# Read json files with pandas.
df_lee  = pd.read_json ("facebook_lee.json")
df_yoon = pd.read_json ("facebook_yoon.json")

# Function option 1
def ssearch_post (key_list, df, stretch = False):
    if stretch == True:
        pd.set_option('display.max_colwidth', None)
    if stretch == False:
        pd.reset_option('display.max_colwidth')
    for key in key_list:
        key_df = df [df ["text"].apply (lambda x: key in x) == True]
        print ("\n*** Search keyword: " + key)
        print ("Num: " + str(len (key_df ["date"])) + '\n')
        print (key_df)
    return (key_df)

# Function option 2
def any_bool (x, key_list):
    bool = False
    for i in range (0, len (key_list)):
        if key_list[i] in x:
            bool = True
    return bool
def ssearch_all_posts (key_list, df, stretch = False):
    if stretch == True:
        pd.set_option('display.max_colwidth', None)
    if stretch == False:
        pd.reset_option('display.max_colwidth')
    key_df = df [df ["text"].apply (lambda x: any_bool (x, key_list)) == True]
    print ("\n*** Search keyword: " + str (key_list))
    print ("Num: " + str(len (key_df ["date"])) + '\n')
    print (key_df)
    return (key_df)


####################################################################################################################
####################################################################################################################
####################################################################################################################

# ** 여기만 변경하시면 돼요! (1) key_list, (2) df, (3) which func to use

key_list = ["남성", "여성", "성별", "남녀", "젠더"]
df = df_yoon

# ** Function to identify postings per each keyword in key_list.
#   - stretch == True -> see full text contents
#   - stretch == False -> see text contents with ...
ssearch_post (key_list, df, stretch = True)

# ** Function to identify postings with any of the keyword in key_list.
ssearch_all_posts (key_list, df, stretch = False)
