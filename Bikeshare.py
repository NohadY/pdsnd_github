import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#Funcations to get cities
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please write a city (chicago, new york city, washington) you want to check?")
        city = city.title()
        if city in ['Chicago', 'New York City', 'Washington']:
            break
        else:
            print("invalid input. Please try again")

    # TO DO: get user input for month (all, january, february, ... , june)
          
    while True:    
        month = input("Please select a specific month by typing the month name?")
        month = month.title()
        if month in ['January', 'February', 'March', 'April', 'May', 'June', 'All']:
            break
        else:
            print("invalid input.Please try again")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please specify a day? ")
        day = day.title()
        if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']:
            break
        else:
            print("invalid input.Please try again")

    print('-'*40)
    return city, month, day


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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is ", df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    print("The most common month is ", df['day_of_week'].mode()[0], "\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is ",df['hour'].mode()[0],"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is ",df['Start Station'].mode()[0],"\n")

    # TO DO: display most commonly used end station
    print("The most common end station is ",df['End Station'].mode()[0],"\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['Concatenate'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is ", df['Concatenate'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is ",df['Trip Duration'].sum(),"\n")

    # TO DO: display mean travel time
    print("The mean travel time is ",df['Trip Duration'].mean(),"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")

    # TO DO: Display counts of gender
    gen = df.groupby(['Gender'])['Gender'].count()
    print(gen)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
    print("The earliest year of birth is ", earliest, "\n")
    recent = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
    print("The most recent year of birth is ", recent, "\n")
    common = df['Birth Year'].mode()[0]
    print("The most common year of birth is ", common, "\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
