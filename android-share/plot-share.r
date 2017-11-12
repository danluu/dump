library(ggplot2)

df <- read.csv("share-plot.csv",colClasses=c("Date",NA,NA))
 ggplot(df, aes(x=date,y=percent,fill=as.factor(months))) + geom_area() + scale_fill_manual(values = colorRampPalette(c("darkgreen","goldenrod3","goldenrod2","goldenrod1","firebrick4","firebrick3","firebrick2","firebrick1"))(80))
