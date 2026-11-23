import os
os.chdir(r'C:\Users\MOHSEN\Desktop\Github Projects\bin-checker')
path = 'bin-checker.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if logStripe exists
if "function logStripe" in content:
    print("logStripe already exists")
else:
    # Find where to insert logStripe - after logBin and logStripe functions
    # Look for the end of logStripe function
    start_idx = content.find("function logStripe(card,res){")
    if start_idx != -1:
        end_idx = content.find("function", start_idx+1)
        if end_idx != -1:
            # Insert new function after logStripe
            insert_pos = content.rfind("\nfunction", 0, end_idx)
            if insert_pos != -1:
                insert_pos = content.rfind("\n", 0, insert_pos) + 1
                new_func = "\nfunction logStripe(card,res){\n  var bin=String(card.number||'').slice(0,8);\n  var binMsg = bin + ' | ' + card.date + ' | CVV ' + card.cvv + ' | ' + card.country + ' -> ' + (res.hit ? 'HIT' : 'MISS') + ' | ' + res.msg;\n  appendLog(binMsg);\n}\n"
                content = content[:insert_pos] + new_func + content[insert_pos:]
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("Added logStripe function")
    else:
        print("logStripe function definition not found")