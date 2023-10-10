all_users=["sachin","rahul","rohit","kohli","dravid","laxman","ganguly"]
sachin_follwings=["rahul","ganguly","dravid"]

sachin_sugg=set(all_users).difference(set(sachin_follwings))
sachin_sugg.remove("sachin")
print(sachin_sugg)