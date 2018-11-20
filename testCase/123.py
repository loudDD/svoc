class printhanshu():

    def printa(self,i):
        print(i)

    def diaoyong(self,i):
        for b in range(i):
            return printhanshu.printa(self,b)

printhanshu().diaoyong(5)