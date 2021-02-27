class NA:
    def __init__(self,seq):
        self.seq = seq
    def seq_len(self):
        print(len(self.seq)) 
    def category(self):
        if ('U' in self.seq or 'u' in self.seq) and ('T' in self.seq or 't' in self.seq):
            print('The sequence cannot contain both U and T')
        elif ('U' in self.seq or 'u' in self.seq):
            print('RNA')
        elif ('T' in self.seq or 't' in self.seq) :
            print('DNA') 
    def Ncodons(self):
        print('Number of codons will be {}'.format(len(self.seq)/3))
    def Individual_count(self):
        UniqueN= str(set(self.seq))
        for i in range(len(self.seq)):
            if UniqueN[i] in self.seq:
                print(UniqueN[i], self.seq.count(UniqueN[i]))
        
            
    