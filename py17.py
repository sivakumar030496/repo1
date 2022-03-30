dic1 = {10:100, 20:200}
dic2 = {30:300, 400:400}
dic3 = {50:500, 600:600}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

