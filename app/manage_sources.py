import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.join(base_dir, "sources")


def get_files():
    stats_files = list()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                stats_files.append(f"{directory}/{file}")
    return stats_files
