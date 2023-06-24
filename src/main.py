import json
import os
import datetime

from Logging import Log
from FuseFiles import MergeFiles

with open("CrawlList.json", 'r') as file:
    data = json.load(file)

crawl_sites = data["CrawlSites"]
print("\nWebsites: (", str(len(crawl_sites)), ")")

today = datetime.datetime.now()
dateID = int(today.timestamp() * 1000)

CompiledDirectory = os.path.join(os.environ['TEMP'], 'WebCrawl-Compiled')
ScrapFilesDirectory = os.path.join(os.environ['TEMP'], f'WebCrawl_{dateID}')

os.makedirs(ScrapFilesDirectory, exist_ok=True)
os.makedirs(CompiledDirectory, exist_ok=True)

output_file = os.path.join(CompiledDirectory, f'WebCrawl_{dateID}.txt')

try:
    Log(crawl_sites, ScrapFilesDirectory)
except KeyboardInterrupt:
    MergeFiles(ScrapFilesDirectory, output_file)
    print("Output files saved in:", CompiledDirectory)
    exit(0)

print("Scraping complete.")

MergeFiles(ScrapFilesDirectory, output_file)

print("Output files saved in:", CompiledDirectory)
