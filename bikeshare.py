import time
import pandas as pd
import numpy as np

def get_filters():

    """Capture user input that will be converted to a filter list for use as an input in later functions

    City name filter
    City filename filter
    Does city have gender/birth data filter
    Day, Month, None filter
    Day filter
    Month filter

    """

    #City Filter: Select which city and return file name and filter criteria of whether file contains gender and birthyear information to filter list

    city_names = {'1': ['Chicago', 'chicago.csv', 'y'], '2': ['New York City', 'new_york_city.csv', 'y'], '3': ['Washington', 'washington.csv', 'n']}

    get_city = input('Select a City: 1 = Chicago, 2 = New York City, 3 = Washington: ')

    is_city = get_city in city_names

    while is_city == False:
        get_city = input('Whoops!  Please entere the number of your choice: 1 = Chicago, 2 = New York City, 3 = Washington: ')
        is_city = get_city in city_names

    else:
        print("You selected: {}".format(city_names[get_city][0]))

        city_name = city_names [get_city][0]
        city_file = city_names[get_city][1]
        city_setting = city_names[get_city][2]

    #Day, Month, None Filter: Next get first level filter and return filter information to filter list

    dma_setting = 'All'

    #Subfilter by month

    month_names = {'1': ['January'], '2': ['February'], '3': ['March'], '4': ['April'], '5': ['May'], '6': ['June'], '7': ['All']}

    get_month = input('Select a month to filter by: 1 = Jan, 2 = Feb, 3 = Mar, 4 = April, 5 = May, 6 = June, 7= All: ')

    is_month = get_month in month_names

    while is_month == False:
        get_month = input('Whoops!  Please entere the number for the month of your choice: 1 = Jan, 2 = Feb, 3 = Mar, 4 = April, 5 = May, 6 = June: ')
        is_month = get_month in month_names

    else:
        print("You selected: {}".format(month_names[get_month][0]))

        month_setting = month_names[get_month][0]

    # #Subfilter by day

    day_names = {'1': ['Monday'], '2': ['Tuesday'], '3': ['Wednesday'], '4': ['Thursday'], '5': ['Friday'], '6': ['Saturday'], '7': ['Sunday'], '8': ['All']}

    get_day = input('Select a day to filter by: 1 = Mon, 2 = Tue, 3 = Wed, 4 = Thur, 5 = Fri, 6 = Sat, 7 = Sun, 8 = All: ')

    is_day = get_day in day_names

    while is_day == False:
        get_day = input('Whoops!  Please enter the number for the day of your choice: 1 = Mon, 2 = Tue, 3 = Wed, 4 = Thur, 5 = Fri, 6 = Sat, 7 = Sun: ')
        is_day = get_day in day_names

    else:
        print("You selected: {}".format(day_names[get_day][0]))

        day_setting = day_names[get_day][0]



    #Return the filter list for use in next function

    filter = [city_name, city_file, city_setting, dma_setting, day_setting, month_setting]
    return filter

