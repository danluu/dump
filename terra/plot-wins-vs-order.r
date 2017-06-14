library(ggplot2)

data <- read.csv(file="order.csv", header=TRUE, sep=",")

ggplot(data, aes(rating, win.rate)) +
  geom_point(aes(colour=factor(player))) +
  theme_minimal()