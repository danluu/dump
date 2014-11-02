setwd("~/dev/dump/travis-api")

df <- read.csv(file="results.csv")
qplot(data=df,x=reorder(project, nines),fill=category,y=nines) + geom_bar() + coord_flip()
