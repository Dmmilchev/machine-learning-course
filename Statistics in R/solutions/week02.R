# task 18
# x = 2
dbinom(2, 10, 1/6)

# x <= 2
pbinom(2, 10, 1/6)

# x >= 2
1 - pbinom(1, 10, 1/6)

# 3 <= x <= 8
pbinom(8, 10, 1/6) - pbinom(2, 10, 1/6)

# task 19
pgeom(10 - 1, 1/6)
1 - pgeom(5 - 1, 1/6)

# task 20
pnbinom(20 - 3, 3, 1/6)

# task 21
1 - choose(5,2)*choose(3,0)/choose(8,2)

# task 22
pbinom(2, 1500, 1/500)
pbinom(3, 1500, 1/500) - dbinom(0, 1500, 1/500)

# task 23
1 - pbinom(4, 10, 1/4)

# task 24
pbinom(137, 143, 0.92)
dbinom(137, 143, 0.92)

# task 25
pgeom(10 - 1, 0.03)
1 - pbinom(1, 50, 0.03)

# task 26
1 - phyper(1, 3, 97, 50)
