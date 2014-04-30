#!/usr/bin/ruby

require 'yaml'
require 'twitter'
require 'csv'

# get more results
def get_more_tweets(results, client)
	return if results.to_h[:search_metadata][:next_results].nil?
	max_id  = $1.to_i - 1 if [:search_metadata][:next_results] =~ /max_id=(.*?)&/
	results = client.search("#thankcsiroforthat", options = {:include_entities => 1, :count => 100, :max_id => max_id})
	CSV.open("#{ENV['HOME']}/Dropbox/projects/twitter/csiro/scratch/thankcsiro.csv", "a") do |csv|
		results.each do |tweet|
    		csv << [tweet.user.id, tweet.user.name, tweet.id, tweet.created_at, tweet.user.time_zone, tweet.user.followers_count, tweet.text.gsub("\n", " "), tweet.retweet_count, tweet.favorite_count]
    	end
	end
	puts "Max ID = #{max_id}"
	get_more_tweets(results, client)
end

credentials = YAML.load_file("#{ENV['HOME']}/Documents/twitcred.yaml")

client = Twitter::REST::Client.new do |config|
    config.consumer_key        = credentials["api_key"]
    config.consumer_secret     = credentials["api_secret"]
    config.access_token        = credentials["access_token"]
    config.access_token_secret = credentials["access_token_secret"]
end

# first search
csiro = client.search("#thankcsiroforthat", options = {:include_entities => 1, :count => 100})

CSV.open("#{ENV['HOME']}/Dropbox/projects/twitter/csiro/scratch/thankcsiro.csv", "w") do |csv|
    csv << ["userid", "username", "tweetid", "timestamp", "timezone", "followers", "text", "retweet", "favorite"]
    csiro.each do |tweet|
        csv << [tweet.user.id, tweet.user.name, tweet.id, tweet.created_at, tweet.user.time_zone, tweet.user.followers_count, tweet.text.gsub("\n", " "), tweet.retweet_count, tweet.favorite_count]
    end
end

# subsequent searches
get_more_tweets(csiro, client)