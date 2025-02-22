import threading
import time
class Knight(threading.Thread):
    def __init__(self,name,power):
        threading.Thread. __init__(self)
        self.name=str(name)
        self.power=int(power)
        self.day = 0
        self.enemies = 100

    def run (self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            time.sleep(1)
            self.day += 1
            self.enemies -= self.power
            print(f'{self.name} сражается {self.day} дней(дня)..., осталось {self.enemies} воинов. ')
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()


print(f'Все битвы закончились!')



