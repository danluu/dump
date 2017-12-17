library(ggplot2)

svg(filename="refresh-v-latency.svg", width=12, height=12)

df <- read.csv("refresh.csv")
ggplot(df, aes(x=refresh,y=latency)) + geom_point()

dev.off()