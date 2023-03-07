from json import load

with open("dados.json") as f:
    a = load(f)
    incomeByDay = {d["dia"]:d["valor"] for d in a if d["valor"]}

smallest = min(incomeByDay.items(),key=lambda x:x[1])
greatest = max(incomeByDay.items(),key=lambda x:x[1])
average = sum(incomeByDay.values())/len(incomeByDay)
aboveAverage = len([x for x in incomeByDay.values() if x > average])

print(f"{smallest[0]} was the day with the smallest revenue, {smallest[1]:.2f}.")
print(f"{greatest[0]} was the day with the greatest revenue, {greatest[1]:.2f}.")
print(f"There were {aboveAverage} days in which the revenue was above {average:.2f}, the monthly average.")