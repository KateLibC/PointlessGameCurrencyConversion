# Cariad's pointless game currency converter

## Introduction

This tool will take either US dollars or in-game currencies and convert them. The 
purpose is to have fun and realise how grounded in reality a game might be.

It was written as a joke by Cariad Keigher (@KateLibC on Twitter and Twitch).

## Use and requirements

This tool was written using Python 3, so any computer with Python 3.7 or greater 
should be able to use it.

You can see what commands are available as follows:

`python3 converter.py -h`

If you want to convert $1 USD to rupees, you can do the following:

`python3 converter.py --usd 1 zelda_botwr`

If you want to convert 1 rupee instead, you can use the following:

`python3 converter.py 1 zelda_botwr`

Conversion between two different games' currencies is not an option as of yet, but 
should be in a future release.

## Examples of what you can learn

Game currencies often have very weird scaling and as a result we can learn some unusual 
aspects of the universe economy we're working with.

* Link's home in Breath of the Wild costs 3,000 rupees which is $450 US
* A can of Coca Cola in Dark Souls requires 150 human souls

This should not be used as any definitive source as this was not written by someone 
who has experience in economics. These are just guesses at best!

## Sources

Some of the conversions were done by the author or with input from others. If you believe 
that any of these could be done better, feel free to make a pull request!

### Apples from various games

The following games have apples available for purchase:

* Legend of Zelda, Breath of the Wild (`zelda_botwr`)
* "Old School" Runescape (`osrunescape`)
* Final Fantasy VII (`ff_vii_gil`)

Based on a [tweet](https://twitter.com/KateLibc/status/1199176672701870080) this author 
made in late-2019, we can use the cost of a single apple in Breath of the Wild costing 
5 rupees.

The real world has apples costing between $0.75 CAD to $1.25 CAD depending on variety. This 
is based on grocery store prices and the average weight of an apple.

Because of this, it's safe to assume that 1 rupee is a fifth of a Canadian dollar, or $0.15 USD.

This same logic can apply to other games that indicate the cost of an apple. Some games don't 
explicitly label some items as an apple but are otherwise drawn as one and are considered 
"fruit", so we'll use them this way too.

### Durians in Hyrule Warriors: Age of Calamity (`zelda_aocr`)

Unlike Breath of the Wild, apples don't exist so it should be presumed at some point after 
Ganon messed up the whole place that some mutation occurred and we ended up with them.

However, we still have durians! An in-game durian costs 15 rupees. Using this knowledge, we can 
look up the average price of the fruit. Per 
[some study on Malaysian retail prices](https://www.statista.com/statistics/1000890/malaysia-average-retail-price-d24-durian/),
we're looking at 18.9 MYR per kilogram (in 2019), which should come out to $4.49 USD. 

A consistent answer on what an average durian weighs is really difficult to determine,
but it seems to be between 1 and 3 KG, so let's just say 2 KG and leave it. This would arrive
at $9.48 USD for a single fruit.

We can then use this result to suggest that each Age of Calamity rupee is worth $0.632 USD.

## Final Fantasy XV noodles (`ff_xv_gil`)

You can sell a Cup Noodles (an actual real world item in a fantasy world) for 110 Gil and 
buy at 220. At the time of writing, retail pricing is $0.82 USD per item, meaning that 1 
Gil in the game is $0.00373 USD assuming the buy price is the best use.

### Titanite shards in Dark Souls (`darksouls`)

Dark Souls uses "Souls" as in-game currency.

So the one item in Dark Souls that we can relate back to the real world and come up with a cost 
is titanite. A 13.45 gram chunk of raw titanite from an Etsy seller costs about $22 CAD.

Let's assume that a titanite chunk weighs that amount, meaning per gram, titanite is $1.64 CAD.

You will eventually have the ability to trade the chunk for three large titanite shards. The 
shards otherwise sell for 3,800-4,000 souls.

Assuming the shards are equally split apart, they weigh about 4.48 grams or are worth $7.35 CAD 
each.

Splitting the difference, the shards are worth 3,900 souls each on the market. This means that 
a gram of titanite is worth 871 souls.

Converting a soul to US dollars, a soul is worth $0.008, meaning it's not even worth a cent. 

One other thing: copper coins are worth 1000 souls or $8 USD, silver are 3000 or $24 USD, and 
gold is 5000 or $40 USD.

### Star Wars Credits

There are two known types of credits in the Star Wars universe.

A Galactic Credit (`starwars_rc`) which is found in Star Wars Knights of the Old Republic (KOTOR) 
is reportedly worth $0.62 USD. These two values were sourced from a 
[forum post](https://www.swtor.com/community/showthread.php?t=442915), which used the cost of food 
at a diner to figure this out. Other suggestions imply that it may be as high as $1.40 USD but we 
can settle with this value.

There are also Imperial Credits (`starwars_ic`), which have a value of $1.44 USD per, based on the work 
found in this [blog](https://www.travelmoneyoz.com/blog/news-other/learn-you-will-guide-intergalactic-currencies) 
from an Australian currency converter. These are found in games after the fall of the republic.

If there are any other known credits in this universe, they can be added in.

## Licence

The code is free to use as long as it is not for commercial purposes. I am not going to attach a 
specific licence to this, but you must provide a link to repository if you opt to use it in your own 
project.