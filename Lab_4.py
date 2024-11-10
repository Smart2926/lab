class Perfume: 
    sold_bottles = 0

    def __init__(self, volume=0, price=0.0, manufacturer="", public_numeric=0, public_string="", bottles_sold=0):
        self.__volume = volume
        self.__price = price
        self.__manufacturer = manufacturer
        self.public_numeric = public_numeric
        self.public_string = public_string
        self.bottles_sold = bottles_sold

        Perfume.sold_bottles += 1

    def get_volume(self): 
        return self.__volume

    def set_volume(self, volume): 
        self.__volume = volume

    def get_price(self): 
        return self.__price

    def set_price(self, price): 
        self.__price = price

    def get_manufacturer(self): 
        return self.__manufacturer

    def set_manufacturer(self, manufacturer): 
        self.__manufacturer = manufacturer

    def __str__(self):
        return f"{self.__manufacturer}: {self.__volume}ml, {self.__price} UAH, Sold: {self.bottles_sold} bottles"

    def __repr__(self):
        return f"Perfume({self.__volume}, {self.__price}, '{self.__manufacturer}', {self.public_numeric}, '{self.public_string}', {self.bottles_sold})"

    def __del__(self):
        print(f"Deleting Perfume: {self.__manufacturer}")

def get_total_bottles_sold(perfumes):
    total_bottles_sold = 0
    for perfume in perfumes:
        total_bottles_sold += perfume.bottles_sold
    return total_bottles_sold

def least_sold_perfume(perfumes):    
    least_sold = perfumes[0]
    for perfume in perfumes:
        if perfume.bottles_sold < least_sold.bottles_sold:
            least_sold = perfume
    print("Perfumes with the fewest bottles sold:")
    print(least_sold)
    
def main():
    perfumes = [
        Perfume(50, 500, "Chanel", 1, "Classic", 5),
        Perfume(100, 700, "Dior", 2, "Luxury", 3),
        Perfume(30, 300, "Gucci", 3, "Trendy", 2)
    ]

    for perfume in perfumes:
        print(perfume)

    print(f"Total bottles sold: {get_total_bottles_sold(perfumes)}")

    least_sold_perfume(perfumes)

#if __name__ == "__main__":
main()
