import pandas as pd
import matplotlib.pyplot as plt

def fetch_Covid_Data():
    #Download Covid-19 Dataset
    url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

    #Save Data Set to variable and return
    df_confirmed = pd.read_csv(url_confirmed)

    return df_confirmed

def save_data():
    #Saves downloaded data to text
    #Write dataset to text file
    with open ('covid_dataset.txt', 'w') as f:
        #Iterate through data set and print all rows
        for index, row in df_confirmed.iterrows():
            #print(row)
            f.write(str(row) + '\n')

def organize_data(df_confirmed):
    #Drop unnecessary columns
    df_confirmed = df_confirmed.drop(['Province/State', 'Lat', 'Long'], axis=1)

    #convert index to DateTimeIndex
    #FIXME: WHY WONT YOU CONVERT!!!???
    df_confirmed = pd.to_datetime((df_confirmed.stack()).unstack(), format='%m/%d/%y', errors='coerce').unstack()

    #Drop rows with missing dates
    df_confirmed = df_confirmed.dropna()

    #Group by country
    df_confirmed = df_confirmed.groupby('Country/Region').sum()

    return df_confirmed

def visualize_data():
    #TODO: Allow user to select country from drop down
    #window menu
    global df_confirmed

    #Plot data for example country
    italy_data = df_confirmed.loc['Italy']
    plt.plot(italy_data.index, italy_data.values)

    #customize plot
    plt.title('Total Confirmed Covid-19 Cases in Italy')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')

    #Display
    plt.show()

#Main Code Loop
df_confirmed = fetch_Covid_Data()

#print list of available countries
print(df_confirmed.index)

df_confirmed = organize_data(df_confirmed)
#save_data(df_confirmed)
visualize_data()

#print(df_confirmed.head())
