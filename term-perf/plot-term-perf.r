library(ggplot2)

data <- read.csv(file="term-perf.csv", header=TRUE, sep=",")

ggplot(data, aes(latency..ms.,colour=terminal)) + geom_freqpoly(bins=100) + theme_minimal() + scale_colour_brewer(palette="Set1")