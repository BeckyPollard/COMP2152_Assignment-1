# following instructions: https://github.com/sojoudian/COMP2152_Assignment-1/blob/master/Instructions1.md

"""
Author: Becky Pollard
Assignment: #1
"""

# STEP A: Do some silly box drawing decorative stuff because Becky likes having fun.
print("╔═════════════════════════════════════════════════════╗")
print("║                                                     ║")
print("║                    ☆ WORKOUTS ☆                     ║")
print("║                                                     ║")
print("╠═════════════════════════════════════════════════════╣")

# STEP B: Create 4 variables
gym_member = "Alex Alliton"  #string
preferred_weight_kg = 20.5  #float
highest_reps = 25  #integer
membership_active = True  #boolean

# STEP C: Create a dictionary named workout_stats
# dictionary: string keys and tuple values of int (yoga), int (running), int (weightlifting)
workout_stats = {
  "Loralie": (30, 45, 100),
  "Shalaka": (60, 150, 35),
  "Kaori": (10, 10, 10),
  "Becky": (10, 0, 10)
}

# STEP D: Calculate total workout minutes using a loop and add to dictionary
for friend, mins in list(workout_stats.items()):
  total_mins = sum(mins)
  workout_stats[f"{friend}_Total"] = total_mins

# STEP E: Create a 2D nested list called workout_list
# 2d list: is a list of lists that is storing workout information
# I decided to add the name so that the info could be useful
workout_list = []
for name, times in workout_stats.items():
  if '_Total' not in name:
    workout_list.append([name, *times])

# STEP F: Slice the workout_list
print("║ All friends yoga and running minutes")
for row in workout_list:
  print(f"║ ☆ {row[0]} = {row[1:3]}")
print(f"║")

print("║ Last two friends weightlifting minutes: ")
for row in workout_list[1:]:
  print(f"║ ☆ {row[0]} = {row[3]}")
print(f"║")

# STEP G: Check if any friend's total >= 120
print("║ Which friends have worked out for >= 120min?")
for times in workout_list:
  if sum(times[1:]) >= 120:
    print(f"║ ☆ Great job staying active, {times[0]}!")
print(f"║")

# STEP H: User input to look up a friend
print("║ SEARCH for a friend!")
searchName = input("║ Enter the name of a friend: ")
print(f"║")
if searchName in workout_stats:
  yoga, running, weightlifting = workout_stats[searchName]
  total = workout_stats[f"{searchName}_Total"]
  print(f"║ Workout details for {searchName.upper()}:")
  print(f"║ ☆ Yoga: {yoga} Minutes")
  print(f"║ ☆ Running: {running} Minutes")
  print(f"║ ☆ Weightlifting: {weightlifting} Minutes")
  print(f"║ ☆ Total: {total} Minutes")
else:
  print(f"║ ☆ Friend {searchName.upper()} not found in the records.")
print(f"║")

# STEP I: Friend with highest and lowest total workout minutes
print("║ Highest and lowest total workout minutes:")
totals = {}
for name in workout_stats:
  if '_Total' in name:
    totals[name] = workout_stats[f"{name}"]
highest = max(totals, key = totals.get)
lowest = min(totals, key = totals.get)
print(f"║ ☆ Highest total workout minutes: {highest.replace("_Total", "")}")
print(f"║ ☆ Lowest total workout minutes: {lowest.replace("_Total", "")}")
print(f"║")

# STEP J: Finish decorative junk
print("╚═════════════════════════════════════════════════════╝")

