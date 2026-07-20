

rating = [[4, 5, 3, 2], [5, 4, 4, 3], [3, 2, 5, 5]]



lsst = [j for i in rating for j in i if j > 4]
print(lsst)

