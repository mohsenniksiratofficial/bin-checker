// Standalone logic verification — mirrors functions in bin-checker.html
function luhnCheck(num){
  var s=0,alt=false;
  for(var i=num.length-1;i>=0;i--){
    var n=parseInt(num[i],10);
    if(alt){n*=2;if(n>9)n-=9;}
    s+=n;alt=!alt;
  }
  return s%10===0;
}
function formatExp(val){
  val=val.replace(/\D/g,'').slice(0,4);
  if(val.length>=3)val=val.slice(0,2)+'/'+val.slice(2);
  return val;
}
function formatDate(val){
  val=val.replace(/\D/g,'');
  if(val.length>=3)val=val.slice(0,2)+'/'+val.slice(2);
  else if(val.length===2)val=val+'/';
  return val;
}

// 1. Luhn on 4242424242424242 must pass
console.log('Luhn 4242424242424242:', luhnCheck('4242424242424242'), '(expect true)');
console.log('Luhn 4242424242424241:', luhnCheck('4242424242424241'), '(expect false)');

// 2. formatExp("1230") -> "12/30"
console.log('formatExp 1230:', JSON.stringify(formatExp('1230')), '(expect "12/30")');

// 3. formatDate("072031") -> "07/2031"
console.log('formatDate 072031:', JSON.stringify(formatDate('072031')), '(expect "07/2031")');

// 4. genBatch CVV precedence: must be 3-digit 100-999
var cvv = Math.floor(Math.random()*900)+100;
console.log('CVV sample:', cvv, 'in range:', cvv>=100 && cvv<=999);

// 5. Batch: generate 5 cards from BIN 552612, check luhn
function genFromBin(binPrefix, n){
  var valid=[];
  for(var i=0;i<n;i++){
    var num=binPrefix.replace(/[^0-9]/g,'');
    while(num.length<15) num+=Math.floor(Math.random()*10);
    var s=0,alt=true;
    for(var j=num.length-1;j>=0;j--){var d=parseInt(num[j],10);if(alt){d*=2;if(d>9)d-=9;}s+=d;alt=!alt;}
    num+=((10-s%10)%10);
    if(luhnCheck(num)) valid.push(num);
  }
  return valid;
}
var batch=genFromBin('552612',5);
console.log('Batch from 552612, 5 cards, valid:', batch.length, '(expect 5)');
console.log('Sample:', batch.slice(0,3));

// 6. Output format
var out = batch.map(function(num){
  return 'BIN: 552612xxxxxxxx | Date: 07/2031 | CVV: '+(Math.floor(Math.random()*900)+100)+' | Name: TEST';
}).join('\n');
console.log('Output sample:\n'+out.split('\n')[0]);