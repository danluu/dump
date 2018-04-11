library(rethinking)
globe.qa <- map(
  alist(
    w ~ dbinom(9, p),
    p ~ dunif(0, 1)
  ),
  data = list(w=6))

precis(globe.qa)