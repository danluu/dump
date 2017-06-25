library(ggplot2)

data <- read.csv(file="weights.csv", header=TRUE, sep=",")
ggplot(data, aes(date, weight)) +
  geom_point(aes(colour=status)) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
  