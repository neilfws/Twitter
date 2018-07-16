Twitter Coverage of the Australian Bioinformatics & Computational Biology Society Conference 2017
================
Neil Saunders
2018-07-16 22:45:12

Introduction
============

An analysis of tweets from the ABACBS 2017 meeting. 2006 tweets were collected using the `rtweet` R package:

``` r
library(rtweet)
abacbs2017 <- search_tweets("#abacbs17 OR #combine17", 5000)
```

Quitting from lines 33-53 (abacbs2017.Rmd) Error in pandoc.table.return(...) : Wrong number of parameters (3 instead of *2*) passed: justify Calls: <Anonymous> ... pander.data.frame -&gt; pandoc.table -&gt; cat -&gt; pandoc.table.return

For this analysis we retain all tweets and treat the ABACBS and COMBINE meetings as one event.

Timeline
========

Tweets by day
-------------

![](abacbs2017_files/figure-markdown_github/tweets-by-day-1.png)

Tweets by day and time
----------------------

Filtered for dates November 13-17, Adelaide time. ![](abacbs2017_files/figure-markdown_github/tweets-by-day-hour-1.png)

Users
=====

Top tweeters
------------

![](abacbs2017_files/figure-markdown_github/tweets-top-users-1.png)

Sources
-------

![](abacbs2017_files/figure-markdown_github/tweets-top-sources-1.png)

Networks
========

Replies
-------

The "replies network", composed from users who reply directly to one another.

Better to view the original PNG file in the `data` directory.

![](../../data/abacbs2017_replies.png)

Mentions
--------

The "mentions network", where users mention other users in their tweets.

Better to view the original PNG file in the `data` directory.

![](../../data/abacbs2017_mentions.png)

Retweets
========

Retweet proportion
------------------

![](abacbs2017_files/figure-markdown_github/is-retweet-1.png)

Retweet count
-------------

![](abacbs2017_files/figure-markdown_github/retweet-count-1.png)

Top retweets
------------

<table style="width:90%;">
<colgroup>
<col width="23%" />
<col width="45%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">screen_name</th>
<th align="left">text</th>
<th align="right">retweet_count</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">torstenseemann</td>
<td align="left">High performance computing (HPC) works better when used in conjunction with a High Performance Bioinformatician (HPB). #abacbs17 🖥️💻↔️👩👨</td>
<td align="right">57</td>
</tr>
<tr class="even">
<td align="left"><em>lazappi</em></td>
<td align="left">Su-In Lee &quot;Big data to personalised medicine with machine learning&quot; #abacbs17 #sketchnotes <a href="https://t.co/7v5DFP4yQ3" class="uri">https://t.co/7v5DFP4yQ3</a></td>
<td align="right">22</td>
</tr>
<tr class="odd">
<td align="left">abacbs</td>
<td align="left">Terry Speed says he had no vision: &quot;I'm a statistician, we do little things. Now when someone asks me, I say I want to cure cancer.&quot; #abacbs17</td>
<td align="right">18</td>
</tr>
<tr class="even">
<td align="left"><em>lazappi</em></td>
<td align="left">#abacbs17 Opening keynote <span class="citation">@HigginsDes</span> &quot;Everything you ever wanted to know about multiple alignment&quot; #sketchnotes <a href="https://t.co/zdQlKKfqCa" class="uri">https://t.co/zdQlKKfqCa</a></td>
<td align="right">16</td>
</tr>
<tr class="odd">
<td align="left">hdashnow</td>
<td align="left">#lornegenome 2018 will have a dedicated computational biology/bioinformatics session. Bioinformatics and comp bio abstracts from encouraged! Oral abstract deadline extended to Friday 24th Nov <a href="https://t.co/gswSQVoTHk" class="uri">https://t.co/gswSQVoTHk</a> #COMBINE17 #ABACBS17</td>
<td align="right">15</td>
</tr>
<tr class="even">
<td align="left">atma_ivancevic</td>
<td align="left">You know it's a #BioInformatics conference when every speaker lists their <span class="citation">@biorxivpreprint</span> and <span class="citation">@github</span> code #openscience #openaccess #sharingiscaring #abacbs17</td>
<td align="right">12</td>
</tr>
<tr class="odd">
<td align="left">shazanfar</td>
<td align="left">Do you want to be more involved in the COMBINE <span class="citation">@combine_au</span> community? Joining the exec team is a great way to improve your leadership skills, build your confidence and help the COMBINE student community! Nominate: <a href="https://t.co/MvY0I1OIME" class="uri">https://t.co/MvY0I1OIME</a> #abacbs17 #COMBINE17 <span class="citation">@abacbs</span></td>
<td align="right">11</td>
</tr>
<tr class="even">
<td align="left">milicang</td>
<td align="left">Congratulations to <span class="citation">@CSL</span> travel award recipients <span class="citation">@annaquagli</span> , <span class="citation">@_StuartLee</span> , <span class="citation">@_lazappi_</span> and Virginie Perlo #BioCAsia 2017 #abacbs17 <a href="https://t.co/10HXvlTkBB" class="uri">https://t.co/10HXvlTkBB</a></td>
<td align="right">10</td>
</tr>
<tr class="odd">
<td align="left">MelanieBahlo</td>
<td align="left">Running conferences is a hard job, which takes guts &amp; persistence. We do not want people scared off doing this. It is a part of career progression. Thank you so much for a great conference: #abacbs17 &amp; congratulations to David Lynn &amp; his team. I loved it.</td>
<td align="right">9</td>
</tr>
<tr class="even">
<td align="left">KerryLevett</td>
<td align="left">Look <span class="citation">@andsdata</span> #FAIR Galaxy Training poster at #ABACBS17 by <span class="citation">@galaxyproject</span> <span class="citation">@MelBioInf</span> <a href="https://t.co/u9NLJ6smcd" class="uri">https://t.co/u9NLJ6smcd</a></td>
<td align="right">9</td>
</tr>
</tbody>
</table>

