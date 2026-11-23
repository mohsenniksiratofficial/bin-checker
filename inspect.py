path = r'C:\Users\MOHSEN\Desktop\Github Projects\bin-checker\bin-checker.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find("async function stripeTokenTest")
print("FOUND AT:", idx)
if idx != -1:
    end = content.find("function binTest", idx)
    print("END AT:", end)
    segment = content[idx:end]
    print("SEGMENT START:")
    print(segment[:300])
    print("SEGMENT END:")
    print(segment[-300:])
