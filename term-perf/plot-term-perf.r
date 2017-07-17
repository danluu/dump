library(ggplot2)
library(gridSVG)

# data <- read.csv(file="term-perf.csv", header=TRUE, sep=",")
# ggplot(data, aes(latency.ms,colour=terminal)) + geom_freqpoly(bins=100) + theme_minimal() + scale_colour_brewer(palette="Set1")

# getPalette = colorRampPalette(brewer.pal(10, "Set1"))

per <- read.csv(file="idle-percentile.csv", header=TRUE, sep=",")
ggplot(per, aes(nines,latency.ms,colour=terminal)) +
  geom_line(size=1.5) +
  theme_minimal() +
  # scale_colour_brewer(palette="Set2") +
  scale_x_continuous(breaks=c(0.3,1,2,3), labels=c("50","90","99","99.9")) +
  scale_y_continuous(limits=c(5,115)) +
  labs(x = "Percentile", y = "Latency (ms)", colour = "Terminal")

gridSVG::grid.export("idle-terminal-latency.svg")

per <- read.csv(file="busy-percentile.csv", header=TRUE, sep=",")
ggplot(per, aes(nines,latency.ms,colour=terminal)) +
  geom_line(size=1.5) +
  theme_minimal() +
  # scale_colour_brewer(palette="Set2") +
  scale_x_continuous(breaks=c(0.3,1,2,3), labels=c("50","90","99","99.9")) +
  scale_y_continuous(limits=c(5,115)) +
  labs(x = "Percentile", y = "Latency (ms)", colour = "Terminal")

gridSVG::grid.export("loaded-terminal-latency.svg")