Favourites
==========

Favourite proportion
--------------------

![](abacbs2017_files/figure-markdown_github/has-favorite-1.png)

Favourite count
---------------

![](abacbs2017_files/figure-markdown_github/favorite-count-1.png)

Top favourites
--------------

<table style="width:92%;">
<colgroup>
<col width="23%" />
<col width="45%" />
<col width="22%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">screen_name</th>
<th align="left">text</th>
<th align="right">favorite_count</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">torstenseemann</td>
<td align="left">High performance computing (HPC) works better when used in conjunction with a High Performance Bioinformatician (HPB). #abacbs17 🖥️💻↔️👩👨</td>
<td align="right">152</td>
</tr>
<tr class="even">
<td align="left">torstenseemann</td>
<td align="left">Legend. #abacbs17 <a href="https://t.co/dbIfVnV6TQ" class="uri">https://t.co/dbIfVnV6TQ</a></td>
<td align="right">76</td>
</tr>
<tr class="odd">
<td align="left">MelanieBahlo</td>
<td align="left">Running conferences is a hard job, which takes guts &amp; persistence. We do not want people scared off doing this. It is a part of career progression. Thank you so much for a great conference: #abacbs17 &amp; congratulations to David Lynn &amp; his team. I loved it.</td>
<td align="right">50</td>
</tr>
<tr class="even">
<td align="left">abacbs</td>
<td align="left">Terry Speed says he had no vision: &quot;I'm a statistician, we do little things. Now when someone asks me, I say I want to cure cancer.&quot; #abacbs17</td>
<td align="right">47</td>
</tr>
<tr class="odd">
<td align="left">torstenseemann</td>
<td align="left">I knew something was up when I saw Terry Speed wearing pants at #abacbs17 ! Well deserved award 😁</td>
<td align="right">47</td>
</tr>
<tr class="even">
<td align="left">atma_ivancevic</td>
<td align="left">You know it's a #BioInformatics conference when every speaker lists their <span class="citation">@biorxivpreprint</span> and <span class="citation">@github</span> code #openscience #openaccess #sharingiscaring #abacbs17</td>
<td align="right">35</td>
</tr>
<tr class="odd">
<td align="left"><em>lazappi</em></td>
<td align="left">#abacbs17 Opening keynote <span class="citation">@HigginsDes</span> &quot;Everything you ever wanted to know about multiple alignment&quot; #sketchnotes <a href="https://t.co/zdQlKKfqCa" class="uri">https://t.co/zdQlKKfqCa</a></td>
<td align="right">35</td>
</tr>
<tr class="even">
<td align="left">RLadiesAU</td>
<td align="left">Our past first year, our vision, our speakers and sponsors in one infographic! Thanks to <span class="citation">@annaquagli</span> and to <span class="citation">@robbie_bonelli</span> for designing it! Grab one at #COMBINE17 or <span class="citation">@abacbs</span> and spread the word! <a href="https://t.co/5xcY7gxMPs" class="uri">https://t.co/5xcY7gxMPs</a></td>
<td align="right">32</td>
</tr>
<tr class="odd">
<td align="left">hdashnow</td>
<td align="left">We're in Adelaide ready for #COMBINE17 #abacbs17! Is that <span class="citation">@sahmriAU</span> in the distance? <a href="https://t.co/yQYMm4P249" class="uri">https://t.co/yQYMm4P249</a></td>
<td align="right">32</td>
</tr>
<tr class="even">
<td align="left">LonsBio</td>
<td align="left">Awwwww yeah! #ABACBS17 <a href="https://t.co/7uwXhTHlIc" class="uri">https://t.co/7uwXhTHlIc</a></td>
<td align="right">29</td>
</tr>
</tbody>
</table>

