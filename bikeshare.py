import time
import pandas as pd
import numpy as np

#Source data file
#chicago.csv contains data for Chicago city
#new_york_city.csv contains data for New York city
#washington.csv contains data for Washington city

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
	while True:
		print("\nEnter the city you are interested in:")
		city = input("1. Chicago\n2. New York City\n3. Washington\n> ").lower()
		if city not in CITY_DATA:
			print("\nWrong Input. Please try again!\n")
		else:
			break

	# TO DO: get user input for month (all, january, february, ... , june)
	while True:
		print("\nEnter the month you are interested in:")
		month = input("1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. All\n> ").lower()
		if month not in ["january", "february", "march", "april", "may", "june", "all"]:
			print("\nWrong Input. Please try Again!\n")
		else:
			break

	# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
	while True:
		print("\nEnter the day you are interested in:")
		day = input("1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n6. Saturday\n7. Sunday\n7. All\n> ").lower()
		if day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
			print("\nWrong Input. Please try Again!\n")
		else:
			break

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

	# load data file into a dataframe
	df = pd.read_csv(CITY_DATA[city])

	# convert the Start Time column to datetime
	df['Start Time'] = pd.to_datetime(df['Start Time'])

	# extract month and day of week from Start Time to create new columns
	df['month'] = df['Start Time'].dt.month
	df['day_of_week'] = df['Start Time'].dt.day_name()

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

	df['combo_station'] = df['Start Station'] + " - " + df['End Station']
	return df


def time_stats(df):
	"""Displays statistics on the most frequent times of travel."""

	print('\nCalculating The Most Frequent Times of Travel...\n')
	start_time = time.time()

	# TO DO: display the most common month
	common_month = df['month'].mode()[0]
	print("Most Common Month: ", common_month)

	# TO DO: display the most common day of week
	common_dow = df['day_of_week'].mode()[0]
	print("Most Common Day of Week: ", common_dow)

	# TO DO: display the most common start hour
	common_hour = df['Start Time'].dt.hour.mode()[0]
	print("Most Common Start Hour: ", common_hour)

	print("\nThis took %s seconds." % (time.time() - start_time))
	print('-'*40)


def station_stats(df):
	"""Displays statistics on the most popular stations and trip."""

	print('\nCalculating The Most Popular Stations and Trip...\n')
	start_time = time.time()

	try:
		# TO DO: display most commonly used start station
		start_station = df['Start Station'].mode()[0]
		print("Most Commonly Used Start Station: ", start_station)

		# TO DO: display most commonly used end station
		end_station = df['End Station'].mode()[0]
		print("Most Commonly Used End Station: ", end_station)

		# TO DO: display most frequent combination of start station and end station trip
		combo_station = df['combo_station'].mode()[0]
		print("Most Frequent Combination Of Start Station And End Station: ", combo_station)
	except KeyError:
		print("\nAn Error Occurred. No Data Available\n")

	print("\nThis took %s seconds." % (time.time() - start_time))
	print('-'*40)


def trip_duration_stats(df):
	"""Displays statistics on the total and average trip duration."""

	print('\nCalculating Trip Duration...\n')
	start_time = time.time()

	# TO DO: display total travel time
	travel_time = df['Trip Duration'].sum()
	print("Total Travel Time: ", travel_time, " seconds")

	# TO DO: display mean travel time
	mean_time = df['Trip Duration'].mean()
	print("Mean Travel Time: ", mean_time, " seconds")

	print("\nThis took %s seconds." % (time.time() - start_time))
	print('-'*40)


def user_stats(df):
	"""Displays statistics on bikeshare users."""

	print('\nCalculating User Stats...\n')
	start_time = time.time()

	try:
		# TO DO: Display counts of user types
		user_types = df['User Type'].value_counts()
		print("Count Of User Type:\n", user_types)

		# TO DO: Display counts of gender
		gender_count = df['Gender'].value_counts()
		print("\nCount Of Gender:\n", gender_count)

		# TO DO: Display earliest, most recent, and most common year of birth
		earliest_yob = int(df['Birth Year'].min())
		print("\nThis Is The Earliest Year Of Birth: ", earliest_yob)

		recent_yob = int(df['Birth Year'].max())
		print("This Is The Most Recent Year Of Birth: ", recent_yob)

		common_yob = int(df['Birth Year'].mode()[0])
		print("This Is The Most Common Year Of Birth: ", common_yob)

	except KeyError:
		print("\nAn Error Occurred. No Data Available.\n")

	print("\nThis took %s seconds." % (time.time() - start_time))
	print('-'*40)


def raw_data(df):
	"""Displays a set of next 5 rows until the user inputs 'no'."""
	choice = input("\nWould you like to view the first 5 rows? Enter yes or no.\n>")
	start, end = 0, 5
	while choice.lower() == "yes":
		print(df[start:end])
		choice = input("\nWould you like to view the next 5 rows? Enter yes or no.\n>")
		start, end = end, end+5


def main():
	while True:
		city, month, day = get_filters()
		df = load_data(city, month, day)

		time_stats(df)
		station_stats(df)
		trip_duration_stats(df)
		user_stats(df)
		raw_data(df)

		restart = input('\nWould you like to restart? Enter yes or no.\n>')
		if restart.lower() != 'yes':
			break


if __name__ == "__main__":
	main()
