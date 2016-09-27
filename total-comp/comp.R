library(ggplot2)

c <- read.csv("fall2015.csv")
ft <- c[c$Position.Type == "Full Time",]
ft$totalcomp <- as.numeric(gsub(",","",ft$totalcomp))
ft <- ft[ft$totalcomp != NA,]
ggplot(data=ft, aes(ft$totalcomp)) + geom_histogram(binwidth=10000) +  theme_bw()
