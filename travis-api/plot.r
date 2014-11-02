setwd("~/dev/dump/travis-api")

png(filename="reliability.png",width=640,height=1280)

df <- read.csv(file="results.csv")
ggplot(data=df,aes(x=reorder(project, nines),fill=category,y=nines)) + geom_bar() + coord_flip() +
labs(y="Uptime (percent)", x="Project") +
scale_y_continuous(breaks=c(0,1,2,3,4,5), labels=c("0","90","99","99.9","99.99","99.999")) +
theme_minimal(base_size=16) +
theme(legend.justification=c(1,0), legend.position=c(1,.5)) +
scale_fill_brewer(palette="Set1")

dev.off()
