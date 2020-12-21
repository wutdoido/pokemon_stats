import numpy as np
import pandas as pd
import requests
import datetime as dt
from showdown_stats import PokemonStats
import seaborn as sns
import matplotlib.pyplot as plt
from MDate import MDate

poke = PokemonStats("Umbreon")
poke.get_stats("vgc")
sns.set(rc={'figure.figsize':(9, 12)})
sns.barplot(x="usage_amount", y=poke.full_data.index, data=poke.full_data, ci=None)
plt.title("{} Usage".format(poke.name))
plt.ylabel("Month")
plt.xlabel("Usage amount")
plt.tight_layout()
plt.show()