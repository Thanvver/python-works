from json import load

path="C:\\Users\\thanveer\\OneDrive\\Desktop\\luminar\\read_json\\data.json"

with open(path) as f:
    records=load(f)

print(records)

fw_names=[f.get("name") for f in records]
print(fw_names)

top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)

py_fw=[r.get("name") for r in records if r.get("language")=="python"]
print(py_fw)

be_fw=[r.get("name")for r in records if r.get("side")=="backend"]
print(be_fw)

top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)
