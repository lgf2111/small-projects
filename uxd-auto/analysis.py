# from collections import Counter
# with open('scoreboard.txt') as f:
#     scoreboard = eval(f.read())
# print(*sorted(scoreboard.items()), sep='\n')

import shelve
with shelve.open('db') as db:
    print(db['questions'])