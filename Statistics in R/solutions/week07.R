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

# task 74
