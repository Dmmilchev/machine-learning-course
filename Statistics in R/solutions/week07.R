# task 72
setwd("~/Desktop/ML/Statistics in R/solutions")

examAB <- read.table( "../data/examAB.txt", header=T )
x <- examAB$points[examAB$variant=="A"]
y <- examAB$points[examAB$variant=="B"]
t.test( x, y, alternative="greater" )

# task 73
reacttime <- read.table("../data/reacttime.txt", header=T)
x <- reacttime$before
y <- reacttime$after
t.test(x, y, alternative="greater")

# task 75
# а) Двойка наблюдения
# б) Независими извадки
# в) Двойка наблюдения
# г) Независими извадки

# task 76
n = 500

sim.equality <- function() {
  x <- rnorm(n, 5, 1)
  y <- rnorm(n, 5, 0.8)
  t.test(x, y)$p.value
}

res <- replicate(10000, sim.equality())
sum(res <= 0.05) / length(res)

# task 77
n = 500

sim.equality2 <- function() {
  x <- rnorm(n, 5, 1)
  y <- rnorm(n, 5.2, 1)
  t.test(x, y)$p.value
}

res <- replicate(10000, sim.equality2())
sum(res <= 0.05) / length(res)

# task 78
x <- c(26, 43)
n <- c(500, 540)
prop.test( x=x, n=n, alternative="less", correct=FALSE)

# task 79
x <- c(1.2, 1.3, 1.5, 1.4, 1.7, 1.8, 1.4, 1.3)
y <- c(1.4, 1.7, 1.5, 1.3, 2.0, 2.1, 1.7, 1.6)
t.test(x, y)$p.value