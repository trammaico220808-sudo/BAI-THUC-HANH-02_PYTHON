text = list(input("Nhập một đoạn văn: ").split())
dau_cau =".,!,?"
text_moi = []
for i in text:
    tu = ""
    for j in i:
        if j not in dau_cau:
            tu += j
    if tu != "":
        text_moi.append(tu)
ket_qua = []
da_dem =[]
for i in text_moi:
    if i not in da_dem:
        ket_qua.append([i,text_moi.count(i)])
        da_dem.append(i)
for i in text_moi:
    if i not in da_dem:
        ket_qua.append([i,text_moi.count(i)])
        da_dem.append(i)
ket_qua.sort(key=lambda x: x[1],reverse=True)
for i in ket_qua:
     print(i[0],i[1])