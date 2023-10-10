enquiries=["django","testing","django","bigdata","django","aws","aws","django"]

enquiry_count={}

for i in enquiries:
    if i in enquiry_count:
        enquiry_count[i]+=1
    else:
        enquiry_count[i]=1
print(enquiry_count)
