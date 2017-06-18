library(ggplot2)
library(gridSVG)

# data <- read.csv(file="order.csv", header=TRUE, sep=",")

# ggplot(data, aes(rating, win.rate)) +
#   geom_point(aes(colour=factor(player))) +
#   scale_colour_brewer(palette="Set1") +
#   theme_minimal()

# gridSVG::grid.export("wins-vs-turn-order.svg")


data_1 <- read.csv(file="order.fav11.1.csv", header=TRUE, sep=",")
ggplot(data_1, aes(rating, win.rate)) +
  geom_point(aes(colour=factor(player))) +
  scale_colour_brewer(palette="Set1") +
  theme_minimal()

gridSVG::grid.export("wins-vs-turn-order-fav11-1.svg")

data_2 <- read.csv(file="order.fav11.2.csv", header=TRUE, sep=",")
ggplot(data_2, aes(rating, win.rate)) +
  geom_point(aes(colour=factor(player))) +
  scale_colour_brewer(palette="Set1") +
  theme_minimal()

gridSVG::grid.export("wins-vs-turn-order-fav11-2.svg")


data_3 <- read.csv(file="order.fav11.3.csv", header=TRUE, sep=",")
ggplot(data_3, aes(rating, win.rate)) +
  geom_point(aes(colour=factor(player))) +
  scale_colour_brewer(palette="Set1") +
  theme_minimal()

gridSVG::grid.export("wins-vs-turn-order-fav11-3.svg")

data_4 <- read.csv(file="order.fav11.4.csv", header=TRUE, sep=",")
ggplot(data_4, aes(rating, win.rate)) +
  geom_point(aes(colour=factor(player))) +
  scale_colour_brewer(palette="Set1") +
  theme_minimal()

gridSVG::grid.export("wins-vs-turn-order-fav11-4.svg")

# data_1 <- read.csv(file="order.fif.1.csv", header=TRUE, sep=",")
# ggplot(data_1, aes(rating, win.rate)) +
#   geom_point(aes(colour=factor(player))) +
#   scale_colour_brewer(palette="Set1") +
#   theme_minimal()

# gridSVG::grid.export("wins-vs-turn-order-fif-1.svg")

# data_2 <- read.csv(file="order.fif.2.csv", header=TRUE, sep=",")
# ggplot(data_2, aes(rating, win.rate)) +
#   geom_point(aes(colour=factor(player))) +
#   scale_colour_brewer(palette="Set1") +
#   theme_minimal()

# gridSVG::grid.export("wins-vs-turn-order-fif-2.svg")


# data_3 <- read.csv(file="order.fif.3.csv", header=TRUE, sep=",")
# ggplot(data_3, aes(rating, win.rate)) +
#   geom_point(aes(colour=factor(player))) +
#   scale_colour_brewer(palette="Set1") +
#   theme_minimal()

# gridSVG::grid.export("wins-vs-turn-order-fif-3.svg")

# data_4 <- read.csv(file="order.fif.4.csv", header=TRUE, sep=",")
# ggplot(data_4, aes(rating, win.rate)) +
#   geom_point(aes(colour=factor(player))) +
#   scale_colour_brewer(palette="Set1") +
#   theme_minimal()

# gridSVG::grid.export("wins-vs-turn-order-fif-4.svg")