library(twitteR)
setwd("~/Dropbox/projects/twitter/ismb")

# loads 5 objects, 1 per day
load("data/ismb1-5.RData")

# ugly hack to get one big data frame
ismb <- rbind(twListToDF(ismb1),
              twListToDF(ismb2),
              twListToDF(ismb3),
              twListToDF(ismb4),
              twListToDF(ismb5))

# save and write to CSV
save(ismb, file = "data/ismb.RData")
write.table(ismb, "data/ismb.csv", sep = ",", quote = F, row.names = F, col.names = T)
