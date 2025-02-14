class ProductOfNumbers(object):

    def __init__(self):
        self.prefix_products = [1]

    def add(self, num):
        if num == 0:
            self.prefix_products = [1]
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k):
        if k >= len(self.prefix_products):
            return 0
        return self.prefix_products[-1] // self.prefix_products[-k - 1]

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)