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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print('choose a city to explore: chicago, new york city, washington...> ')
        city = input().lower()
        if city not in CITY_DATA.keys():
            print('\ninvalid city')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    months = ['all', 'february', 'march', 'april','may', 'june', 'january']
    while month not in months:
        print('which month you would like to see details on??: january, february, march, april, may, june or all...> ')
        month = input().lower()
        if month not in months:
            print('\ninvalid month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    days = ['all', 'monday', 'tuesday', 'wendsday', 'thursday', 'friday', 'sunday']
    while day not in days:
        print('choose a day: sunday, monday, tuesday, wendsay, thursday, friday or all ...> ')
        day = input().lower()
        if day not in days:
            print('\ninvalid day')

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

    if month != 'all':

        months = ['january', 'february', 'march', 'april','may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print(f"\nmost popular month: {popular_month}")

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_weekday = df['day_of_week'].mode()[0]
    print(f"\nmost popular day of week: {popular_weekday}")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"\npopular hour: {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f'most common start station: {start_station}')

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f'most common end station: {end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    group_station = df.groupby(['Start Station','End Station'])
    popular_combination = group_station.size().sort_values(ascending = False).head(1)
    print(f'most frequent combination: {popular_combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print(f'total travel time: { total_travel}')

    # TO DO: display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print(f'the mean travel time: {travel_mean}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f'count of user types: {user_types}')

    if city != 'washington':

        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print(f'count of gender: {gender}')

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        print(f'most common earliest year: {earliest}')

        recent = df['Birth Year'].max()
        print(f'most common recent year: {recent}')

        common_year = df['Birth Year'].mode()[0]
        print(f'most common year: {common_year}')


    print("\nThis took %s seconds." % int((time.time() - start_time)))
    print('-'*40)


def raw_input(df):
#     view raw details for user
    print('\ndata row on screen\n')

    row = 5
    print(df.head(row))

    while True:
#         convert user input to lower case
        details = input('want to load more details? yes or no... ').lower()
        if details == 'no':
            break
        elif details == 'yes':
#             add more 5 rows when user ask for more details
            row = row + 5
            print(df.iloc[row-5:row, :])
        else:
            print('\ntype yes to load more, or no to exit\n')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() !='no':
            restart = input('\nplease type yes to resart the program, or no to exit\n')
        elif restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
