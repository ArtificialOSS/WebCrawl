import requests
import os
import re

from bs4 import BeautifulSoup
from tqdm import tqdm

from ScrapWebsite import ScrapWebsite

def CleanFilename(filename):
    cleaned = re.sub(r'[\\/:*?"<>|]', '_', filename)
    return cleaned

def Log(crawlSites, outDir):
    progress = tqdm(total=len(crawlSites), ncols=80, desc="Scraping Progress", unit="Website")
    for index, site in enumerate(crawlSites, start=1):
        text = ScrapWebsite(site)

        soup = BeautifulSoup(requests.get(site).content, 'html.parser')
        title_tag = soup.title
        title = title_tag.string if title_tag else f"website_{index}"

        cleaned_title = CleanFilename(title)
        output_file = os.path.join(outDir, f"{cleaned_title}.txt")

        # Save the scraped text to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)

        progress.set_postfix({"Website": f"{index}/{len(crawlSites)}"})
        progress.update()

    progress.close()
