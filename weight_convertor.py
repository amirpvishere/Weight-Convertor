class Weight:
    def __init__(self, weight):
        self.weight = int(input("Enter Your weight: "))

    def grams_to_kilograms(self, weight):
        return self.weight/1000

    def kilograms_to_gram(self, weight):
        return self.weight*1000

    def pounds_to_gram(self, weight):
        return self.weight*454

    def gram_to_pounds(self, weight):
        return self.weight/454

    def gram_to_tonnes(self, weight):
        return self.weight/1000000

    def tonness_to_gram(self, weight):
        return self.weight*1000000

    def kilogram_to_tonnes(self, weight):
        return self.weight*1000

    def tonness_to_kilograms(self, weight):
        return self.weight/1000

    def ounces_to_gram(self, weight):
        return self.weight*28.35

    def gram_to_ounces(self, weight):
        return self.weight/28.35

    def miligrams_to_gram(self, weight):
        return self.weight/1000

    def gram_to_miligrams(self, weight):
        return self.weight*1000
