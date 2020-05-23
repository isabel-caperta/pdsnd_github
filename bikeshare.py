# EXPLORE US BIKESHARE DATA WITH PYTHON
# This project uses Python to understand U.S. bikeshare data.
# It calculates statistics and builts an interactive environmente where a user chooses the data and filter for a dataset to analyze.

import time
import datetime
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
    print('\nHello there! Let\'s explore some US bikeshare data!\n')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York City or Washington?\n')
    city = city.lower()
    while city != 'chicago' and city != 'new york city' and city != 'washington':
        print('Looks like you have misspelled your option.\n')
        city = input('Please choose Chicago, New York City or Washington.\n')
        city = city.lower()
    print('Looks like you want to see the data for {}.\nIf this is not true, please restart the program.\n'.format(city.upper()))

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["January", "February", "March", "April", "May", "June"]
    month = input('Would you like to see data for a specific month? \nIf not type "All", otherwise specify the desired month: \n"January", "February", "March", "April", "May" or "June".\n')
    month = month.title()
    while month != 'All' and month not in months:
        print('Looks like you have misspelled your option.\n')
        month = input('Please type "All" or specify the desired month: \n"January", "February", "March", "April", "May" or "June".\n')
        month = month.title()
    print('You have chosen to see the data for {}.\n'.format(month.upper()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = input('Would you like to see data for a specific day of the week? \nIf not type "All", otherwise specify the desired day: \n"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" or "Sunday".\n')
    day = day.title()
    while day != 'All' and day not in days:
        print('Looks like you have misspelled your option.\n')
        day = input('Please type "All" or specify the desired day: \n"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" or "Sunday".\n')
        day = day.title()
    print("You have chosen the data for {}.\n".format(day.upper()))

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
    if month != 'All':
        months = ["January", "February", "March", "April", "May", "June"]
        month = months.index(month) + 1
        df = df[df['month'] == month]

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months = ["January", "February", "March", "April", "May", "June"]
    common_month = months[common_month - 1]
    print('Most common month: {}'.format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of the week: {}'.format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour: {}h00'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_st = df['Start Station'].mode()[0]
    print('Most commonly used start station: {}'.format(common_start_st))

    # TO DO: display most commonly used end station
    common_start_st = df['End Station'].mode()[0]
    print('Most commonly used end station: {}'.format(common_start_st))

    # TO DO: display most frequent combination of start station and end station trip
    common_combination_st = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    common_combination_st = common_combination_st.index[0]
    start_st, end_st = common_combination_st
    print('Most frequent combination trip: \n - Start station: {}\n - End station: {}.'.format(start_st, end_st))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    total_time = time.strftime('%H:%M:%S', time.gmtime(total_time))
    print('The total travel time is {} (hh:mm:ss)'.format(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    mean_time = time.strftime('%H:%M:%S', time.gmtime(mean_time))
    print('The average trip duration is {} (hh:mm:ss)'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts().to_string()
    print('Count of users by type:\n{}\n'.format(user_type))

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts().to_string()
    print('Count of users by gender:\n{}\n'.format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    current_year = datetime.datetime.now().year

    earliest_year = int(df['Birth Year'].min())
    recent_year = int(df['Birth Year'].max())
    common_year = int(df['Birth Year'].mode())
    print('Earliest user year of birth: {}\nThe oldest user is {} years old.\n'.format(earliest_year,(current_year-earliest_year)))
    print('Most recent user year of birth: {}\nThe youngest user is {} years old.\n'.format(recent_year,(current_year-recent_year)))
    print('Most commom user year of birth: {}\nThe most common user age is {} years old.'.format(common_year,(current_year-common_year)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    view_raw = input('\nWould you like to view individual trip data? Type \'yes\' or \'no\'.\n')
    while True:
        if view_raw.lower() != 'yes':
            break
        else:
            i = 0
            while i < len(df):
                i += 5
                if i >= len(df):
                    print('There is no more individual trip data for this query.\n')
                else:
                    pd.options.display.max_columns = 12
                    print (df.iloc[i-5 : i])
                    view_raw = input('\nWould you like to view 5 more individual trip data entries? Type \'yes\' or \'no\'.\n')
                    if view_raw.lower() != 'yes':
                        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != "washington":
            user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
