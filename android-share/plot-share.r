library(gganimate)
library(ggplot2)

svg(filename="android-age.svg", width=12, height=12)

df <- read.csv("share-plot.csv",colClasses=c("Date",NA,NA))
new_pal <- colorRampPalette(c("darkblue","darkgreen"))(3)
recent_pal <- colorRampPalette(c("forestgreen","goldenrod4"))(3)
real_pal <- colorRampPalette(c("goldenrod1","darkorange2","darkorange4","firebrick4","firebrick2","white","gray87","gray67","gray48","gray28","gray11","black"))(74)
extra_pal <- colorRampPalette(c("black","black"))(24)
my_pal <- c(new_pal, recent_pal, real_pal, extra_pal)
ggplot(df, aes(x=date,y=percent,fill=as.factor(age))) + geom_area() +
           theme_minimal() +
           theme(text = element_text(size = 30), legend.text=element_text(size=10)) +
           scale_fill_manual(values = my_pal, guide="colorbar") +
           guides(fill=guide_legend(keyheight=0.3, ncol=1, title="months")) +
           scale_y_continuous(labels=c(100,75,50,25,0)) + 
           labs(y = "percentile")

dev.off()

svg(filename="android-percentile-age.svg", width=12, height=12)
df <- read.csv("percentile-plot.csv",colClasses=c(NA,"Date",NA))
ggplot(df, aes(x=date, y=age, col=as.factor(percentile))) + geom_line(size=3) +
           theme_minimal() +
           theme(text = element_text(size = 30)) +
           labs(y = "months out of date") + 
           guides(col=guide_legend(title="percentile")) +
           scale_y_continuous(breaks=c(0,24,48,72)) + 
           scale_color_brewer(type='qual', palette='Spectral')
dev.off()

svg(filename="android-age-over-time.svg", width=12, height=12)
df <- read.csv("date-plot.csv",colClasses=c("Date",NA,NA))
ggplot(df, aes(x=percentile, y=age, col=as.factor(date))) + geom_line(size=3) +
           theme_minimal() +
           theme(text = element_text(size = 30)) +
           labs(y = "months out of date") + 
           guides(col=guide_legend(title="date")) +
           scale_x_continuous(breaks=c(0,25,50,75,99)) + 
           scale_color_brewer(palette='YlGn', labels=c('2010','2012','2014','2016'))
dev.off()


df <- read.csv("all-date-plot.csv",colClasses=c("Date",NA,NA))
p <- ggplot(df, aes(x=percentile, y=age, frame=date)) + geom_line(size=3) +
           theme_minimal() +
           theme(text = element_text(size = 30)) +
           labs(y = "months out of date") + 
           guides(col=guide_legend(title="date")) +
           scale_x_continuous(breaks=c(0,25,50,75,99)) +
           scale_y_continuous(breaks=c(0,24,48,72))           

gganimate(p,interval=.1,"android-age.gif")