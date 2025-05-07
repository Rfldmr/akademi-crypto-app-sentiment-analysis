from google_play_scraper import Sort, reviews_all
import pandas as pd

scrapreview= reviews_all(
    'com.akademi.crypto',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT
)

app_reviews_df = pd.DataFrame(scrapreview)
app_reviews_df.to_csv('Dataset/akademicrypto_playstore_review.csv', index=None, header=True)

print(f"Total ulasan yang berhasil diambil: {len(app_reviews_df)}")