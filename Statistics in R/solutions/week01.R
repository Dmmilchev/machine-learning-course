# task 1
sim.balls1 <- function() {
  x <- sample(c(1:8), 2, replace=TRUE)
  x[1] == x[2]
}

res <- replicate(100000, sim.balls1())
sum(res)/length(res)

# task 2
sim.socks <- function() {
  x <- sample(c(1, 1, 2, 2, 3, 3), 2, replace = FALSE)
  x[1] == x[2]
}

res <- replicate(100000, sim.socks())
sum(res) / length(res)

# task 3
sim.keys <- function() {
  x <- sample(c(1, 2, 3, 4), 4, replace = FALSE)
  x[4] == 4 # doesn't matter if it is 4 or anything else
}

res <- replicate(100000, sim.keys())
sum(res) / length(res)

# task 4
sim.exam  <- function() {
  questions = c(rep(1, 17), rep(0, 3))
  x <- sample(questions, 2, replace = FALSE)
  sum(x) == 1
}

res <- replicate(100000, sim.exam())
sum(res) / length(res)

# task 5
sim.birthday <- function() {
  x <- sample(c(1:365), 25, replace = TRUE)
  any(duplicated(x))
}

res <- replicate(100000, sim.birthday())
sum(res) / length(res)

# task 6 (not the best solution but still...)
sim.gifts <- function() {
  x <- sample(c(1:20), 20, replace = FALSE)
  for (i in c(1:20)) {
    if (x[i] == i) {
      return(1)
    }
  }
  return(0)
}

res <- replicate(100000, sim.gifts())
sum(res) / length(res)

# task 7
sim.ants <- function() {
  a1 <- sample(c(1, 2), 1)
  a2 <- sample(c(1, 3), 1)
  a3 <- sample(c(3, 2), 1)
  !any(duplicated(c(a1, a2, a3)))
}

res <- replicate(100000, sim.ants())
sum(res) / length(res)

#task8
sim.eggs.A <- function() {
  eggs <- c(rep(1, 2), rep(0, 6))
  draws <- sample(eggs, 8, replace = FALSE)
  p1 <- draws[1:2]
  p2 <- draws[3:4]
  p3 <- draws[5:6]
  p4 <- draws[7:8]
  
  sum(p1) == 2 || sum(p2) == 2 || sum(p3) == 2 || sum(p4) == 2
}

res <- replicate(100000, sim.eggs.A())
sum(res) / length(res)

# I think the problem is wrong. They must ask about the chance of everyone having
# a non boiled egg
sim.eggs.B <- function() {
  eggs <- c(rep(1, 2), rep(0, 6))
  draws <- sample(eggs, 8, replace = FALSE)
  p1 <- draws[1:2]
  p2 <- draws[3:4]
  p3 <- draws[5:6]
  p4 <- draws[7:8]
  
  sum(p1) <= 1 && sum(p2) <= 1 && sum(p3) <= 1 && sum(p4) <= 1
}

res <- replicate(100000, sim.eggs.B())
sum(res) / length(res)


sim.eggs.C <- function() {
  eggs <- c(rep(1, 2), rep(0, 6))
  draws <- sample(eggs, 8, replace = FALSE)
  p1 <- draws[1:2]
  p2 <- draws[3:4]
  p3 <- draws[5:6]
  p4 <- draws[7:8]
  
  sum(p1) == 2
}

res <- replicate(100000, sim.eggs.C())
sum(res) / length(res)

#  it is obvious that the next subtask is same as this one

# task 9
sim.test <- function() {
  x <- sample(c(0, 1), 10, replace = TRUE, prob = c(0.75, 0.25))
  sum(x) >= 5
  }

res <- replicate(100000, sim.test())
sum(res) / length(res)

# task 10
sim.airplane <- function() {
  x <- sample(c(0, 1), 143, replace = TRUE, prob = c(0.08, 0.92))
  sum(x)
}

# A
res <- replicate(100000, sim.airplane())
sum((res <= 138)) / length(res)

#B
res <- replicate(100000, sim.airplane())
sum((res == 137)) / length(res)

# task 11
sim.boxes <- function() {
  x <- sample(c(1, 6), 1)
  if (x==6) {
    ball <- sample( c("g", "g", "r", "r"), 1 )
  } else {
    ball <- sample( c("g", "r", "r", "r", "r"), 1 )
  }
  ball=="g"
}

res <- replicate(100000, sim.boxes())
sum(res) / length(res)
