from sys import stdin


def f(x):
    return str(x+1)

def relax(e, d, p):
    if d[e[0]] > d[e[1]] + e[2]:
        d[e[0]] = d[e[1]] + e[2]
        p[e[0]] = e[1]
    return d, p

def ford(es, d, p, n):
    for _ in range(n):
        for e in es:
            d, p = relax(e, d, p)
    return d, p

def main():
    n = int(stdin.readline().strip())
    xs = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]
    es = [(to, frm, w)  for frm, x in enumerate(xs) for to, w in enumerate(x) if w != 10**5]
    es += [(i, n, 0) for i in range(n)]
    # pprint(es)
    d = [float('+inf')] * (n+1)
    d[n] = 0
    p = [float('+inf')] *(n+1)

    # first Ford
    d, p = ford(es, d, p, n)

    copy_d = d[:]

    # second Ford
    d, p = ford(es, d, p, n)

    # search d[i] != copy_d[i]
    res = 'NO'
    for i in range(n):
        if d[i] != copy_d[i]:
            v = i
            # v = number the first bad
            # search cycle with i
            path = [v]
            while p[v] not in path:
                v = p[v]
                path.append(v)
            # choice only cycle
            path = [p[v]] + path[path.index(p[v])+1:][::-1]
            res = 'YES'
            break
    print(res)
    if res == 'YES':
        print(len(path))
        print(' '.join(map(f, path)))

if __name__ == '__main__':
    main()

