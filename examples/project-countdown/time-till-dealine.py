import datetime

user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
# calculate how many days from now till deadtile

time_till = deadline_date - today_date
hours_till = int(time_till.total_seconds() / 60 / 60)

print(
    f"Dear user! Time remainning for your goal: {goal} is {hours_till} hours")
