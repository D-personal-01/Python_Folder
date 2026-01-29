dic={"hello":"world",1343:2321,"python":"rocks",3.14:"pi",True:"bool",None:"nothing"}

print(type(dic))

print(dic[1343])

print(dic.get(1343))

print(dic.keys())

print(dic.values())

print(dic.items())

print("------------------------------")

for key,value in dic.items():

    print(key,":",value)

print("------------------------------")

for key in dic.keys():

    print(key,":",dic.get(key))

print("------------------------------")

dic[1343]="new_value"

dic["Hello"]="World"

print(dic)

