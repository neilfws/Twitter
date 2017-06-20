# Twitter Coverage of the Sydney Bioinformatics Research Symposium 2017
Neil Saunders  
`r Sys.time()`  



# Introduction
An analysis of tweets from the Sydney Bioinformatics Research Symposium 2017. 215 tweets were collected using the `rtweet` R package:


```r
library(rtweet)
sbrs17 <- search_tweets("#sbrs17 OR #sbrs2017", 1000)
```

# Timeline
## Tweets by day
![](sbrs17_files/figure-html/tweets-by-day-1.png)<!-- -->

## Tweets by day and time
![](sbrs17_files/figure-html/tweets-by-day-hour-1.png)<!-- -->

# Users
## Top tweeters
![](sbrs17_files/figure-html/tweets-top-users-1.png)<!-- -->

## Sources
![](sbrs17_files/figure-html/tweets-top-sources-1.png)<!-- -->

# Networks
## Replies
The "replies network", composed from users who reply directly to one another, was very small for SBRS 17 and was not analysed further.




## Mentions
The "mentions network", where users mention other users in their tweets, was constructed as per the code in the accompanying `Rmd` file. The resulting `graphml` file was visualised using Gephi (0.9.1). Nodes and edges are coloured by pagerank value.



![](../../data/sbrs_mentions.png)

# Retweets
## Retweet proportion
![](sbrs17_files/figure-html/is-retweet-1.png)<!-- -->

## Retweet count
![](sbrs17_files/figure-html/retweet-count-1.png)<!-- -->

## Top retweets
<table>
 <thead>
  <tr>
   <th style="text-align:left;"> screen_name </th>
   <th style="text-align:left;"> text </th>
   <th style="text-align:right;"> retweet_count </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> koadman </td>
   <td style="text-align:left;"> Bioinformatics research as defined by Geoff Barton. Peer reviewed journal publications just one of many outputs… https://t.co/zKZA6yLPPF </td>
   <td style="text-align:right;"> 23 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> nat_twine </td>
   <td style="text-align:left;"> Fast forward presentations at #sbrs2017 #BigData #machinelearning applications for #ALS at #CSIRO https://t.co/vTMfG94xmY </td>
   <td style="text-align:right;"> 10 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> shazanfar </td>
   <td style="text-align:left;"> Love how @gjbarton has concrete recommendations for designing RNA-Seq exps. 1: Do at least 6 biological replicates! Yes! #sbrs17 #sbrs2017 </td>
   <td style="text-align:right;"> 7 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> scientist_kate </td>
   <td style="text-align:left;"> Geoff Barton - Closing invited lecture: lessons from a 48 replicate RNAseq experiment #sbrs2017 @gjbarton https://t.co/Sznnpj1iZ3 </td>
   <td style="text-align:right;"> 5 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> gjbarton </td>
   <td style="text-align:left;"> VariantSpark  big data + machine learning.  I really did talk too small.  lovely mix of methods and applications in this meeting.  #sbrs2017 </td>
   <td style="text-align:right;"> 5 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> shazanfar </td>
   <td style="text-align:left;"> In this session at #sbrs2017 #sbrs17 I'll be speaking about this work on single cell data analysis of neurons https://t.co/GFSrwlvoxl </td>
   <td style="text-align:right;"> 3 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> gjbarton </td>
   <td style="text-align:left;"> Ohhhh!  Technical variation talk!! qPCR is not a gold standard. consensus modelling across different techniques on same sample.  #sbrs2017 </td>
   <td style="text-align:right;"> 3 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> rebecca_poulos </td>
   <td style="text-align:left;"> Exciting research at #sbrs17! Ancient DNA, plant genomics, complex genomic rearrangements, and more. Now onto fast forward talks #sbrs2017 </td>
   <td style="text-align:right;"> 3 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> shazanfar </td>
   <td style="text-align:left;"> #sbrs17 Gene ORGANizer linking disease genes to organs @lirancarmel https://t.co/Sju8WSDW1a </td>
   <td style="text-align:right;"> 3 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> shazanfar </td>
   <td style="text-align:left;"> #SBRS17 Sydney Bioinformatics Research Symposium program available here https://t.co/z4Vno7yQfv </td>
   <td style="text-align:right;"> 3 </td>
  </tr>
</tbody>
</table>

# Favourites
## Favourite proportion
![](sbrs17_files/figure-html/has-favorite-1.png)<!-- -->

## Favourite count
![](sbrs17_files/figure-html/favorite-count-1.png)<!-- -->

