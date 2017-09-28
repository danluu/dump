library(ggplot2)
library(scales)

# data <- read.csv(file="all.results", header=TRUE, sep=",")
data <- read.csv(file="filtered.csv", header=TRUE, sep=",")

ggplot(data=data, aes(data$num_options)) + stat_density(aes(y=..count..), color="black", fill="blue", alpha=0.3) + scale_x_continuous(breaks=c(0,1,2,4,8,16,32,64,128,256,512,1024), trans="log1p", expand=c(0,0)) + scale_y_continuous(breaks=c(0,1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384), trans="log1p", expand=c(0,0))

data <- read.csv(file="results.combined", header=TRUE, sep=",")
# ggplot(data,aes(x=options,fill=factor(ubuntu_version))) + geom_dotplot(stackdir="center",stackgroups=TRUE)

ggplot(data,aes(factor(ubuntu_version),options)) + geom_point() + scale_x_discrete() + scale_y_log10()