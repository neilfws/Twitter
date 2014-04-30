## Data

I wish I could say that these data were collected in a reproducible fashion. However, the vagaries of the Twitter search API do not allow for this.

If you ran a script such as the one in code/ruby/thankcsiro.rb on 2014-04-16, you would have retrieved 799 tweets tagged with #thankcsiroforthat.

One week later on 2014-04-23, you would have retrieved 275 tweets, of which 60 were previously unseen.

So that is what was done; the JSON files from both days were named by date, then combined into a data frame of 859 tweets using the R code in code/R/CSIROjson2data.R. 
