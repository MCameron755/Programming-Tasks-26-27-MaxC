"""
TASK: 04 Temp Stats Csv

# Skills CSV read, simple maths
Go to this site https://www.metoffice.gov.uk/hadobs/hadcet/data/download.html and download the txt file
Daily Mean Temperature.
This file has dates and daily temperatures:
- Read all of the values
- Find the highest, lowest and average
- Print those three values
Extend - See how you can potentially use the dates to chart daily temp changes by years, by months
by day comparisons over time. Maybe chart them using mathplotlib or another library. Just see what you can do with it

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def calculatetempstats(filepath):
    temperatures = []
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.split()
            if not parts or len(parts) < 2:
                continue
            try:
                tempvalue = float(parts[1])
                temperatures.append(tempvalue)
            except ValueError:
                continue
    if not temperatures:
        print("No valid temperature data found.")
        return
    highesttemp = max(temperatures)
    lowesttemp = min(temperatures)
    averagetemp = sum(temperatures) / len(temperatures)
    print(f"Highest Temperature: {highesttemp}°C")
    print(f"Lowest Temperature: {lowesttemp}°C")
    print(f"Average Temperature: {averagetemp:.2f}°C")

calculatetempstats("meantemp_daily_totals.txt")