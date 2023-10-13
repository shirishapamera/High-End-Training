#hierarchical inheritance
class Siva:
    def gold (warangal):
        print("price 5L")
    def car(warangal):
        print("price 3L");
class Baby1(Siva):
    def bank(warangal):
        print("deposited 2L")      
class Baby2(Siva):
    def jewels(warangal):
        print("price 10L")       
b1=Baby1()
b1.bank()
b1.car()
b1.gold()
b2=Baby2()
b2.jewels()
b2.gold()
b2.car()