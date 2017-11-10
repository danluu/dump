library(ggplot2)

df <- read.csv("share-plot.csv")
ggplot(df, aes(x=date,y=percent,color=months)) + geom_point()