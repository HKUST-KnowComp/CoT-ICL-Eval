def direct_miniscan_prompt(dict):
    prompt = (
'''Here is a task:Your task is to convert an input sequence into an output sequence based on specific rules.
Each word in the input sequence either corresponds to a direct transformation into a word in the output sequence,
or a rule that defines how the output sequence should be structured.
'''
    )
    for i, IO_pair in enumerate(dict["train"]):
        prompt += f"Input{i + 1}: {IO_pair['input']} Output{i + 1}: {IO_pair['output']}\n"
    prompt += (
         "Your task is to predict the output sequence based on the new input sequence:\n"
        f"Input: {dict['test']['input']}\n"
        '''
Please output your final answer in the following json dict format without any explanation:

{
    "answer": "your answer"
}''')
    messages = [{"role": "user", "content": prompt}]
    return messages

def cot_miniscan_prompt(dict):
    prompt = (
'''Here is a task:Your task is to convert an input sequence into an output sequence based on specific rules.
Each word in the input sequence either corresponds to a direct transformation into a word in the output sequence,
or a rule that defines how the output sequence should be structured.
'''
    )
    for i, IO_pair in enumerate(dict["train"]):
        prompt += f"Input{i + 1}: {IO_pair['input']} Output{i + 1}: {IO_pair['output']}\n"
    prompt += (
         "Your task is to predict the output sequence based on the new input sequence:\n"
        f"Input: {dict['test']['input']}\n"
        '''
Please first perform reasoning and then output your final answer in the following json dict format:

{
    "reasoning": "your reasoning process",
    "answer": "your answer"
}''')
    messages = [{"role": "user", "content": prompt}]
    return messages

def react_miniscan_prompt(dict):
    prompt = (
'''
You should now solve the below question using the following pipeline:

Question: the input question you must answer
Thought: Think about what to do
Action: Your action process
Observation: the result of the action
(this Thought/Action/Observation can be repeated zero or more times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Here is a task:Your task is to convert an input sequence into an output sequence based on specific rules.
Each word in the input sequence either corresponds to a direct transformation into a word in the output sequence,
or a rule that defines how the output sequence should be structured.
'''
    )
    for i, IO_pair in enumerate(dict["train"]):
        prompt += f"Input{i + 1}: {IO_pair['input']} Output{i + 1}: {IO_pair['output']}\n"
    prompt += (
         "Your task is to predict the output sequence based on the new input sequence:\n"
        f"Input: {dict['test']['input']}\n"
        '''
You should respond in the following json dict format:

{
    "process": "your full problem-solving process",
    "answer": "your final answer"
}''')
    messages = [{"role": "user", "content": prompt}]
    return messages

def tot_miniscan_prompt(dict):
    prompt = (
'''
Imagine three different experts are answering this question.
All experts will write down 1 step of their thinking,
then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realises they're wrong at any point then they leave.
 
Here is a task:Your task is to convert an input sequence into an output sequence based on specific rules.
Each word in the input sequence either corresponds to a direct transformation into a word in the output sequence,
or a rule that defines how the output sequence should be structured.
'''
    )
    for i, IO_pair in enumerate(dict["train"]):
        prompt += f"Input{i + 1}: {IO_pair['input']} Output{i + 1}: {IO_pair['output']}\n"
    prompt += (
         "Your task is to predict the output sequence based on the new input sequence:\n"
        f"Input: {dict['test']['input']}\n"
        '''
You should respond in the following json dict format:

{
    "discussion": "full discussion and reasoning process of experts",
    "answer": "final agreed answer"
}''')
    messages = [{"role": "user", "content": prompt}]
    return messages