import json

x = '{"dateRep","countriesAndTerritories","cases","deaths"}'

v = json.loads(x)

print("The Records of Covid Cases",v)
print("Date Reported: ", v['dateRep'])
print("Countries and Territories: ", v['countriesAndTerritories'])
print("Number of Cases: ", v['cases'])
print("Number of Deaths: ", v['deaths'])