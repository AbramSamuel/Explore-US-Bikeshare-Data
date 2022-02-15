# These are links i used to help for solving the Bikeshare Data project

#https://stackoverflow.com/questions/48590268/pandas-get-the-most-frequent-values-of-a-column/48590361
#https://stackoverflow.com/questions/62264821/validation-prompting-user-again-for-input-if-input-is-wrong


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all','january','february','march', 'april','may','june']

weekdays = ['all','monday','tuesday', 'wednesday', 'thursday','friday','saturday', 'sunday']

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

    city_name = ''
    while city_name.lower() not in CITY_DATA:

                city_name = input('\nEnter Name of the City: ').lower()
                # Terminate the loop once getting the right answer
                if city_name.lower() in CITY_DATA:
                    city = CITY_DATA[city_name.lower()]
                    break
                else:
                    print('\n Invalid City Name!!\n\n')

    # get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in months:
                month_name = input('\n\nEnter month(january, february, ... , june or all) to filter data in month: ').lower()
                # Terminate the loop once getting the right answer
                if month_name.lower() in months:
                    month = month_name.lower()
                    break

                else:
                    print('\n Invalid month choice!!\n\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in weekdays:
                day_name = input('\n\nEnter day (monday, tuesday, ... sunday or all) to filter data in day: ').lower()
                # Terminate the loop once getting the right answer
                if day_name.lower() in weekdays:
                    day= day_name.lower()
                    break

                else:
                    print('\n Invalid Weekday choice!!\n\n')

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

    # load data file into a dataframe.
    df = pd.read_csv(city)

      # convert the Start Time column to datetime.
    df['Start Time']= pd.to_datetime(df['Start Time'])

    #Extracting month from Start_Time.
    df['month']= df['Start Time'].dt.month

    #Extracting month from Start_Time.
    df['day_of_week'] =df['Start Time'].dt.weekday_name


    #Filter by month if applicable.
    if month !='all':
        #Using the index of months list to get the coresponding integer.
        month = months.index(month)

        #Filtering by month to creat the new dataframe.
        df = df.loc[df['month'] == month]


    #Filter by day if applicable.
    if month !='all':
        # Filtering by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]




    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.

    Args:
    df - pandas DataFrame containing data of city filtered by month and day.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Extracting the most common month.
    df['month']=df['Start Time'].dt.month
    # display the most common month.
    most_common_month = df['month'].mode()[0]
    print('\n\n The Most Common Month:', most_common_month)

    #Extracting the most common week.
    df['week'] = df['Start Time'].dt.weekday_name

    # display the most common day of week.
    most_common_week =df['week'].mode()[0]
    print('\n\n The Most Common week:', most_common_week)

    #Extracting hour from the start_time column to creat an hour column.
    df['hour']=df['Start Time'].dt.hour

    # display the most common start hour
    most_common_hour =df['hour'].mode()[0]
    print('\n\n The Most Common Hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Args:
    df - pandas DataFrame containing data of city filtered by month and day.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('\n\nThe Most Commonly Used Start Station:', most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('\n\nThe Most Commonly Used Start Station:', most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    most_frequent_trip = df['Start To End'].mode()[0]
    print('\n\n The Most Frequent Trip: ', most_frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Args:
        df - pandas DataFrame containing data of city filtered by month and day.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\n\nThe Total Travel Time :', total_travel_time)

    # display mean travel time
    mean_travel_time =  df['Trip Duration'].mean()
    print('\n\nThe Mean Travel Time :', total_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types =df['User Type'].value_counts()
    print('\n\nThe Count of User Types: ',user_types)


    # Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print('\n\nThe Count of User Gender: ',gender)

    # Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        print('\n\nThe Earliest Birth of Users: ',earliest_birth)

        most_recent_birth = df['Birth Year'].max()
        print('\n\nThe Most Recent Birth of Users: ',most_recent_birth)

        most_common_birth = df['Birth Year'].mode()[0]
        print('\n\nThe Most Common Birth of Users: ',earliest_birth)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    '''Display raw data on user request.

        Args:
        df - pandas DataFrame containing data of city filtered by month and day.
    '''

    start_loc = 0
    end_loc = 5
    #Asking user about seeing  the raw data
    view_display = input("Do you want to see the raw data?(yes/y or no/n): ").lower()

    if  view_display == 'yes' or  view_display == 'y':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':
                break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