Quotes
======

Quote proportion
----------------

![](abacbs2017_files/figure-markdown_github/is-quote-1.png)

Quote count
-----------

![](abacbs2017_files/figure-markdown_github/quotes-count-1.png)

Top quotes
----------

<table style="width:88%;">
<colgroup>
<col width="23%" />
<col width="45%" />
<col width="18%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">screen_name</th>
<th align="left">text</th>
<th align="right">quote_count</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">robbie_bonelli</td>
<td align="left">Don't miss out on <span class="citation">@RLadiesAU</span> here at #COMBINE17 #abacbs17! Grab a pamphlet or simply talk to us! :D <a href="https://t.co/PddTGsmDRB" class="uri">https://t.co/PddTGsmDRB</a></td>
<td align="right">2</td>
</tr>
<tr class="even">
<td align="left">combine_au</td>
<td align="left">It's great to have <span class="citation">@RLadiesAU</span> and <span class="citation">@RLadiesAdelaide</span> representing at #COMBINE17 and #abacbs17 this week! #rstats <a href="https://t.co/kBsHrWTHkB" class="uri">https://t.co/kBsHrWTHkB</a></td>
<td align="right">2</td>
</tr>
<tr class="odd">
<td align="left">AliciaOshlack</td>
<td align="left">Obviously too easy! Before lunch on the first day. Keep going to get a full card everyone! #confbingo #abacbs17 <a href="https://t.co/2cqeH0ah6q" class="uri">https://t.co/2cqeH0ah6q</a></td>
<td align="right">2</td>
</tr>
<tr class="even">
<td align="left">LonsBio</td>
<td align="left">Winning all the prizes! #abacbs17 <a href="https://t.co/GpibqMzHQC" class="uri">https://t.co/GpibqMzHQC</a></td>
<td align="right">2</td>
</tr>
<tr class="odd">
<td align="left">annaquagli</td>
<td align="left">The second genetic eye disease treated so far #abacbs17! Cousin of #MacTel showcased by <span class="citation">@robbie_bonelli</span> <a href="https://t.co/coW9orShQw" class="uri">https://t.co/coW9orShQw</a></td>
<td align="right">2</td>
</tr>
<tr class="even">
<td align="left">combine_au</td>
<td align="left">Yay more fantastic student talks! #abacbs17 <a href="https://t.co/fYFLcM57IP" class="uri">https://t.co/fYFLcM57IP</a></td>
<td align="right">2</td>
</tr>
<tr class="odd">
<td align="left">atma_ivancevic</td>
<td align="left">When your plots are so pretty they get more tweets than your science #firstworldproblems #dataviz #abacbs17 <a href="https://t.co/ueOi8sYKqu" class="uri">https://t.co/ueOi8sYKqu</a></td>
<td align="right">2</td>
</tr>
<tr class="even">
<td align="left">abacbs</td>
<td align="left">Early #christmas festivities at <span class="citation">@sahmriAU</span> #abacbs17 <a href="https://t.co/0cUhpTWVmg" class="uri">https://t.co/0cUhpTWVmg</a></td>
<td align="right">2</td>
</tr>
<tr class="odd">
<td align="left">robbie_bonelli</td>
<td align="left">.<span class="citation">@bluebirdi</span> shows us how to give an awesome and engaging presentation even when preceded by Terry Speed! #YouAlsoHadPrettyPictures! #abacbs17 <a href="https://t.co/5DREmTEe5o" class="uri">https://t.co/5DREmTEe5o</a></td>
<td align="right">2</td>
</tr>
<tr class="even">
<td align="left">AliciaOshlack</td>
<td align="left">And doing a great job! <span class="citation">@bluebirdi</span> #abacbs17 <a href="https://t.co/QtCSCqbsow" class="uri">https://t.co/QtCSCqbsow</a></td>
<td align="right">2</td>
</tr>
</tbody>
</table>

