logs=["30 99 sign-in", "20 105 sign-out", "21 100 sign-in", "20 80 sign-in", "30 120 sign-out", "1 110 sign-in"]
maxspan=20
## Try1
# build a dict with a nested list to contain the input data - can use defaultdict from collections for this accumulation then convert back
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
{k for k,v in sessions.items() if v and v>maxspan}


## Try2 
# same with defaultdict - avoid the not in check
from collections import defaultdict
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
{k for k,v in sessions.items() if v and v>maxspan}
