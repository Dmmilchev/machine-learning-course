# task 32
x <- runif(500, min=2, max=3)
hist(x)

x <- runif(5000, min=2, max=3)
hist(x, probability=T)
curve(dunif(x, min=2, max=3), from=2, to=3, add=T, lwd=2)

# task 33
x <- rexp(500, rate=1/7)
hist(x, probability=T)
curve(dexp(x, rate=1/7), from=0, to=100, add=T, lwd=3)

x <- rexp(5000, rate=1/7)
hist(x, probability=T)
curve(dexp(x, rate=1/7), from=0, to=100, add=T, lwd=3)

# task 34
x <- rnorm(500, mean=0, sd=1)
hist(x, probability=T)
curve(dnorm(x, mean=0, sd=1), from=min(x), to=max(x), add=T, lwd=3)


x <- rnorm(5000, mean=0, sd=1)
hist(x, probability=T)
curve(dnorm(x, mean=0, sd=1), from=min(x), to=max(x), add=T, lwd=3)

# task 35
punif(250, min=248, max=255)

qunif(0.05, 248, 255)

# task 36
1 - pexp(10, 1/10)
pexp(11, 1/10) - pexp(7, 1/10)
qexp(0.03, 1/10)

# task 37
1 - pnorm(51, 41, 5)
pnorm(50, 41, 5) - pnorm(45, 41, 5)
qnorm(0.99, 41, 5)

# task 38
x <- rnorm(5000, 252, 3)
sum(x >= 250) / length(x)

1 - pnorm(250, 252, 3)

