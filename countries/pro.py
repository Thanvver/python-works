from json import load
path="C:\\Users\\thanveer\\OneDrive\\Desktop\\luminar\\countries\\countries.json"

with open(path,encoding="utf-8") as f:
    countries=load(f)
    # print(len(countries))

country_name=[c.get("name") for c in countries]
# print(country_name)

capital_china=[c.get("capital") for c in countries if c.get("name")=="China"]
# print(capital_china)

regions=[c.get("region") for c in countries ]
# print(regions)

country_border=[c.get("borders") for c in countries if c.get("name")=="India"][0]
border_name=[c.get("name") for c in countries if c.get("alpha3Code") in country_border]
# print(border_name)

# print independant country
# print currency name of india

currency_name=[c.get("currencies") for c in countries if c.get("name")=="India"][0][0]
# print(currency_name.get("name"))

data=[c.get("name") for c in countries if "currencies" not in c]
# print(data)


country_currencies=[c for c in countries if "currencies" in c]
currencies=[c.get("currencies")[0].get("symbol  ") for c in country_currencies]
wc={}
for c in currencies:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1
print(max((v,k) for k,v in wc.items()))

# indpnt_country=[c.get("name") for c in countries if c.get("independant")==True]
# print(indpnt_country)