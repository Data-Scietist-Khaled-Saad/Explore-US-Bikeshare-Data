"""
Owner: Khaled Saad
Project: 1st project _ Udacity _ Egypt FWD
"""

#import packages
import time
import pandas as pd
import numpy as np

#dictionary of the raw adta files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print("*"*100)
    print('\n Hello! Let\'s explore some US bike_share data! \n')
    print("*"*100)

    # get user input for city (chicago, new york city, washington).
    while True:
        cities= { 'ch': 'chicago',
                      'ny': 'new_york_city',
                      'wa': 'washington' }
        city= input("\n Please select a city by typing city code: \n Chicago(code: ch) \n New york city(code: ny) \n Washington(code: wa) \n").lower()
        if city in cities:
            selected_city = cities[city]
            print('-'*100)
            print("you selected : ",selected_city)
            print('-'*100)
            break
        else:
            print("\n Please enter a valid city code (ch, ny, wa) \n")

    # get user input for month (all, january, february, ... , june)
    def get_month():
        while True:
            months= { '1' : 'January',
                     '2' : 'February',
                     '3' : 'March',
                     '4' : 'April',
                     '5' : 'May',
                     '6' : 'June',
                     ' ' : 'all months' }
            month= input("\n Please select a month by typing month number (from 1 to 6) or just press a space to select all six months \n")
            if month in months:
                selected_month = months[month]
                print('-'*100)
                print("you selected : ", selected_month)
                print('-'*100)
                break
            else:
                print("\n Please enter a valid month number (from 1 to 6) or just press a space to select all six months \n")
        return(selected_month)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    def get_day():
        while True:
            days= {'sunday' : 'Sunday',
                   'monday' : 'Monday',
                   'tuesday' : 'Tuesday',
                   'wednesday' : 'Wednesday',
                   'thursday' : 'Thursday',
                   'friday' : 'Friday',
                   'saturday' : 'Saturday',
                    ' ' : 'all days' }
            day= input("\n Please select a day or just press a space to select all days \n")
            if day in days:
                selected_day = days[day]
                print('-'*100)
                print("you selected : ", selected_day)
                print('-'*100)
                break
            else:
                print("\n Please enter a valid day or just press a space to select all days \n")
        return(selected_day)

    #ask user for choices of time filters
    while True:
        filtr = input(" \n If you would like to filter the data by month select 'm' \n\n If you would like to filter the data by day select 'd' \n\n If you would like to filter the data by month and day select 'b' \n\n If you would not like to filter the data by month or day select 'n' \n")
        if filtr == "m":
            selected_month = get_month()
            selected_day = "all days"
            break
        elif filtr == "d":
            selected_day = get_day()
            selected_month = "all months"
            break
        elif filtr == "b":
            selected_month = get_month()
            selected_day = get_day()
            break
        elif filtr == "n":
            selected_day = "all days"
            selected_month = "all months"
            break
        else:
            print("\n Please enter a valid selsction \n")

    print('-'*100)
    print("\n we will do the analysis according to your choices as follow \n" , "\n city : ", selected_city, "\n","\n month : " , selected_month, "\n", "\n day : ", selected_day,"\n")
    print('-'*100)

    return[selected_city, selected_month, selected_day]

def load_data(selected_city, selected_month, selected_day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # read the required csv file into dataframe according to the entered City
    print("\n loading data of : ", selected_city)
    print("\n # ",CITY_DATA[selected_city]," # \n")
    df = pd.read_csv(CITY_DATA[selected_city])

    # convert Start Time and End Time columns to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # add new columns of month and day and "hour" created by extracting month
    #and day and hour from Start Time
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # to extract data as per time filters from user inputs
    if selected_month != 'all months':
        df = df.loc[(df['month']==selected_month)]
    if selected_day != 'all days':
        df = df.loc[(df['day_of_week']==selected_day)]

    #explore the collected data
    print('*'*100)
    print("\n now let's take a look on the loaded data as per your selections \n")
    print('*'*100)
    print("\n As per your selection the data size is : \n ",df.size)
    print("-"*100)
    print("\n As per your selection the data shape is : \n ",df.shape)
    print("-"*100)
    print("\n As per your selection the first 5 rows of the data are : \n ",df.head())
    print("-"*100)
    print("\n As per your selection the last 5 rows of the data are : \n ",df.tail())
    print("-"*100)

    #to explore more data
    x = 5
    while True:
        explr = input("If you would like to explore more data type 'yes' and press enter or just press enter to skip ")
        if explr.lower() == "yes":
                x += 5
                print("\n x = ", x)
                print("-"*100)
                print("\n As per your selection you are watching the rows from row no. ", x-4,"to row no.",x," \n ", df.iloc[ x-5 : x ] )
                print("-"*100)
        else:
            break

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("As per your selections the most common month is: ", df['month'].mode()[0])

    # display the most common day of week
    print("As per your selections the most common day is: ", df['day_of_week'].mode()[0])

    # display the most common start hour
    print("As per your selections the most common hour is: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("As per your selections the most common start statioin is: ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("As per your selections the most common end statioin is: ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['combination'] = "from  " + df['Start Station'] +" to  "+ df['End Station']
    print("As per your selections the most frequent combination of start station and end station trip is: ",\
     df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('As per your selections total travel time is', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('As per your selections mean travel time is', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    print("As per your selections the user types is : ", df['User Type'].value_counts().to_frame())

    #Display counts of gender
    if 'Gender' in df:
        print( "As per your selections user gender is : " ,df['Gender'].value_counts().to_frame())
    else:
        print('Sorry, No Gender data available')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode()[0])
        print("As per your selections the earliest year of birth is:",earliest_birth,
        "\n As per your selections the most recent year of birth is:",recent_birth,
        "\n  As per your selections the most common year of birth is: ",common_birth)
    else:
        print('Sorry, No Birth year data available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def main():
    while True:
        selected_city, selected_month, selected_day = get_filters()
        df = load_data(selected_city, selected_month, selected_day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n if you Would you like to restart please type "yes" and press enter or just press enter to exit \n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

"""
The end
Friday
20230113
"""
