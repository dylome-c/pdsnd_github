import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
              print("\nPlease only enter city name (Chicago/ New York City/ Washington): ")
              city = input().lower()

    if city in CITY_DATA.keys():
            print("Hello," + " data from " + city.title() + " will be called.")

    else:
            print("ERROR. Restarting the programme...")
            print('-'*40)

    # get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january': 1,
                      'february': 2,
                      'march': 3,
                      'april': 4,
                      'may': 5,
                      'june': 6,
                      'all': 7}

    month = ''
    while month not in MONTH_DATA.keys():
                print("\nPlease enter the month (from January to June) or type 'all' to select all months:")
                month = input().lower()

    if month in MONTH_DATA.keys():
                    print("\n"+ month.title()+" data will be called.")
                    print('-'*40)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS_DATA = {'monday': 1,
                    'tuesday': 2,
                    'wednesday': 3,
                    'thursday': 4,
                    'friday': 5,
                    'saturday': 6,
                    'sunday': 7,
                    'all':8}


    day = ''
    while day not in DAYS_DATA.keys():
                print("\nPlease enter the day (eg.monday) that you would like to select or type 'all' to select all days:")
                day = input().lower()

    if day in DAYS_DATA.keys():
                    print("\n"+ day.title()+" data will be called.")
                    print('-'*40)

    print(f"\nYou have selected: {city.upper()}, month: {month.upper()} and day: {day.upper()}.")

    print('-'*40)
    return city, month, day

def display_raw_data(df):
    """ Your docstring here """

    i = 0
    raw = input("\nWould you like to look at the database?").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5, :]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Would you like to see more of the data set?").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
      # convert the Start Time column to datetime
    start_time = time.time()

    # display the most common month
    #to load data
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # display the most common day of week
    # extract day
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print('Most Popular Day:', popular_day)


    # display the most common start hour
    # extract hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    commonly_used_start_station = df['Start Station'].mode()[0]
    print(f"\nThe most commonly used start station: {commonly_used_start_station}")

    # display most commonly used end station
    commonly_used_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {commonly_used_end_station}")

    #display most commonly used station combination
    df['combination'] = df['Start Station'].str.cat(df['End Station'], sep=' - ')
    commonly_used_combination = df['combination'].mode()[0]
    print(f"\nThe most commonly used combination of start and end stations: {commonly_used_combination}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print(f"\nTotal travel time by all users: {total_travel_time} mins")

    # display mean travel time
    avg_travel_time = df["Trip Duration"].mean()
    print(f"\nAverage travel time by all users: {avg_travel_time} mins")

    # display longest travel time
    longest_travel_time = df["Trip Duration"].max()
    print(f"\nLongest travel time by all users: {longest_travel_time} mins")

    # display shortet travel time
    shortest_travel_time = df["Trip Duration"].min()
    print(f"\nShortest travel time by all users: {shortest_travel_time} mins")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    #if the dataset does not have info about gender, skip this with an exception
    try:
        gender = df['Gender'].value_counts()
        print(gender)
    except:
        print(" Data for gender of users in this city is not available")

    # Display earliest, most recent, and most common year of birth
    #if the dataset does not have info about birthday, skip this with an exception
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
        print(f"Eaeliest year:{earliest_year}")
        print(f"Most Recent Year: {most_recent_year}")
        print(f"Most Common Year: {most_common_year}")

    except:
        print(" Data for birth year of users in this city is not available")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes to restart or press any key to exit.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
