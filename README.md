# WorldBrain Webmarks

WorldBrain Webmarks is an open souce web research tool for science communicators.
It aims to make the 2 main elements of online research more efficient: Content Discovery and Knowledge Management.

## Key features:

#### Short Term (~2 months)

 - Automatically retrieve related content and meta information for articles, blog posts and scientific papers from a **personal/science community-trusted** network of blogs, news outlets, facebook groups/pages and scholarly(PubMed) or governmental(FDA) databases.
 - Perform individual searches through all of those sources at once, instead of searching every page manually or the whole web via google. 
 
**Help neeed:** We currently gather a set of sources to index for the relevancy search. So if you want to help us, send us an email with a list of resources you want to have **or** use [our handy bookmarklet](https://github.com/WorldBrain/metabrowser/blob/master/helper_processes/bookmarklet_send.txt), you can click everytime you visit a page you like. It then anonymously sends the current domain to us and we can start indexing it. 

#### Medium Term (~6 months)

 - Providing more ways of retreiving meta information like Altmetric data, author information, citations etc. etc. 
 - Customise the choice of sources to get relevant content from and to search through.

#### Long Term (~1 year)

 - There are endless possibilities in how you can put a page in context - and we surely won't cover all. This is why we want to publish this as open source library that allows data scientists to develop, use or distribute their individual meta-browsing scripts to WorldBrain users. 
 - Bookmarking and annotating of web content. 
 

## Demo

To get an idea of the look and feel, take a look at our demo video of the proof of concept or try it out yourself. 

How to try it out:

 1. Get a Hypothes.is account (optionally, install their plugin)
 2. Join related article group (Just open and close the page again)
 3. Drag and drop this text into your bookmark bar
 4. Press the "WorldBrain Related Articles"-button whenever you want to get related content for a website.
 5. Wait a few seconds for Hypothes.is to refresh or switch groups back and forth to do so manually.


**Important:** Some websites block bookmarklets and therefore the sidebar won't open automatically. Use the [Hypothes.is browser plugin](http://www.hypothes.is) instead then.
We also saw that in rare cases Hypothes.is doesn't show the elements in the sidebar although they are saved. ([We already filed this bug](https://github.com/hypothesis/h/issues/3518))

In this case you can access them via the dashboard you find in the top right corner of the sidebar, when clicking on your user name. ([Screenshot](http://www.worldbrain.io/wp-content/uploads/2016/06/Screen-Shot-2016-06-22-at-11.14.30.png))


## Current State & Roadmap

We just published our first proof of concept with the channel "Related Content" which is powered by [Laterals News API](https://lateral.io/publishing) and is broadcasted into a [Hypothes.is group](https://hypothes.is/groups/KG9bL1Bm/related-articles).

Currently we are working on the feature of retrieving relevant content from a **science community-trusted** network of blogs, news outlets, facebook groups/pages and scholarly(PubMed) or governmental(FDA) databases.

## How to currently contribute best
 1. [Check out some open tasks to code on](https://github.com/WorldBrain/Webmarks/issues)
 2. [Showing us which which websites you trust and we should index first](https://github.com/WorldBrain/Webmarks/blob/master/helper_processes/bookmarklet_send.txt)
 

