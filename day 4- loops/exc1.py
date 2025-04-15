
calories_per_minute = 4.2


time_intervals = [10, 15, 20, 25, 30]


for time in time_intervals:
  calories_burned = calories_per_minute * time
  print(f"After {time} minutes, you burn calories {calories_burned} calories.")
  