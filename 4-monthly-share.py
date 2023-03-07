revenueString = '''SP – R$67.836,43
                   RJ – R$36.678,66
                   MG – R$29.229,88
                   ES – R$27.165,48
                   Outros – R$19.849,53'''

revenueString = revenueString.replace('.','')
revenueString = revenueString.replace(',','.')
revenueString = revenueString.replace("– R$",'')
revenueList = revenueString.split()
revenue = dict(zip(revenueList[::2],map(float,revenueList[1::2])))

state = input("insert state acronym: ")
if state in revenue:
    percentage = (revenue[state]/sum(revenue.values()))*100
    print(f"{state} accounted for {percentage:.2f}% of the supplier's monthly revenue.")
else:
    print("The desired state doesn't exist, or it wasn't discriminated in the monthly report.")