class Problem:
    def problems(self,string):
        a=[]
        a[:]=string
        for i in a:
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
                a.remove(i)
        print(a)
        return a
obj=Problem()
obj.problems("hipalaniappan")