library(ggplot2)

df <- read.csv("share-plot.csv")
ggplot(df, aes(x=date,y=percent,color=as.factor(months),group=months)) + geom_line() + geom_point()