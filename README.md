# Ceneoscraper
#selektory skladowych

| **skladowa** | **nazwa** | **selektor** |
| --- | --- | --- |
| opinia | opinion | div.js\_product-review |
| Identyfikator opinii | opinion\_id | [data-entry-id] |
| autor | autor | span.user-post\_\_author-name |
| rekomendacja | recomendation | span.user-post\_\_author-recomendation \> em |
| Liczba gwiazdek | score | span.user-post\_\_score-count |
| Potwierdzone zakupem | purchased | div.review-pz |
| Data wystawienie | opinion\_date | span.user-post\_\_published \> time:nth-child(1)[datetime] |
| Data zakupu | purchase\_date | span.user-post\_\_published \> time:nth-child(2)[datetime] |
| Ile uznalo za przydatna | likes | button.vote-yes \> span |
| Ile za nieprzydtana | dislikes | button.vote-no \> span |
| Tresc opinii | content | div.user-post\_\_text |
| Wady | cons | div.review-feature\_\_title—negatives ~ div.review-feature\_\_item |
| Zalety | prons | div.review-feature\_\_title—positives ~ div.review-feature\_\_item |

## wykorzystane biblioteki
-Requests
-BeautifulSoup
-Os
-Sson
-Pandas
-Matplotlib
-Numpy