Media
=====

Media count
-----------

![](abacbs2017_files/figure-markdown_github/has-media-1.png)

Top media
---------

<table style="width:92%;">
<colgroup>
<col width="23%" />
<col width="45%" />
<col width="22%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">screen_name</th>
<th align="left">text</th>
<th align="right">favorite_count</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">torstenseemann</td>
<td align="left">Legend. #abacbs17 <a href="https://t.co/dbIfVnV6TQ" class="uri">https://t.co/dbIfVnV6TQ</a></td>
<td align="right">76</td>
</tr>
<tr class="even">
<td align="left"><em>lazappi</em></td>
<td align="left">#abacbs17 Opening keynote <span class="citation">@HigginsDes</span> &quot;Everything you ever wanted to know about multiple alignment&quot; #sketchnotes <a href="https://t.co/zdQlKKfqCa" class="uri">https://t.co/zdQlKKfqCa</a></td>
<td align="right">35</td>
</tr>
<tr class="odd">
<td align="left">RLadiesAU</td>
<td align="left">Our past first year, our vision, our speakers and sponsors in one infographic! Thanks to <span class="citation">@annaquagli</span> and to <span class="citation">@robbie_bonelli</span> for designing it! Grab one at #COMBINE17 or <span class="citation">@abacbs</span> and spread the word! <a href="https://t.co/5xcY7gxMPs" class="uri">https://t.co/5xcY7gxMPs</a></td>
<td align="right">32</td>
</tr>
<tr class="even">
<td align="left">hdashnow</td>
<td align="left">We're in Adelaide ready for #COMBINE17 #abacbs17! Is that <span class="citation">@sahmriAU</span> in the distance? <a href="https://t.co/yQYMm4P249" class="uri">https://t.co/yQYMm4P249</a></td>
<td align="right">32</td>
</tr>
<tr class="odd">
<td align="left">LonsBio</td>
<td align="left">Awwwww yeah! #ABACBS17 <a href="https://t.co/7uwXhTHlIc" class="uri">https://t.co/7uwXhTHlIc</a></td>
<td align="right">29</td>
</tr>
<tr class="even">
<td align="left"><em>lazappi</em></td>
<td align="left">Su-In Lee &quot;Big data to personalised medicine with machine learning&quot; #abacbs17 #sketchnotes <a href="https://t.co/7v5DFP4yQ3" class="uri">https://t.co/7v5DFP4yQ3</a></td>
<td align="right">29</td>
</tr>
<tr class="odd">
<td align="left"><em>lazappi</em></td>
<td align="left">.<span class="citation">@AliciaOshlack</span> presenting on the behalf of <span class="citation">@nadia_davidson</span> who can't be here sure to being part of the <span class="citation">@MCRI_for_kids</span> Bioinformatics baby boom #abacbs17 <a href="https://t.co/mSlzXAjX5n" class="uri">https://t.co/mSlzXAjX5n</a></td>
<td align="right">27</td>
</tr>
<tr class="even">
<td align="left">torstenseemann</td>
<td align="left">Genomic Tetris is a game that needs to be written #abacbs17 <span class="citation">@jaredtsimpson</span> <span class="citation">@sjackman</span> <span class="citation">@ianholmes</span> ? <a href="https://t.co/jRaLtLpk3A" class="uri">https://t.co/jRaLtLpk3A</a></td>
<td align="right">27</td>
</tr>
<tr class="odd">
<td align="left">trashystats</td>
<td align="left">Come see me at my poster #abacbs17 <a href="https://t.co/OVbeOqWZDv" class="uri">https://t.co/OVbeOqWZDv</a></td>
<td align="right">27</td>
</tr>
<tr class="even">
<td align="left">torstenseemann</td>
<td align="left">Now <span class="citation">@hdashnow</span> speaking on pathogenic short tandem repeat expansions in humans and her STRretch software #COMBINE17 <span class="citation">@AliciaOshlack</span> <a href="https://t.co/raW4r4ZCGS" class="uri">https://t.co/raW4r4ZCGS</a></td>
<td align="right">27</td>
</tr>
</tbody>
</table>

### Most liked media image

![](http://pbs.twimg.com/media/DOpoCX0X0AAcvIW.jpg)

Tweet text
==========

The 100 words used 3 or more times.

![](abacbs2017_files/figure-markdown_github/count-words-1.png)

Who has 280 characters?
-----------------------

![](abacbs2017_files/figure-markdown_github/count-tweet-length-1.png)
