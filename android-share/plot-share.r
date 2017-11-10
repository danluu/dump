library(ggplot2)

df <- read.csv("share-plot.csv",colClasses=c("Date",NA,NA))
ggplot(df, aes(x=date,y=percent,fill=as.factor(months))) + geom_area()
