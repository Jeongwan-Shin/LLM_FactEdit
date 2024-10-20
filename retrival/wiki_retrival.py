from typing import Any, Dict, List, Tuple
import requests
import json
from tqdm import tqdm

class WikiRetriever:
    def __init__(self, search_url: str = ""):
        self.search_url = search_url

    # Search Function
    def search(self, query: List[str]):
        headers = {"User-Agent": "Test Client"}
        pload = {
            "query": query,
        }
        response = requests.post(self.search_url, headers=headers, json=pload)
        data = json.loads(response.content)

        outputs = data["document"]
        return outputs

    def __call__(self, data_list, batch_size: int):
        #data = data.dropna()
        #print(data.isnull().values.any())
        #assert not data.isnull().values.any(), print("There's NULL data!! Check it!!")
        #query = data["query"].tolist()
        query_list = [qry for data in data_list for qry in data["query"]]
        print("Num of queries : ",len(query_list))
        
        batch_queries_list = [query_list[i : i + batch_size] for i in range(0, len(query_list), batch_size)]
        retrival_result = []
        for batch_qry in tqdm(batch_queries_list):
            list_documents = self.search(batch_qry)
            retrival_result.append(list_documents)

        result = [item for sublist in retrival_result for item in sublist]
        #print(f"len(result): {len(result)}")
        #print(f"len(data[query]): {len(data['query'])}")
        #data_list["retrieved_doc"] = result
        
        #save_path = "retrieve/" + data_path + "_retrieved.csv"
        #data.to_csv(save_path)

        return result