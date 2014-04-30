parseJSON <- function(json) {
  require(rjson)
  j <- fromJSON(file = json)
  tweets <- data.frame(userid    = sapply(j$statuses, function(x) x$user$id_str),
                       username  = sapply(j$statuses, function(x) x$user$name),
                       tweetid   = sapply(j$statuses, function(x) x$id_str),
                       timestamp = sapply(j$statuses, function(x) x$created_at),
                       followers = sapply(j$statuses, function(x) x$user$followers_count),
                       text      = sapply(j$statuses, function(x) x$text),
                       retweet   = sapply(j$statuses, function(x) x$retweet_count),
                       favorite  = sapply(j$statuses, function(x) x$favorite_count)
                       )
  return(tweets)
}