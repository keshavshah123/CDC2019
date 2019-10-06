# CAROLINA DATA CHALLENGE 2019
# Principal Component Analysis on election data from NC counties & voting districts

library(igraph)
library(magrittr)
library(ggfortify)

get_proportion <- function(sdev, N) {
  return((sdev**2)/N)
}

# Read data
counties <- read.csv("./counties.csv")
districts <- read.csv("./districts.csv")

# Transform data
# Counties
counties <- do.call(rbind, lapply(counties, unlist))
county_props <- matrix(0, dim(counties)[1], 1)
rownames(county_props) <- labels(counties)[[1]]
# Checks
for (i in 1:dim(counties)[1]) {
  prop <- counties[i,1]/counties[i,2]
  if ((prop <= 1.0) & (prop > 0.0) & !is.na(prop)) {
    county_props[i] <- prop
  }
}
clabs <- labels(counties)[[1]]
for ( ind in rev(which(county_props == 0.0)) ) {
  county_props <- county_props[-ind]
  clabs <- clabs[-ind]
}
county_props <- as.matrix(county_props)
rownames(county_props) <- clabs
# Districts
districts <- do.call(rbind, lapply(districts, unlist))
district_props <- matrix(0, dim(districts)[1], 1)
rownames(district_props) <- labels(districts)[[1]]
# Checks
for (i in 1:dim(districts)[1]) {
  prop <- districts[i,1]/districts[i,2]
  if ((prop <= 1.0) & (prop > 0.0) & !is.na(prop)) {
    district_props[i] <- prop
  }
}
dlabs <- labels(districts)[[1]]
for ( ind in rev(which(district_props == 0.0)) ) {
  district_props <- district_props[-ind]
  dlabs <- dlabs[-ind]
}
district_props <- as.matrix(district_props)
rownames(district_props) <- dlabs

# PCA & get proportions of variance
# Counties
counties.diffs <- matrix(0, length(county_props), length(county_props))
for (i in 1:length(county_props)) {
  for (j in 1:length(county_props)) {
    if (i != j) {
      counties.diffs[i,j] <- abs(county_props[i] - county_props[j])/county_props[i]
    }
  }
}
rownames(counties.diffs) <- clabs
# Districts
districts.diffs <- matrix(0, length(district_props), length(district_props))
for (i in 1:length(district_props)) {
  for (j in 1:length(district_props)) {
    if (i != j) {
      districts.diffs[i,j] <- abs(district_props[i] - district_props[j])/district_props[i]
    }
  }
}
rownames(districts.diffs) <- dlabs

counties.pca <- prcomp(counties.diffs, center = TRUE, scale = TRUE)
districts.pca <- prcomp(districts.diffs, center = TRUE, scale = TRUE)

cvar <- lapply( counties.pca$sdev, function(x) {get_proportion(x,dim(counties.diffs)[1])} )
dvar <- lapply( districts.pca$sdev, function(x) {get_proportion(x,dim(districts.diffs)[1])} )

# Plot proportions of variance
#top_pcs <- min(length(cvar), length(dvar))
top_pcs <- 5

plot(1:top_pcs, cvar[1:top_pcs], type = 'l', xlab = 'Principal component', ylab = 'Proportion of variance')
lines(1:top_pcs, dvar[1:top_pcs], col = 'blue')
legend('topright', legend = c('Counties', 'Districts'), col = c('black', 'blue'), lty = 1)

# Plot first 2 PCs
autoplot(counties.pca, loadings = TRUE, label = TRUE)
autoplot(districts.pca, loadings = TRUE, label = TRUE)
