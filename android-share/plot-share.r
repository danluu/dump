library(ggplot2)

svg(filename="android-age.svg")

df <- read.csv("share-plot.csv",colClasses=c("Date",NA,NA))
real_pal <- colorRampPalette(c("darkgreen","goldenrod3","goldenrod1","darkorange2","darkorange4","firebrick4","firebrick3","firebrick2","firebrick1","white","gray87","gray67","gray48","gray28","gray11","black"))(80)
extra_pal <- colorRampPalette(c("black","black"))(24)
my_pal <- c(real_pal, extra_pal)
ggplot(df, aes(x=date,y=percent,fill=as.factor(months))) + geom_area() + scale_fill_manual(values = my_pal)

dev.off()