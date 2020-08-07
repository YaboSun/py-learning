from concurrent.futures.thread import ThreadPoolExecutor
def print_hello():
    print("hello")
with ThreadPoolExecutor(max_workers=4) as t:
    task1 = t.submit(print_hello(), 1)
    task2 = t.submit(print_hello(), 2)
    task3 = t.submit(print_hello(), 3)
    task4 = t.submit(print_hello(), 4)

    print(f"task1:{task1.done()}")
    print(f"task2:{task2.done()}")
    print(f"task3:{task3.done()}")
    print(f"task4:{task4.done()}")

