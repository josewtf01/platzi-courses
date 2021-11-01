import time

class FiboIter():

    def __init__(self, limit=None):
        self.limit = limit


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.limit:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1 , self.n2 = self.n2 , self.aux
                self.counter += 1
                return self.aux
        else:
            if self.counter == 0 and self.n1 <= self.limit:
                self.counter += 1
                return self.n1
            elif self.counter == 1 and self.n2 <= self.limit:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                if self.aux >= self.limit+1:
                    raise StopIteration
                self.counter += 1
                return self.aux

def run():
    fibonacci = FiboIter(22)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)

if __name__ == "__main__":
    run()