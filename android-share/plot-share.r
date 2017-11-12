library(ggplot2)

svg(filename="android-age.svg")

df <- read.csv("share-plot.csv",colClasses=c("Date",NA,NA))
new_pal <- colorRampPalette(c("darkblue","darkgreen"))(3)
recent_pal <- colorRampPalette(c("forestgreen","goldenrod4"))(3)
real_pal <- colorRampPalette(c("goldenrod1","darkorange2","darkorange4","firebrick4","firebrick2","white","gray87","gray67","gray48","gray28","gray11","black"))(74)
extra_pal <- colorRampPalette(c("black","black"))(24)
my_pal <- c(new_pal, recent_pal, real_pal, extra_pal)
ggplot(df, aes(x=date,y=percent,fill=as.factor(months))) + geom_area() +
           scale_fill_manual(values = my_pal, guide="colorbar") +
           guides(fill=guide_legend(keyheight=0.01,nrow=74)) +
           theme(legend.text = element_text(size=5))

dev.off()