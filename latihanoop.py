class AkunBank: 
    def __init__(self, saldo): 
        self.__saldo = saldo  # Private attribute 
 
    def cek_saldo(self): 
        return self.__saldo 
 
    def setor(self, jumlah): 
        if jumlah > 0: 
            self.__saldo += jumlah 
    def tarik(self, jumlah): 
        if 0 < jumlah <= self.__saldo: 
            self.__saldo -= jumlah  
 
rekening = AkunBank(1000) 
rekening.setor(500) 
print(rekening.cek_saldo()) # Output: 1500 
 