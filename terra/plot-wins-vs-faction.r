library(ggplot2)
library(gridSVG)

data <- read.csv(file="faction.csv", header=TRUE, sep=",")

ggplot(data, aes(rating, win.rate)) +
   geom_point(aes(colour=factor(faction), shape=factor(faction))) +
   # scale_colour_brewer(palette="Set1") +
   scale_colour_manual(values = c("orange","black","green","red","brown","black","orange","grey","grey","yellow","red","brown","#deebf7","blue","yellow","purple","purple","blue","green","#deebf7")) +
   scale_shape_manual(values = c(13, 13, 13, 13, 13, 19, 19, 13, 19, 13, 19, 19, 13, 13, 19, 13, 19, 19, 19, 19)) + 
   ylim(0.05, 0.4) +
   theme_minimal()

gridSVG::grid.export("wins-vs-faction.svg")


