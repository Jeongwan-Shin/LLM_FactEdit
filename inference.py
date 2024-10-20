import argparse
import pandas as pd
import time
import numpy as np
import torch
import random
import csv

import os
os.environ["TRANSFORMERS_CACHE"] = "/root/nas_yh/huggingface_model_load"

from vllm import LLM, SamplingParams
from data_utils.dataset import Halu_dataset
from PipelineStage import generate_atomic_fact, generate_atomic_qeury, evidence_doc_retrieval

# fixed seed
def setup_seed(seed: int = 42):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    random.seed(seed)
    
def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("--data_type", required=True, help="nq(NQ), sqa(SQA), haluqa(HaluQA)")
    parser.add_argument("--n_gpu",  type=int, required=True, help="number of GPUs")
    parser.add_argument("--search_url", required=True, help="Write a Search API server IP")
    
    #model arg
    parser.add_argument("--model_download_dir", required=True, help="Write model download directory")
    parser.add_argument("--model_size", type=int, help="Write a model size")
    parser.add_argument("--model_name", required=True, help="Write a model size")
    
    args = parser.parse_args()
    
    return args
    
def main():
    args = get_arguments()
    print("args:", args)
    
    # sampling Parameters
    sampling_params = SamplingParams(temperature = 0.0, max_tokens = 500, stop = "\n\n", frequency_penalty = 1.0)

    test_dataset = Halu_dataset(args)
    print("Test data size: ", len(test_dataset))
    
    # load vllm
    llm = LLM(model=args.model_name, download_dir=args.model_download_dir, tensor_parallel_size=args.n_gpu)
    
    # Extract Atomic
    test_dataset.atomic_facts = generate_atomic_fact(llm, test_dataset.ori_inputs, sampling_params)
    print("CHECK: ", len(test_dataset.atomic_facts))
    print("CHECK ATOMIC[:2]: ", test_dataset.atomic_facts[:2])
    
    # Generate Query
    test_dataset.atomic_queries = generate_atomic_qeury(llm, test_dataset.atomic_facts, sampling_params)
    print("CHECK: ", len(test_dataset.atomic_queries))
    print("CHECK QUERY[:2]: ", test_dataset.atomic_queries[:2])
    
    # evidence_doc_retrieval
    test_dataset.retrieved_docs = evidence_doc_retrieval(test_dataset.atomic_queries ,args.search_url)
    print("CHECK: ", len(test_dataset.retrieved_docs))
    print("CHECK RETRIEVED DOCS[:2]: ", test_dataset.retrieved_docs[:2])
    
    # select_evidence
    
    # fect_check
    
    # fect_edit
    
    # fect_merge
    
    
if __name__ == "__main__":
    main()