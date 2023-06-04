import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


print(*[filename.removesuffix(".json") for filename in os.listdir("./opinions")],sep="\n")
product_code=input("Podaj kod produktu: ")

opinions = pd.read_json(f"opinions/{product_code}.json")
print (opinions)
opinions.score = opinions.score.map(lambda x: x.split("/")[0].replace(",",".")).astype(float)
stats = {
    "opinion_count":opinions.shape[0],
    "pros_count":opinions.pros.astype(bool).sum(),
    "cons_count":opinions.cons.astype(bool).sum(),
    "average_score":opinions.score.mean(),
}
print(f"""Dla produktu o kodzie {product_code} pobranyc zostalo {stats["opinion_count"]} opinii
Dla {stats["pros_count"]} opinii zostala podana lista zalet,
a dla {stats["cons_count"]} lista wad.
Srednia ocena wynosi {stats["average_score"]:.2f}""")

score = opinions.score.value_counts().reindex(list(np.arange(0,5.5,0.5)),fill_value=0)
score.plot.bar()

recommendation = opinions["recommendation"].value_counts(dropna = False)
recommendation.plot.pie(
    autopct = "%1.1f%%",
    labels = ["polecam", "nie polecam", "brak zdania"],
    colors = ["blue","yellow","red"] 
)

plt.show()