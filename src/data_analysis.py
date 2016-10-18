import pandas as pd
from os import listdir
from os.path import isfile, join


DEFAULT_WORKSPACE = "/Users/Melancardie/Dropbox/documents/My Research/NYU/Sundararajan/Replacable Jobs/"
DEFAULT_DATA_DIR = DEFAULT_WORKSPACE+"data/db_21_0_text/"

def import_datasets(dir=DEFAULT_DATA_DIR):
    all_files = [f for f in listdir(dir) if isfile(join(dir, f))]
    datasets = {}
    for file_name in all_files:
        df_name = file_name[:-4].replace(",", "").replace(" ", "_")
        datasets[df_name]=pd.read_csv(dir+file_name, sep='\t', na_values=['n/a'])
    return datasets
