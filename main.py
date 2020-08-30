# used to handle spreadsheet
import pandas as pd

# get spreadsheet file name and sheet
file_name = input("Xlsx Name: ")
sheet_name = input("Sheet Name: ")

# search in O(n) time
# I could improve this if we sort the spreadsheet first
# then all operations after would be much faster!
def linear_search(series, target_val):
    for index in range(series.size):
        if ( series[index] == target_val ):
            return index
        else:
            continue
    return -1

# read in the spreadsheet
try:
    df = pd.read_excel(file_name, index_col=0, na_values=["""modify this"""], na_filter=True, sheet_name=sheet_name)
except FileNotFoundError:
    print("Error please enter a valid file name!")
    exit()

column = input("Enter a column to search: ")

while(True):
    # search query
    search = input("enter a search: ")

    # exit string
    if(search == 'q'):
        break

    # replace string
    replace = int(input("replace with: "))

    # search the series
    index = linear_search(df[column], search)

    # find and replace
    try:
        df[column][index] = replace
        print(df[column][index], replace)
    except KeyError:
        print('enter a valid query!')
        continue

df.to_excel('output.xlsx')
exit()
