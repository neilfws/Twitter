# get the JSON from search into a data frame
setwd("~/Dropbox/projects/twitter/csiro")
source("code/R/thankCSIROjson.R")

files      <- list.files("data", full.names = TRUE, pattern = "*.json$")
thankcsiro <- lapply(files, function(f) parseJSON(f))
thankcsiro <- do.call("rbind", thankcsiro)
thankcsiro <- thankcsiro[!duplicated(thankcsiro[, "tweetid"]),]

save(thankcsiro, file = "data/thankcsirojson.RData")