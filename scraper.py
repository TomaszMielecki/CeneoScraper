import requests
from bs4 import BeautifulSoup
# product_code = input("Podaj kog produktu: ")

product_code = "87884295"

url = f"https://www.ceneo.pl/{product_code}#tab=reviews"

response = requests.get(url)
page_dom = BeautifulSoup(response.text, "html.parser")
opinions = page_dom.select("div.js_product-reviews")
all_opinions = []
for opinion in opinions:
    single_opinon = {
        "opinion_id": opinion["data-entry-id"],
        "author": opinion.select_one("span.user-post__author-name").text.strip(),
        "recomendation": opinion.select_one("span.user-post__author-recomendation > em").text.strip(),
        "rating": opinion.select_one("span.user-post__score-count").text.strip(),
        "verified": opinion.select_one("div.review-pz").text.strip(),
        "post_date": opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"].strip(),
        "purchase_date": opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"].strip(),
        "vote_up": opinion.select_one("buton.vote-yes")["data-total-vote"].strip(),
        "vote_down": opinion.select_one("buton.vote-no")["data-total-vote"].strip(),
        "content": opinion.select_one("div.user-post__text").text.strip(),
        "cons": [cons.text.strip() for cons in opinion.select_one("div.review-feature__title review-feature__title—negatives ~ div.review-feature__item")],
        "pros": [pros.text.strip() for pros in opinion.select_one("div.review-feature__title review-feature__title—positives ~ div.review-feature__item")], 
    }
    all_opinions.append[single_opinon]
    
    print(type(opinion))

