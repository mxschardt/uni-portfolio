
def calc_delta(timetable) -> float:
    delta = 0
    for (start, end) in timetable:
        delta += end - start
    return delta



def calc_time(func, args) -> list:
    import timeit
    
    timetable = [None] * len(args) 
    for i, n in enumerate(args):
        start_time = timeit.default_timer()
        func(*n)
        end_time = timeit.default_timer()
        timetable[i] = (start_time, end_time)

    return timetable


def setup_data(n: int, root=10) -> list:
    from random import randint
   
    min_height = 0
    max_height = 15
    data = [None] * n

    for i in range(n):
        data[i] = (randint(min_height, max_height), root)

    return data

