library(MASS)
?survey

# task 45
survey$Exer
barplot(table(survey$Exer))

# task 46
table(survey$Pulse)
pulse.interval <- cut(Pulse, breaks=seq(30,110,10))
pulse.interval
table(pulse.interval)

barplot( table(pulse.interval) )
hist(Pulse)
hist(Pulse, breaks=seq(30,110,5))

# task 48
v1 <- rep(4, 30)
v2 <- rep(c(3.5,4.5), 15)
v3 <- rep(c(3,5), 15)
v4 <- rep(c(2:6), 6)
v5 <- rep(c(2,6), 15)

median(v1, na.rm = T)
mean(v1, na.rm = T)
sd(v1, na.rm = T)

#...