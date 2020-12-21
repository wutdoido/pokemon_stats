# pokemon_stats

The main "showdown_stats.py" file has an initializer that takes in a Pokemon name "name". From here, it will attempt to load a local csv file that has the usage stats. If none is found, it sets it as "none"

the main public method is get_stats(format, year, month). This method currently only supports "vgc" as the format input, and defaults the year and month to 2014 and 1, the earliest possible values for data to be found on Pokemon Showdowns stats. It will then parse through all vgc usage information from the entered time period to present, and save all the information as a dataframe, then save it locally. From there, you can plot the data using seaborn as desired. The typical entries of interest are "usage_amount" and "usage_percent" plotted with the date, which is set as the index.

test.py shows an example using Umbreon as the default pokemon.

Possible future expansions on this: Smogon uses a tiering system for singles which constantly change on a nearly month-to-month basis. So while constructing usage information for those pokemon is possible, and probably easy, finding a way to do it that doesn't take 10s of minutes at a time is not. There's probably a way to do it, such as finding a site that has all of the tier histories for a pokemon, or scouting adjacent tiers once the pokemon in question is found in one, but that's not a guaranteed solution to the problem. If I think of an idea, I will probably implement it.

MDate.py is not really used here except for storing date information, but it's mostly a small test in inheritence and overloading that I wanted to do. 

