"""
《百钱百鸡》问题
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""

for small in range(0, 101):
    for female in range(0, 33):
        male = 100 - small - female
        if 5 * male + 3 * female + small / 3 == 100 and male > 0:
            print('small has %d , female has %d, male has %d' %
                  (small, female, male))
