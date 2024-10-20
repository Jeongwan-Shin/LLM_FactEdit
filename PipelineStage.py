import enum
from retrival.wiki_retrival import WikiRetriever

from prompt import (
    all_split_atomic_prompt,
    all_split_qgen_prompt,
    all_split_agreement_prompt,
    all_split_edit_prompt,
    merge_prompt,
)

class FactSplit(enum.Enum):
    """
    Which type of FactSplit from original text.
    """

    ATOMIC = enum.auto() 
    ENTITY = enum.auto()  
    SENTENCE = enum.auto()  
    
class EvidenceExtraction(enum.Enum):
    """
    Which type of EvidenceExtraction from fact.
    """

    LLM_BASED = enum.auto()  
    BING = enum.auto()  
    WIKI = enum.auto()  
    
class Pipeline_Stage(enum.Enum):
    """
    Which type of EvidenceExtraction from fact.
    """
    GEN_ATOMIC = enum.auto()  
    GEN_QUERY = enum.auto()  
    RETRIEVE = enum.auto()  
    SELECT_EVIDENCE = enum.auto()  
    FACT_CHECK = enum.auto()  
    HALU_EDIT = enum.auto()  
    MERGE = enum.auto()  
    

def get_PromptList(texts, stage):
    input_list = []
    if stage == Pipeline_Stage.GEN_ATOMIC:
        print("Extract Atomic : ", stage)
        input_list=[all_split_atomic_prompt % (text,) for text in texts]
    elif stage == Pipeline_Stage.GEN_QUERY:
        print("Generate Atomic Query: ", stage)
        input_list = [all_split_qgen_prompt % (text,) for text in texts]
    elif stage == Pipeline_Stage.FACT_CHECK:
        input_list =[all_split_agreement_prompt % (text,) for text in texts]
    elif stage == Pipeline_Stage.HALU_EDIT:
        input_list =[all_split_edit_prompt % (text,) for text in texts]
    elif stage == Pipeline_Stage.MERGE:
        input_list =[merge_prompt % (text,) for text in texts]
        
    return input_list

def check_generation(outputs, input_list, sampling_params):
    while (True):
        check_num = 0
        for i, output in enumerate(outputs):
            if isinstance(output.outputs[0].text,str):
                check_num +=1
                continue
            else:
                outputs[i] = llm.generate(input_list[i], sampling_params)[0]
        if check_num == len(outputs):
            break
    return outputs

def generate_atomic_fact(llm, ori_inputs, sampling_params):
    print("ori_inputs[0] : ", ori_inputs[0])
    # get instruction prompt
    input_list = get_PromptList(ori_inputs, Pipeline_Stage.GEN_ATOMIC)
    print("input_list[0] : ", input_list[0][1500:])
    
    # request vllm
    outputs = llm.generate(input_list, sampling_params)
    # check error 
    outputs = check_generation(outputs, input_list, sampling_params)
    print("Complete Atomic generation, Output size: ", len(outputs))
    
    # split generated text
    atomic_facts_list = []
    for output in outputs:
        atomic_generated = output.outputs[0].text
        if "- I decomposed: " in atomic_generated:
            atomic_facts_list.append(atomic_generated.split("- I decomposed: ")[1:])
        else:
            print("ERROR: I decomposed ") 
            atomic_facts_list.append(atomic_generated)
    
    return atomic_facts_list

def generate_atomic_qeury(llm, atomic_facts_list, sampling_params):

    atomic_facts_str = [[ ''.join(atomic_facts) ] for atomic_facts in atomic_facts_list]
    print("atomic_facts_str[:2] : ", atomic_facts_str[:2])
    input_list = get_PromptList(atomic_facts_str, Pipeline_Stage.GEN_QUERY)
    print("input_list[0] : ", input_list[0][1000:])
    
    outputs = llm.generate(input_list, sampling_params)
    outputs = check_generation(outputs, input_list, sampling_params)
    print("Complete Atomic generation, Output size: ", len(outputs))
    
    # split generated text
    atomic_query_list = []
    for i, output in enumerate(outputs):
        query_generated = output.outputs[0].text

        if "- I decomposed: " in query_generated or "- I decomposed : " in query_generated:
            query_generated = query_generated.replace("- I decomposed : ", "- I decomposed: ").replace("-I decomposed :","- I decomposed: ")
            query_generated = query_generated.replace("- I decomposed :", "- I decomposed: ")
            query_generated = query_generated.replace(" ->I googled : ", " -> I googled: ").replace(" -> I googled : "," -> I googled: ")
            query_generated = query_generated.replace(" ->I googled :", " -> I googled: ").replace("-> I googled:"," -> I googled: ").replace("I googled:"," -> I googled: ")
            atomic_query_sets = query_generated.split("- I decomposed: ")[1:]
        else:
            print("GENERATE QUERY ERROR CHECK, idx is ", i ) 

        atomic_QG = [atomic_query_set.split(" -> I googled: ")[0].replace("\n", "").replace(" -> ","") for atomic_query_set in atomic_query_sets
                        if atomic_query_set != ""]
        queries_QG = [atomic_query_set.split(" -> I googled: ")[-1].replace("\n", "") for atomic_query_set in atomic_query_sets
                        if atomic_query_set != ""]

        atomic_query_list.append({"query": queries_QG, "atomic_fact":atomic_QG})
    print("atomic_query_list length : ", len(atomic_query_list))
    return atomic_query_list

def evidence_doc_retrieval(atomic_queries, url):
    retriever = WikiRetriever(search_url=url)
    retrieved_data = retriever(atomic_queries, 1000)
    
    return retrieved_data

def select_evidence(llm, ori_text):
    return True

def fect_check(llm, ori_text):
    return True

def fect_edit(llm, ori_text):
    return True

def fect_merge(llm, ori_text):
    return True