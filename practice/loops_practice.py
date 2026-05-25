import random
import time

MAX_LOAD = 85
ITERATIONS = 10
DELAY = 0.2


class Solution:

    @staticmethod
    def numbers_practice():
        numbers = list(range(1, 8))
        for n in numbers:
            print(n)
            if n == 5:
                break

    @staticmethod
    def words_practice():
        words = [f"str{i}" for i in range(10)]
        for word in words:
            print(word)

    @staticmethod
    def monitor_rostics_load():
        iteration = 1
        while iteration <= ITERATIONS:
            load = random.randint(0, 100)
            message = f"Iteration: {iteration}, load: {load}%."
            if load > MAX_LOAD:
                message += f" Warning! Load is more than {MAX_LOAD}%!"
            print(message)
            time.sleep(DELAY)
            iteration += 1


Solution.numbers_practice()
Solution.words_practice()
Solution.monitor_rostics_load()
