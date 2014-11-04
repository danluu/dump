library(ggplot2)

setwd("~/dev/dump/linux-mining")

png(filename="null-percentile.png",width=640,height=480)
df <- read.csv(file="nulls.csv")
ggplot(df,aes(Rank,Percentile)) + geom_point(alpha=1/10)
