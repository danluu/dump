library(ggplot2)

svg(filename="android-age.svg")

df <- read.csv("share-plot.csv",colClasses=c("Date",NA,NA))
my_pal <- colorRampPalette(c("darkgreen","goldenrod3","goldenrod2","goldenrod1","firebrick4","firebrick3","firebrick2","firebrick1","gray87","gray67","gray48","gray28","gray11","black"))(80)
ggplot(df, aes(x=date,y=percent,fill=as.factor(months))) + geom_area() + scale_fill_manual(values = my_pal)

dev.off()