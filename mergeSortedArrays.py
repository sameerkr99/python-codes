def main():
    l = [1,3,4,5,7,11,12]
    r = [2,6,8,9,10,13]
    out = []
    i,j = 0,0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            while i < len(l) and l[i] < r[j]:
                out.append(l[i])
                i += 1
        else:
            while j < len(r) and l[i] > r[j]:
                out.append(r[j])
                j += 1
    while i < len(l) :
        out.append(l[i])
        i += 1
    while j < len(r):
        out.append(r[j])
        j += 1
    print(out)
            

if __name__ == '__main__':
    main()