def get_city_data(city_filters):
    """
    Using the filters as inputs to create the dataframe for the city data summary and analyss
    """

    city_name = city_filters[0]
    city_file = city_filters[1]
    city_setting = city_filters[2]
    dma_setting = city_filters[3]
    day_setting = city_filters[4]
    month_setting = city_filters[5]

    print('-'*40)
    print("Let's look at the data for the following settings: \nCity: {} \nMonth Setting: {} \nDay Setting: {}".format(city_name, month_setting, day_setting))
    print('-'*40)

    # load data file into a dataframe
    city_df = pd.read_csv(city_file)

    # convert the Start Time column to datetime
    city_df['Start Time'] = pd.to_datetime(city_df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    city_df['Month'] = city_df['Start Time'].dt.month
    city_df['Day'] = city_df['Start Time'].dt.dayofweek
    city_df['Hour'] = city_df['Start Time'].dt.hour

    # filter by month if applicable
    if month_setting != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month_setting = months.index(month_setting) + 1

        # filter by month to create the new dataframe
        city_df = city_df[city_df['Month'] == month_setting]

    # filter by day of week if applicable
    if day_setting != 'All':
        # filter by day of week to create the new dataframe

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_setting = days.index(day_setting)

        city_df = city_df[city_df['Day'] == day_setting]

    return city_df


def time_stats(city_df, city_filters):

    city_name = city_filters[0]
    city_file = city_filters[1]
    city_setting = city_filters[2]
    dma_setting = city_filters[3]
    day_setting = city_filters[4]
    month_setting = city_filters[5]

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

#---Popular Travel Times 1 - Most Popular Month

    pop_month = city_df['Month'].mode()[0]
    month_name = ['January', 'February', 'March', 'April', 'May', 'June']
    pop_month_output = month_name[pop_month - 1]
    print("Most popular month: {}".format(pop_month_output))

#---Popular Travel Times 2 - Most Popular Day

    pop_day = city_df['Day'].mode()[0]
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pop_day_output = day_name[pop_day]
    print("Most popular day: {}".format(pop_day_output))

#---Popular Travel Times 3 - Most Popular Hour

    pop_hour = city_df['Hour'].mode()[0]
    if pop_hour > 12:
        pop_hour_output = pop_hour - 12
        print("Most popular start time: {}pm".format(pop_hour_output))
    if pop_hour == 12:
        print("Most popular start time: {}pm".format(pop_hour))
    if pop_hour < 12:
        print("Most popular start time: {}am".format(pop_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return

def station_stats(city_df, city_filters):

    city_name = city_filters[0]
    city_file = city_filters[1]
    city_setting = city_filters[2]
    dma_setting = city_filters[3]
    day_setting = city_filters[4]
    month_setting = city_filters[5]

    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #---Most common start station

    mode_start = city_df['Start Station'].mode()
    print("Most popular start station: {}".format(mode_start))

    #---Most common end station

    mode_stop = city_df['End Station'].mode()
    print("Most popular stop station: {}".format(mode_stop))

    #---Most common strip start + end combo

    grouped_df = city_df.groupby(['Start Station'] + ['End Station'])['End Station'].count()
    route_count = grouped_df.max()

    max_key = grouped_df.idxmax()

    print('Most common route: {}'.format(max_key))
    print('Count for most common route: {}'.format(route_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return

def trip_stats(city_df, city_filters):

    city_name = city_filters[0]
    city_file = city_filters[1]
    city_setting = city_filters[2]
    dma_setting = city_filters[3]
    day_setting = city_filters[4]
    month_setting = city_filters[5]

    print('Calculating Trip Duration...\n')
    start_time = time.time()

    #---Total travel time

    total_travel = city_df['Trip Duration'].sum() / 60
    print('Total trip duration: {} minutes'.format(total_travel))

    #---Average trip travel time

    '''Convert trip times to minutes instead of seconds'''

    avg_travel = city_df['Trip Duration'].mean()/60
    print('Average trip duration: {} minutes'.format(avg_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return

def user_stats(city_df, city_filters):

    city_name = city_filters[0]
    city_file = city_filters[1]
    city_setting = city_filters[2]
    dma_setting = city_filters[3]
    day_setting = city_filters[4]
    month_setting = city_filters[5]

    print('Calculating User Stats...\n')
    start_time = time.time()

    #---Count by user types
    user_types = city_df['User Type'].value_counts()
    print('Here is a breakdown of users by customer category: \n{}'.format(user_types))
    print('-'*40)


    #---Counts by gender, only available for Chicago and NYC

    if city_setting != 'n':
        gender = city_df['Gender'].value_counts()
        print('Here is a breakdown of users by gender: \n{}'.format(gender))

        print('-'*40)

    #---Birth Year: Earliest, Most Recent, Most common

    if city_setting != 'n':
        pop_birth = city_df['Birth Year'].mode()
        print('Here is the most common birthyear: \n{}'.format(int(pop_birth)))

        print('-'*40)

    if city_setting != 'n':
        max_birth = city_df['Birth Year'].max()
        print('Here is the most recent birthyear: \n{}'.format(int(max_birth)))

        print('-'*40)

        min_birth = city_df['Birth Year'].min()
        print('Here is the oldest birthyear: \n{}'.format(int(min_birth)))

        ## Add joke if min_birth birth year is prior to 1900

        if min_birth < 1900:
            print('Gee, I guess biking really helps you live longer!')

        print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return

def user_data(city_df, city_filters):

    city_name = city_filters[0]
    city_file = city_filters[1]
    city_setting = city_filters[2]
    dma_setting = city_filters[3]
    day_setting = city_filters[4]
    month_setting = city_filters[5]

    #Display raw user data five lines at a time.

    access = input("Would you like to view user data? Y or N: ").title()

    #Reindexing the dataframe: Got this from thatascience.com/learn-pandas/reset-index/

    city_df.reset_index(drop=True, inplace = True)

    i = 0
    j = 4
    while access != 'N':
        print(city_df.loc[i:j,:])
        i = j + 1
        j = i + 4
        access = input('Would you like to see the next five rows? \n Enter any key to continue or enter N to exit: ').title()

def main():
    while True:

        #Get dataframe:
        city_filters = get_filters()
        df = get_city_data(city_filters)

        #Display data output:
        time_stats(df, city_filters)
        station_stats(df, city_filters)
        trip_stats(df, city_filters)
        user_stats(df, city_filters)
        user_data(df, city_filters)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
