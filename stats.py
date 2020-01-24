import csv


class Year:
    workouts = 0
    running_time = 0
    mileage = 0.0
    total_calories = 0
    longest_run = ''

    def add_run(self, time, distance, calories):
        self.workouts = self.workouts + 1
        self.running_time = self.running_time + int(time)
        self.mileage = self.mileage + distance
        self.total_calories = self.total_calories + calories
        if self.longest_run == '' or distance > self.longest_run:
            self.longest_run = distance

    def time_formatting(self):
        hours = i 
        return formatted_time

    def print_year(self):
        print(f"Total Workouts: {self.workouts}")
        minutes, seconds = divmod(self.running_time, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod (hours, 24 )
        formatted_time = f"{days}:{hours}:{minutes}:{seconds}"
        print(f"Total Time Running: {formatted_time}")
        print(f"Total Mileage: {self.mileage}")
        print(f"Total Calories Burned: {self.total_calories}")
        print(f"Longest Run: {self.longest_run}")


def parse_date(date):
    tmp = date.split('-')
    return int(tmp[0])


def time_to_seconds(time):
    tmp = time.split(':')
    return int(tmp[2]) + (int(tmp[1]) * 60) + (int(tmp[0]) * 3600)


race_number = 1 


def add_race(title, date, time, pace, distance, race_number):
    race = {
        "Title": title,
        "Date": date,
        "Time": time,
        "Pace": pace,
        "Distance": distance
    }
    races[race_number] = race

def print_races():
    while races:
        race = races.popitem()
        print(race)


annum2009 = Year()
annum2010 = Year()
annum2011 = Year()
annum2012 = Year()
annum2013 = Year()
annum2014 = Year()
annum2015 = Year()
annum2016 = Year()
annum2017 = Year()
annum2018 = Year()
annum2019 = Year()
annum2020 = Year()
races = {}


with open('garmin_running.csv') as csvfile:
    workouts = csv.DictReader(csvfile)
    for row in workouts:
        time = int(time_to_seconds(row["Time"]))
        year = parse_date(row["Date"])
        if year == 2009 and row["Activity Type"] == "Running":
            annum2009.add_run(time, float(row["Distance"]), int(row["Calories"]))
        if year == 2010 and row["Activity Type"] == "Running":
            annum2010.add_run(time, float(row["Distance"]), int(row["Calories"]))
        if year == 2011 and row["Activity Type"] == "Running":
            annum2011.add_run(time, float(row["Distance"]), int(row["Calories"]))
        if year == 2012 and row["Activity Type"] == "Running":
            annum2012.add_run(time, float(row["Distance"]), int(row["Calories"]))
        if year == 2013 and row["Activity Type"] == "Running":
            annum2013.add_run(time, float(row["Distance"]), int(row["Calories"]))
        if year == 2014 and row["Activity Type"] == "Running":
            annum2014.add_run(time, float(row["Distance"]), int(row["Calories"]))
        if year == 2015 and row["Activity Type"] == "Running":
            annum2015.add_run(time, float(row["Distance"]), int(row["Calories"]))
        if year == 2016 and row["Activity Type"] == "Running":
            annum2016.add_run(time, float(row["Distance"]), int(row["Calories"]))
        if year == 2017 and row["Activity Type"] == "Running":
            annum2017.add_run(time, float(row["Distance"]), int(row["Calories"]))
        if year == 2018 and row["Activity Type"] == "Running":
            annum2018.add_run(time, float(row["Distance"]), int(row["Calories"]))
        if year == 2019 and row["Activity Type"] == "Running":
            annum2019.add_run(time, float(row["Distance"]), int(row["Calories"]))
        if year == 2020 and row["Activity Type"] == "Running":
            annum2020.add_run(time, float(row["Distance"]), int(row["Calories"]))
        if "5k" in row["Title"]:
            add_race(row["Title"], row["Date"], row["Time"], row["Avg Pace"], float(row["Distance"]), race_number)
            race_number = race_number + 1
        if "10k" in row["Title"]:
            add_race(row["Title"], row["Date"], row["Time"], row["Avg Pace"], float(row["Distance"]), race_number)
            race_number = race_number + 1
        if "Half Marathon" in row["Title"] or "half marathon" in row["Title"]:
            add_race(row["Title"], row["Date"], row["Time"], row["Avg Pace"], float(row["Distance"]), race_number)
            race_number = race_number + 1
        if "Grand Blue" in row["Title"]:
            add_race(row["Title"], row["Date"], row["Time"], row["Avg Pace"], float(row["Distance"]), race_number)
            race_number = race_number + 1
print_races()
print("2009:")
annum2009.print_year()
print("2010:")
annum2010.print_year()
print("2011:")
annum2011.print_year()
print("2012:")
annum2012.print_year()
print("2013:")
annum2013.print_year()
print("2014:")
annum2014.print_year()
print("2015:")
annum2015.print_year()
print("2016:")
annum2016.print_year()
print("2017:")
annum2017.print_year()
print("2018:")
annum2018.print_year()
print("2019:")
annum2019.print_year()
print("2020:")
annum2020.print_year()
