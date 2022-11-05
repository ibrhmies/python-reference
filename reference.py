# value types => string , number
x = 10
y = 80

x = y

y = 60

print(x,y)

#-> value types'larda atamalardan sonra yaptığımız değişiklikler önce yaptığımız atamayı etkilemez.

#reference types => list

a = ["ford","honda"]
b = ["ford","honda"]

a = b

b[0] = "opel"

print(a,b)

# reference types larda bir eşitleme söz konusu olduğunda o 
# listelerin adresleri eşitlenir sonradan değerlerde yapılan 
# değişikliklerde adresler eşit olduğu için değerler eşitlenir.
