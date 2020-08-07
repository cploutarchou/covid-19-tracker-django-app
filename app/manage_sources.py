import os
stats_files = list()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/covid"

directory = os.path.join(BASE_DIR, "sources")
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".csv"):
            stats_files.append(file)
