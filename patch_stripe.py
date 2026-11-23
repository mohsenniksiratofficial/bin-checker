import os
os.chdir(r'C:\Users\MOHSEN\Desktop\Github Projects\bin-checker')
path = 'bin-checker.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

needle = "async function stripeTokenTest(card,key){"
idx = content.find(needle)
end = content.find("function binTest", idx)
seg = content[idx:end]

new_seg = """async function stripeTokenTest(card,key){
  var exp=splitExp(card.date);
  if(!exp.month||!exp.year){return{hit:false,msg:'bad date'}};
  var body='card[number]='+encodeURIComponent(card.number)
    +'&card[cvc]='+encodeURIComponent(card.cvv)
    +'&card[exp_month]='+encodeURIComponent(exp.month)
    +'&card[exp_year]='+encodeURIComponent(exp.year);
  try{
    var r=await fetch('https://api.stripe.com/v1/tokens',{
      method:'POST',
      headers:{
        'Content-Type':'application/x-www-form-urlencoded',
        'Authorization=[redacted]+key
      },
      body:body
    });
    var j=await r.json();
    var res;
    if(j&&j.error){
      res={hit:false,msg:(j.error.code||j.error.type||'error')+' - '+(j.error.message||'')};
    } else if(j&&j.card){
      res={hit:true,msg:'token ok · '+(j.card.brand||'')+' · '+(j.card.funding||'')+' · '+(j.card.country||'')};
    } else {
      res={hit:false,msg:'unexpected response' + ' (HTTP '+r.status+')'};
    }
    logStripe(card,res);
    return res;
  }catch(e){
    var res={hit:false,msg:'net error: '+e.message};
    logStripe(card,res);
    return res;
  }
}"""

content = content[:idx] + new_seg + content[end:]
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced stripeTokenTest with logging")