def str_(l):
    l.append("a")


def nomer(n):
    n += 1



if __name__=='__main__':
    lis = ['asd', 'zxcv', 'zxcvfds']
    str_(lis)
    print(*lis)

    x = 0
    nomer(x)
    print(x)
