library(ggplot2)
library(reshape2)
library(gridSVG)

data_breaks = c("X512","X1024","X2048","X4096","X8192","X16384","X32768","X65536","X131072","X262144","X524288","X1048576","X2097152","X4194304","X8388608","X16777216","X33554432","X67108864","X134217728")

data_labels = c("512", "1k", "2k", "4k", "8k", "16k",
"32k", "64k", "128k", "256k", "512k", "1M", "2M", "4M",
"8M", "16M", "32M", "64M", "128M")

raw_data <- read.csv(file="result.csv", header=TRUE, sep=",")
data <- melt(raw_data,id.vars=c("pattern"))

ggplot(data, aes(variable, value)) + geom_point(aes(colour=factor(pattern))) +
 # scale_y_log10(
 #   breaks = scales::trans_breaks("log10", function(x) 10^x),
 #   labels = scales::trans_format("log10", scales::math_format(10^.x))
 # ) +
 # This janky method of generating breaks is because gridSVG produces SVG output that doesn't display correctly in chrome.
 expand_limits(y=1) +
 scale_y_log10(
   breaks = c(1, 10, 100),
   labels = c("10⁰","10¹","10²")
 ) +
 labs(x="size",y="cycles/load",colour="pattern") +
 theme_minimal() +
 scale_colour_brewer(palette="Set1") +
 theme(axis.text.x=element_text(angle=45, hjust=1)) +
 scale_x_discrete(breaks=data_breaks, labels=data_labels)

gridSVG::grid.export("memory-latency.svg")

# ggsave(file="cache-latency.svg", plot=img, width=10, height=8)