import numpy as np

def direct_list_prompt(dict, num_demos = 3):
    demos = dict["data"]['train']    
    demos_text = ""
    indices = np.random.choice(len(demos), num_demos, replace=False)
    for i in range(num_demos):
        demos_text += f"Input{i+1}: {demos[indices[i]]['input']} Output{i+1}: {demos[indices[i]]['output']} \n"

    prompt = f"Below are several examples of input and output lists. There exists an underlying python function that maps the input list to the output list.\n\
"+demos_text+f"\
Your task is to predict the output list based on the new input list:\n\
Input: {dict['data']['test']['input']}"
    prompt += """ 
Please output your final answer in the following json dict format without any explanation:
{
    "answer": "your answer"
}"""
    messages = [{"role": "user", "content": prompt}]

    return messages


def cot_list_prompt(dict, num_demos = 3):
    demos = dict["data"]['train']    
    demos_text = ""
    indices = np.random.choice(len(demos), num_demos, replace=False)
    for i in range(num_demos):
        demos_text += f"Input{i+1}: {demos[indices[i]]['input']} Output{i+1}: {demos[indices[i]]['output']} \n"

    prompt = f"Below are several examples of input and output lists. There exists an underlying python function that maps the input list to the output list.\n\
"+demos_text+f"\
Your task is to predict the output list based on the new input list:\n\
Input: {dict['data']['test']['input']}"
    prompt += """
Please first perform reasoning and then output your final answer in the following json dict format:
{
    "reasoning": "your reasoning process",
    "answer": "your answer"
}
"""
    messages = [{"role": "user", "content": prompt}]

    return messages


def react_list_prompt(dict, num_demos = 3):
    demos = dict["data"]['train']    
    demos_text = ""
    indices = np.random.choice(len(demos), num_demos, replace=False)
    for i in range(num_demos):
        demos_text += f"Input{i+1}: {demos[indices[i]]['input']} Output{i+1}: {demos[indices[i]]['output']} \n"

    prompt = """ 
You should now solve the below question using the following pipeline:

Question: the input question you must answer
Thought: Think about what to do
Action: Your action process
Observation: the result of the action
(this Thought/Action/Observation can be repeated zero or more times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
"""
    prompt += f"Below are several examples of input and output lists. There exists an underlying python function that maps the input list to the output list.\n\
"+demos_text+f"\
Your task is to predict the output list based on the new input list:\n\
Input: {dict['data']['test']['input']}"
    prompt += """
You should respond in the following json dict format:
{
    "process": "your full problem-solving process",
    "answer": "your final answer"
}
"""
    messages = [{"role": "user", "content": prompt}]

    return messages

def tot_list_prompt(dict, num_demos = 3):
    demos = dict["data"]['train']    
    demos_text = ""
    indices = np.random.choice(len(demos), num_demos, replace=False)
    for i in range(num_demos):
        demos_text += f"Input{i+1}: {demos[indices[i]]['input']} Output{i+1}: {demos[indices[i]]['output']} \n"

    prompt = """ 
Imagine three different experts are answering this question.
All experts will write down 1 step of their thinking,
then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realises they're wrong at any point then they leave.
"""
    prompt += f"Below are several examples of input and output lists. There exists an underlying python function that maps the input list to the output list.\n\
"+demos_text+f"\
Your task is to predict the output list based on the new input list:\n\
Input: {dict['data']['test']['input']}"
    prompt += """
You should respond in the following json dict format:
{
    "discussion": "full discussion and reasoning process of experts",
    "answer": "final agreed answer"
}
"""
    messages = [{"role": "user", "content": prompt}]

    return messages