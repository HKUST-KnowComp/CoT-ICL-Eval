import numpy as np


def direct_salt_prompt(dict):
    rank = [0,1,2,3]
    np.random.shuffle(rank)
    prompt = f"""
Below are several examples that convert english sentence into an output sequence based on specific rules.
Each word in the input sequence either corresponds to a translated word in the output,
or indicates a syntactic rule (e.g., repeating or reordering semantic units) for forming the output sequence.
1. English: "{dict['data']['train'][rank[0]]['input']}", Output: "{dict['data']['train'][rank[0]]['output']}"
2. English: "{dict['data']['train'][rank[1]]['input']}", Output: "{dict['data']['train'][rank[1]]['output']}"
3. English: "{dict['data']['train'][rank[2]]['input']}", Output: "{dict['data']['train'][rank[2]]['output']}"
4. English: "{dict['data']['train'][rank[3]]['input']}", Output: "{dict['data']['train'][rank[3]]['output']}"
Your task is to predict the output sequence based on the new english sentence:
"{dict['data']['test']['input']}" """ + """ 
Please output your final answer in the following json dict format without any explanation:
{
    "answer": "your answer"
}
"""
    messages = [{"role": "user", "content": prompt}] 
    return messages



def cot_salt_prompt(dict):
    rank = [0,1,2,3]
    np.random.shuffle(rank)
    prompt = f"""
Below are several examples that convert english sentence into an output sequence based on specific rules.
Each word in the input sequence either corresponds to a translated word in the output,
or indicates a syntactic rule (e.g., repeating or reordering semantic units) for forming the output sequence.
1. English: "{dict['data']['train'][rank[0]]['input']}", Output: "{dict['data']['train'][rank[0]]['output']}"
2. English: "{dict['data']['train'][rank[1]]['input']}", Output: "{dict['data']['train'][rank[1]]['output']}"
3. English: "{dict['data']['train'][rank[2]]['input']}", Output: "{dict['data']['train'][rank[2]]['output']}"
4. English: "{dict['data']['train'][rank[3]]['input']}", Output: "{dict['data']['train'][rank[3]]['output']}"
Your task is to predict the output sequence based on the new english sentence:
"{dict['data']['test']['input']}" """ + """ 
Please first perform reasoning and then output your final answer in the following json dict format:
{
    "reasoning": "your reasoning process",
    "answer": "your answer"
}
"""
    messages = [{"role": "user", "content": prompt}] 
    return messages

def react_salt_prompt(dict):
    rank = [0,1,2,3]
    np.random.shuffle(rank)
    prompt = f"""
You should now solve the below question using the following pipeline:

Question: the input question you must answer
Thought: Think about what to do
Action: Your action process
Observation: the result of the action
(this Thought/Action/Observation can be repeated zero or more times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Below are several examples that convert english sentence into an output sequence based on specific rules.
Each word in the input sequence either corresponds to a translated word in the output,
or indicates a syntactic rule (e.g., repeating or reordering semantic units) for forming the output sequence.
1. English: "{dict['data']['train'][rank[0]]['input']}", Output: "{dict['data']['train'][rank[0]]['output']}"
2. English: "{dict['data']['train'][rank[1]]['input']}", Output: "{dict['data']['train'][rank[1]]['output']}"
3. English: "{dict['data']['train'][rank[2]]['input']}", Output: "{dict['data']['train'][rank[2]]['output']}"
4. English: "{dict['data']['train'][rank[3]]['input']}", Output: "{dict['data']['train'][rank[3]]['output']}"
Your task is to predict the output sequence based on the new english sentence:
"{dict['data']['test']['input']}" """ + """ 
You should respond in the following json dict format:
{
    "process": "your full problem-solving process",
    "answer": "your final answer"
}
"""
    messages = [{"role": "user", "content": prompt}] 
    return messages

def tot_salt_prompt(dict):
    rank = [0,1,2,3]
    np.random.shuffle(rank)
    prompt = f"""
Imagine three different experts are answering this question.
All experts will write down 1 step of their thinking,
then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realises they're wrong at any point then they leave.

Below are several examples that convert english sentence into an output sequence based on specific rules.
Each word in the input sequence either corresponds to a translated word in the output,
or indicates a syntactic rule (e.g., repeating or reordering semantic units) for forming the output sequence.
1. English: "{dict['data']['train'][rank[0]]['input']}", Output: "{dict['data']['train'][rank[0]]['output']}"
2. English: "{dict['data']['train'][rank[1]]['input']}", Output: "{dict['data']['train'][rank[1]]['output']}"
3. English: "{dict['data']['train'][rank[2]]['input']}", Output: "{dict['data']['train'][rank[2]]['output']}"
4. English: "{dict['data']['train'][rank[3]]['input']}", Output: "{dict['data']['train'][rank[3]]['output']}"
Your task is to predict the output sequence based on the new english sentence:
"{dict['data']['test']['input']}" """ + """ 
You should respond in the following json dict format:
{
    "discussion": "full discussion and reasoning process of experts",
    "answer": "final agreed answer"
}
"""
    messages = [{"role": "user", "content": prompt}] 
    return messages