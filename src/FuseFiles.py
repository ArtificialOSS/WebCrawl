import os

from tqdm import tqdm

def MergeFiles(directory, outputFile):
    with open(outputFile, 'w', encoding='utf-8') as output:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)

            if os.path.isfile(filepath) and filename.endswith('.txt'):
                with open(filepath, 'r', encoding='utf-8') as file:
                    output.write(file.read())
                    output.write('\n')