## Top favourites
<table>
 <thead>
  <tr>
   <th style="text-align:left;"> screen_name </th>
   <th style="text-align:left;"> text </th>
   <th style="text-align:right;"> favorite_count </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> koadman </td>
   <td style="text-align:left;"> Bioinformatics research as defined by Geoff Barton. Peer reviewed journal publications just one of many outputs… https://t.co/zKZA6yLPPF </td>
   <td style="text-align:right;"> 31 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> shazanfar </td>
   <td style="text-align:left;"> Love how @gjbarton has concrete recommendations for designing RNA-Seq exps. 1: Do at least 6 biological replicates! Yes! #sbrs17 #sbrs2017 </td>
   <td style="text-align:right;"> 10 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> nat_twine </td>
   <td style="text-align:left;"> Fast forward presentations at #sbrs2017 #BigData #machinelearning applications for #ALS at #CSIRO https://t.co/vTMfG94xmY </td>
   <td style="text-align:right;"> 10 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> gjbarton </td>
   <td style="text-align:left;"> I think the strong biology-led talks at a bioinformatics meeting just shows how bioinformatics is integral to modern biology.  #sbrs2017 </td>
   <td style="text-align:right;"> 9 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> jasonwwong </td>
   <td style="text-align:left;"> Great talk by @rebecca_poulos on patterns of genome-wide CpG methylation mutations in cancer #sbrs2017 Paper here:… https://t.co/fKFJjsElR8 </td>
   <td style="text-align:right;"> 8 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> statsgen </td>
   <td style="text-align:left;"> Over 50 abstracts submitted, only 8 talks - one of them by @shazanfar ! Nice job @shazanfar ! #sbrs2017 https://t.co/H8DiQhCMDw </td>
   <td style="text-align:right;"> 7 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> scientist_kate </td>
   <td style="text-align:left;"> Geoff Barton - Closing invited lecture: lessons from a 48 replicate RNAseq experiment #sbrs2017 @gjbarton https://t.co/Sznnpj1iZ3 </td>
   <td style="text-align:right;"> 7 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> shazanfar </td>
   <td style="text-align:left;"> In this session at #sbrs2017 #sbrs17 I'll be speaking about this work on single cell data analysis of neurons https://t.co/GFSrwlvoxl </td>
   <td style="text-align:right;"> 7 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> rebecca_poulos </td>
   <td style="text-align:left;"> Exciting research at #sbrs17! Ancient DNA, plant genomics, complex genomic rearrangements, and more. Now onto fast forward talks #sbrs2017 </td>
   <td style="text-align:right;"> 7 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> shazanfar </td>
   <td style="text-align:left;"> GB: @gjbarton showing the interplay between analysis, techniques and applications occurring within bioinformatics r… https://t.co/QcJsVLlNrt </td>
   <td style="text-align:right;"> 6 </td>
  </tr>
</tbody>
</table>

# Quotes
## Quote proportion
![](sbrs17_files/figure-html/is-quote-1.png)<!-- -->

## Quote count
![](sbrs17_files/figure-html/quotes-count-1.png)<!-- -->

## Top quotes
<table>
 <thead>
  <tr>
   <th style="text-align:left;"> screen_name </th>
   <th style="text-align:left;"> text </th>
   <th style="text-align:right;"> quote_count </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> LouCaruana </td>
   <td style="text-align:left;"> Scientists and #biotech experts from @GarvanInstitute are seeking to tackle major diseases like the ebola virus.… https://t.co/4pGvQEc8JH </td>
   <td style="text-align:right;"> 3 </td>
  </tr>
</tbody>
</table>

# Media
## Media count
![](sbrs17_files/figure-html/has-media-1.png)<!-- -->

## Top media
<table>
 <thead>
  <tr>
   <th style="text-align:left;"> screen_name </th>
   <th style="text-align:left;"> text </th>
   <th style="text-align:right;"> favorite_count </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> nat_twine </td>
   <td style="text-align:left;"> Fast forward presentations at #sbrs2017 #BigData #machinelearning applications for #ALS at #CSIRO https://t.co/vTMfG94xmY </td>
   <td style="text-align:right;"> 10 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> statsgen </td>
   <td style="text-align:left;"> Over 50 abstracts submitted, only 8 talks - one of them by @shazanfar ! Nice job @shazanfar ! #sbrs2017 https://t.co/H8DiQhCMDw </td>
   <td style="text-align:right;"> 7 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> scientist_kate </td>
   <td style="text-align:left;"> Geoff Barton - Closing invited lecture: lessons from a 48 replicate RNAseq experiment #sbrs2017 @gjbarton https://t.co/Sznnpj1iZ3 </td>
   <td style="text-align:right;"> 7 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> scientist_kate </td>
   <td style="text-align:left;"> Katherine Jackson from @GarvanInstitute at #SBRS2017 https://t.co/axDmupxoh3 </td>
   <td style="text-align:right;"> 3 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> hydra_hamster </td>
   <td style="text-align:left;"> Optical mapping for detecting complex genomic rearrangement - now that's cool! Eva Chan @GarvanInstitute #SBRS17 https://t.co/m32RDq3WrV </td>
   <td style="text-align:right;"> 3 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> hydra_hamster </td>
   <td style="text-align:left;"> Impressive list of software @gjbarton is involved in bringing to the rest of us! #sbrs17 https://t.co/exsnWqw51M </td>
   <td style="text-align:right;"> 2 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> shazanfar </td>
   <td style="text-align:left;"> #sbrs17 DMRs between ancient neanderthal and modern human maps to face + throat + vocal cord organs @lirancarmel https://t.co/KpysFCGxFt </td>
   <td style="text-align:right;"> 2 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> scientist_kate </td>
   <td style="text-align:left;"> Sydney Bioinformatics Research Symposium is kicking off with Dr Liran Carmel on ancient Epigenomes #SBRS2017 https://t.co/cdApgglOJn </td>
   <td style="text-align:right;"> 2 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> nat_twine </td>
   <td style="text-align:left;"> @gjbarton closing up #sbrs2017 meeting with his work at Dundee university https://t.co/Yk7iY76vFS </td>
   <td style="text-align:right;"> 1 </td>
  </tr>
</tbody>
</table>

### Most liked media image
![](http://pbs.twimg.com/media/DCLHMy4VYAAI7DD.jpg)

# Tweet text
The 100 words used 3 or more times.

![](sbrs17_files/figure-html/count-words-1.png)<!-- -->

