import sys
path = r'C:\Users\MOHSEN\Desktop\Github Projects\bin-checker\bin-checker.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

needle = "async function stripeTokenTest(card,key){"
idx = content.find(needle)
end = content.find("function binTest", idx)
seg = content[idx:end]
lines = seg.split('\n')
for i, l in enumerate(lines):
    print(f"{i:3d}: {repr(l)}")
