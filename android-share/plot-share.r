library(ggplot2)

png(filename="android-age.png",width=1920,height=1080)

df <- read.csv("share-plot.csv",colClasses=c("Date",NA,NA))
my_pal <- colorRampPalette(c("darkgreen","goldenrod3","goldenrod2","goldenrod1","firebrick4","firebrick3","firebrick2","firebrick1"))(80)
ggplot(df, aes(x=date,y=percent,fill=as.factor(months))) + geom_area() + scale_fill_manual(values = my_pal)

dev.off()