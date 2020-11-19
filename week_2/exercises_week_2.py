message = type("All work but no play makes jack dull")
print(message)

#dddddd
print(6 * (1 - 2))

bruce = 6
print(bruce + 4)

principal_amount = int(1000)
interest_rate = float(0.01)
nmbr_years = int(5)
payout_frequency = int(1)
final_amount = principal_amount * (1 + (interest_rate / payout_frequency))**(payout_frequency * nmbr_years)

response = input("What is the principal amount?")
principal_amount = float(response)
interest_rate = float(0.01)
nmbr_years = float(5)
payout_frequency = float(1)
final_amount = principal_amount * (1 + (interest_rate / payout_frequency))**(payout_frequency * nmbr_years)

5 % 2 #1
9 % 5 #4
15 % 12 #3
12 % 15 #12
6 % 6 #0
0 % 7 #0


current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int
final_answer = final_time_int % 24

print("The time after waiting is: ", final_answer)