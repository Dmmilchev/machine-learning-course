# task 64
sim.coin <- function() {
  x <- sample(c(0, 1), 200, replace = T)
  sum(x) == 100
}
res <- replicate(100000, sim.coin())
sum(res) / length(res)

1 - sum(dbinom(86:114, 200, 0.5))

sim.coin2 <- function() {
  x <- sample(c(0, 1), 200, prob = (c(0.4, 0.6)), replace = T)
  sum(x) >= 86 && sum(x) <= 114
}
res <- replicate(100000, sim.coin2())
1 - (sum(res) / length(res))

sim.coin3 <- function() {
  x <- sample(c(0, 1), 200, prob = (c(0.3, 0.7)), replace = T)
  sum(x) >= 86 && sum(x) <= 114
}
res <- replicate(100000, sim.coin3())
1 - (sum(res) / length(res))

# task 65
mu = 6.7
sigma = 0.12
n = 45

res <- replicate(10^5, abs(mean(rnorm(n, mu, sigma)) - mu) >= 0.036)
sum(res) / length(res)

res <- replicate(10^5, abs(mean(rnorm(n, 6.75, sigma)) - mu) >= 0.036)
sum(res) / length(res)

res <- replicate(10^5, abs(mean(rnorm(n, 6.8, sigma)) - mu) >= 0.036)
sum(res) / length(res)

# task 66
n = 66
mu = 61.9
sigma = 4
real_sigma = 4.1
mu_0 = 60

z_obs = (mu - mu_0) / (real_sigma / sqrt(66))
2*(1 - pnorm(abs(z_obs)))
# p_value is 0.0001 which is less than the usually accepted 5%. This means that we reject the null hypothesis.

# task 67
n = 58
x_obs = 32 / n
p = 0.51

z_obs = (x_obs - p) / (sqrt(p*(1-p)) / sqrt(n))
2*(1 - pnorm(abs(z_obs)))
# p_value is 0.55, which means that we accept the null hypothesis

# task 68
data <- c(3.1, 3, 3.7, 2.6, 4.2, 3.8, 3.6, 2.7, 3.8, 4.4)
mu = 4

t_obs = (mean(data) - mu) / (sd(data) / sqrt(length(data)))
pt(t_obs, length(data) - 1)

t.test( data, mu=4, alternative="less" )

 # task 69
data <- c(12.3, 11.2, 14.2, 15.3, 14.8, 13.5, 11.1, 15.1, 15.4, 13.2)
mu <- 14.6

t_obs = (mean(data) - mu) / (sd(data) / sqrt(length(data)))
pt(t_obs, length(data) - 1)
# P_value is 4%, we can reject the null hypothesis

# task 70
z_obs = ((14 / 200) - 0.075) / (sqrt((14/200)*(1 - 14/200)) / sqrt(200))
2 * (1 - pnorm(abs(z_obs)))

# task 71
z_obs = (168 - 170) / (3.9 / sqrt(50))
pnorm(z_obs)