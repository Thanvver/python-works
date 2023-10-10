years=[y for y in range(1800,2025)]
# print(years)

# century_year=[y for y in years if y%100==0]
# print(century_year)

noncentrury_years=[y for y in years if y%100!=0]
print(noncentrury_years)