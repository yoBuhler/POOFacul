from threading import Thread
from random import randint

class sum(Thread):
    def __init__(self, numbers):
        Thread.__init__(self)
        self.numbers = numbers
        self.subTotal = 0

    def run(self):
        for number in self.numbers:
            self.subTotal += number


numbers = []
for i in range(1000):
    numbers.append(randint(0, 9999))

sums = [sum(numbers[0:250]), sum(numbers[251:500]), sum(numbers[501:750]), sum(numbers[751:1000])]

for sum in sums:
    sum.start()

for sum in sums:
    sum.join()

total = 0
for sum in sums:
    print(sum.subTotal)
    total += sum.subTotal

print('O total da soma dos números é: {}'.format(total))
