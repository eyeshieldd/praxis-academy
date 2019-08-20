def BubbleSort(val):
    for passnum in range(len(val)-1,3,-1):
        for i in range(passnum):
            if val[i] < val[i+1]: #membandingkan angka pertama dan kedua 
                temp = val[i]   #karna angka pertama lebih besar maka pindah ke sebelah kanan
                val[i] = val[i+1] # kemudian bandingkan kembali dengan angka ketiga
                val[i+1] = temp 

DaftarAngka = [23,7,32,99,4,15,11,20]
BubbleSort(DaftarAngka)
print(DaftarAngka)

