from collections import defaultdict
import time

# decorator function to check elapsed time
def elapsed_time(f):
    def wrapper():
        t1=time.time()
        f()
        t2=time.time()
        print("time elapsed: ", ((t2-t1)*1000), "ms")
    return wrapper

@elapsed_time
def check_session1(logs, maxspan):
    ## Try1
    # build a dict with a nested list to contain the input data
    nested_dl = {}
    for e in logs:
        if int(e.split(' ')[0]) not in nested_dl:
            nested_dl[int(e.split(' ')[0])] = []
        nested_dl[int(e.split(' ')[0])].append(int(e.split(' ')[1]))
    # new dict to hold session info
    sessions = nested_dl.fromkeys(nested_dl.keys())
    # calc and store session info
    for k,v in nested_dl.items():
        try:
            if v[1]:
                sessions[k] = abs(v[1]-v[0])
        except IndexError:
            print("no second value for ID", k)

        # print sorted IDs where session > maxspan - use sets
        print({k for k,v in sessions.items() if v and v>maxspan})

@elapsed_time
def check_session2(logs, maxspan):
    ## Try2
    # same with defaultdict - avoid the 'not in' check
    nested_defd = defaultdict(list)
    for e in logs:
        nested_defd[int(e.split(' ')[0])].append(int(e.split(' ')[1]))

    # new dict to hold session info
    sessions = nested_defd.fromkeys(nested_defd.keys())
    # calc and store session info
    for k,v in nested_defd.items():
        try:
            if v[1]:
                sessions[k] = abs(v[1]-v[0])
        except IndexError:
            print("no second value for ID", k)

        # print sorted IDs where session > maxspan - use sets
        print({k for k,v in sessions.items() if v and v>maxspan})

def main():
    logs=["30 99 sign-in", "20 105 sign-out", "21 100 sign-in", "20 80 sign-in", "30 120 sign-out"]
    maxspan=20
    check_session1(logs, maxspan)
    check_session2(logs, maxspan)

if __name__ == '__main__': main()
