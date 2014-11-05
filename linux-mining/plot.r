library(ggplot2)

setwd("~/dev/dump/linux-mining")

png(filename="null-percentile.png",width=640,height=480)
df <- read.csv(file="nulls.csv")
ggplot(df,aes(Rank,Percentile)) + geom_point(alpha=1/3) + labs(title="Null")


png(filename="arm-percentile.png",width=640,height=480)
dfa <- read.csv(file="arms.csv")
ggplot(dfa,aes(Rank,Percentile)) + geom_point(alpha=1/3) + labs(title="ARM")


png(filename="posix-percentile.png",width=640,height=480)
dfp <- read.csv(file="posixs.csv")
ggplot(dfp,aes(Rank,Percentile)) + geom_point(alpha=1/3) + labs(title="POSIX")

png(filename="usb-percentile.png",width=640,height=480)
dfu <- read.csv(file="usbs.csv")
ggplot(dfu,aes(Rank,Percentile)) + geom_point(alpha=1/3) + labs(title="USB")


png(filename="fix-percentile.png",width=640,height=480)
dff <- read.csv(file="fixs.csv")
ggplot(dff,aes(Rank,Percentile)) + geom_point(alpha=1/3) + labs(title="Fix")
