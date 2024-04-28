import json

addressbook={}
addressbook['Karthik']={"Name":"Karthik","Address":"29, Janakiraman Street, KR reddy"}
addressbook['Imsa']={"Name":"Imsa","Address":"1, 665 Cordova street,Pasadena"}

jsondump=json.dumps(addressbook)
with open("C://Karthik//Learning//AI//Python//jsonfilewrite.json","w") as fl:
    fl.write(jsondump)
