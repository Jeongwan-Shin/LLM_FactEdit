import os
import torch
from tqdm import tqdm
import csv
import pandas as pd

class Halu_dataset():
    def __init__(self, args):
        self.data_path = "data/" + args.data_type + "_data.csv" 
        self.data_csv = pd.read_csv(self.data_path)
        
        self.ori_inputs = list(self.data_csv["input"])[:50] # Test 중
        self.atomic_facts = []
        self.atomic_queries = {}
        self.retrieved_docs = {}
        self.selected_evids = {}
        self.atomic_edit_facts = {}
        self.merge_text = []
        
    def __len__(self):
        return len(self.ori_inputs)