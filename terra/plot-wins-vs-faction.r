library(ggplot2)
library(gridSVG)

data <- read.csv(file="faction.csv", header=TRUE, sep=",")

ggplot(data, aes(rating, win.rate)) +
   geom_point(aes(colour=factor(faction), shape=factor(faction)), position=position_dodge(width = 20)) +
   scale_colour_manual(values = c("orange","black","green","red","brown","black","orange","grey","grey","yellow","red","brown","purple","blue","yellow","blue","green","purple")) +
   scale_shape_manual(values = c(13, 13, 13, 13, 13, 19, 19, 13, 19, 13, 19, 19, 13, 13, 19, 19, 19, 19)) +
   ylim(0.05, 0.56) +
   theme_minimal()

gridSVG::grid.export("wins-vs-faction.svg")


data <- read.csv(file="faction.adj.csv", header=TRUE, sep=",")

ggplot(data, aes(rating, win.rate)) +
   geom_point(aes(colour=factor(faction), shape=factor(faction)), position=position_dodge(width = 20)) +
   scale_colour_manual(values = c("orange","black","green","red","brown","black","orange","grey","grey","yellow","red","brown","purple","blue","yellow","blue","green","purple")) +
   scale_shape_manual(values = c(13, 13, 13, 13, 13, 19, 19, 13, 19, 13, 19, 19, 13, 13, 19, 19, 19, 19)) +
   ylim(0.05, 0.56) +
   theme_minimal()

gridSVG::grid.export("wins-vs-faction-adjusted.svg")