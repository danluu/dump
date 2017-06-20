library(ggplot2)
library(gridSVG)

# data <- read.csv(file="faction.csv", header=TRUE, sep=",")
# ggplot(data, aes(rating, win.rate)) +
#    geom_point(aes(colour=factor(faction), shape=factor(faction)), position=position_dodge(width = 20)) +
#    scale_colour_manual(values = c("orange","black","green","red","brown","black","orange","grey","grey","yellow","red","brown","purple","blue","yellow","blue","green","purple")) +
#    scale_shape_manual(values = c(13, 13, 13, 13, 13, 19, 19, 13, 19, 13, 19, 19, 13, 13, 19, 19, 19, 19)) +
#    ylim(0.05, 0.56) +
#    theme_minimal()
# gridSVG::grid.export("wins-vs-faction.svg")


# data <- read.csv(file="faction.adj.csv", header=TRUE, sep=",")
# ggplot(data, aes(rating, win.rate)) +
#    geom_point(aes(colour=factor(faction), shape=factor(faction)), position=position_dodge(width = 20)) +
#    scale_colour_manual(values = c("orange","black","green","red","brown","black","orange","grey","grey","yellow","red","brown","purple","blue","yellow","blue","green","purple")) +
#    scale_shape_manual(values = c(13, 13, 13, 13, 13, 19, 19, 13, 19, 13, 19, 19, 13, 13, 19, 19, 19, 19)) +
#    ylim(0.05, 0.56) +
#    theme_minimal()
# gridSVG::grid.export("wins-vs-faction-adjusted.svg")

# data <- read.csv(file="faction.top.csv", header=TRUE, sep=",")
# ggplot(data, aes(rating, win.rate)) +
#    geom_point(aes(colour=factor(faction), shape=factor(faction)), size = 6, position=position_dodge(width = 30)) +
#    scale_colour_manual(values = c("orange","black","brown","black","orange","grey","brown","green","purple")) +
#    scale_shape_manual(values = c(19, 19, 19, 13, 13, 19, 13, 19, 19)) +
#    theme_minimal()
# gridSVG::grid.export("wins-vs-faction-top.svg")

# data <- read.csv(file="faction.bot.csv", header=TRUE, sep=",")
# ggplot(data, aes(rating, win.rate)) +
#    geom_point(aes(colour=factor(faction), shape=factor(faction)), size = 6, position=position_dodge(width = 30)) +
#    scale_colour_manual(values = c("green","red","grey","yellow","red","purple","blue","yellow","blue")) +
#    scale_shape_manual(values = c(19, 19, 19, 19, 13, 19, 19, 13, 13)) +
#    theme_minimal()
# gridSVG::grid.export("wins-vs-faction-bot.svg")

data <- read.csv(file="faction.0.csv", header=TRUE, sep=",")
ggplot(data, aes(rating, win.rate)) +
   geom_point(aes(colour=faction, shape=faction), size = 6, position=position_dodge(width = 30)) +
   geom_line(aes(group=faction, colour=faction), position=position_dodge(width=30)) + 
   scale_colour_manual(values = c("orange","black","brown","black","orange","grey","brown","green","purple")) +
   scale_shape_manual(values = c(19, 19, 19, 13, 13, 19, 13, 19, 19)) +
   theme_minimal()
gridSVG::grid.export("wins-vs-faction-0.svg")

data <- read.csv(file="faction.1.csv", header=TRUE, sep=",")
ggplot(data, aes(rating, win.rate)) +
   geom_point(aes(colour=faction, shape=faction), size = 6, position=position_dodge(width = 30)) +
   geom_line(aes(group=faction, colour=faction), position=position_dodge(width=30)) + 
   scale_colour_manual(values = c("red","brown","purple","blue","yellow","blue")) + 
   scale_shape_manual(values = c(19, 19, 19, 19, 19, 13)) +
   theme_minimal()
gridSVG::grid.export("wins-vs-faction-1.svg")

data <- read.csv(file="faction.2.csv", header=TRUE, sep=",")
ggplot(data, aes(rating, win.rate)) +
   geom_point(aes(colour=faction, shape=faction), size = 6, position=position_dodge(width = 30)) +
   geom_line(aes(group=faction, colour=faction), position=position_dodge(width=30)) + 
   scale_colour_manual(values = c("green","yellow","red")) + 
   scale_shape_manual(values = c(19, 19, 19)) +
   theme_minimal()
gridSVG::grid.export("wins-vs-faction-2.svg")