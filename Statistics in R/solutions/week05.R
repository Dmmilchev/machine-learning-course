# task 56

e03sum <- replicate( 10000, sum( rexp(3, 1/5) ) )
e07sum <- replicate( 10000, sum( rexp(7, 1/5) ) )
e10sum <- replicate( 10000, sum( rexp(10, 1/5) ) )
e30sum <- replicate( 10000, sum( rexp(30, 1/5) ) )
e90sum <- replicate( 10000, sum( rexp(90, 1/5) ) )
e200sum <- replicate( 10000, sum( rexp(200, 1/5) ) )

hist(e03sum)
hist(e07sum)
hist(e10sum)
hist(e30sum)
hist(e90sum)
hist(e200sum)

# task 57
e03sum <- replicate( 10000, sum( rexp(3, 1/5) ) / 3)
e07sum <- replicate( 10000, sum( rexp(7, 1/5) ) / 7)
e10sum <- replicate( 10000, sum( rexp(10, 1/5) ) / 10)
e30sum <- replicate( 10000, sum( rexp(30, 1/5) ) / 30)
e90sum <- replicate( 10000, sum( rexp(90, 1/5) ) / 90)
e200sum <- replicate( 10000, sum( rexp(200, 1/5) ) / 200)

hist(e03sum)
hist(e07sum)
hist(e10sum)
hist(e30sum)
hist(e90sum)
hist(e200sum)

# task 58
e03sum <- replicate( 10000, sum( runif(3, 1/5) ) / 3)
e07sum <- replicate( 10000, sum( runif(7, 1/5) ) / 7)
e10sum <- replicate( 10000, sum( runif(10, 1/5) ) / 10)
e30sum <- replicate( 10000, sum( runif(30, 1/5) ) / 30)
e90sum <- replicate( 10000, sum( runif(90, 1/5) ) / 90)
e200sum <- replicate( 10000, sum( runif(200, 1/5) ) / 200)

hist(e03sum)
hist(e07sum)
hist(e10sum)
hist(e30sum)
hist(e90sum)
hist(e200sum)

# task 59
x <- (900 - 980) / (900*10)
1 - pnorm(x)

# task 60
b <- (35-30)/(60/(sqrt(12)*sqrt(50)))
a <- (25-30)/(60/(sqrt(12)*sqrt(50)))
pnorm(b) - pnorm(a)

# task 61
raisins = c(4:7)
prob = c(0.2, 0.4, 0.3, 0.1)
mu = sum(raisins*prob)
var = sum(raisins*raisins*prob) - mu*mu
x <- (5.5 - mu)/(sqrt(var)/7)
1 - pnorm(x)

# task 62
x <- (4000 - 160*24)/(7*sqrt(160))
1 - pnorm(x)

# task 63
x1 <- (5.5 - 5)/(5/sqrt(80))
x2 <- (4.5 - 5)/(5/sqrt(80))
pnorm(x1) - pnorm(x2)

