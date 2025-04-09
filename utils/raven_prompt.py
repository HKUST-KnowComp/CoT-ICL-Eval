def direct_raven_prompt(dict):
    prompt = f"""
Below are several rows of abstracted symbols. The symbols follow a certain rule or pattern.
Row1: {dict['data']['train'][0]['input']} {dict['data']['train'][0]['output']}
Row2: {dict['data']['train'][1]['input']} {dict['data']['train'][1]['output']}
Your task is to predict the missing symbol based on the incomplete row:
Row3: {dict['data']['test']['input']} [missing_symbol]
Please output your final answer in the following json dict format without any explanation:"""+"""
{
    "answer": "your answer"
}
"""
    messages = [{"role": "user", "content": prompt}]
    return messages

def cot_raven_prompt(dict):
    prompt = f"""
Below are several rows of abstracted symbols. The symbols follow a certain rule or pattern.
Row1: {dict['data']['train'][0]['input']} {dict['data']['train'][0]['output']}
Row2: {dict['data']['train'][1]['input']} {dict['data']['train'][1]['output']}
Your task is to predict the missing symbol based on the incomplete row:
Row3: {dict['data']['test']['input']} [missing_symbol]
Please first perform reasoning and then output your final answer in the following json dict format:"""+"""
{
    "reasoning": "your reasoning process",
    "answer": "your answer"
}
"""
    messages = [{"role": "user", "content": prompt}]
    return messages


def tot_raven_prompt(dict):
    prompt = f"""
Imagine three different experts are answering this question.
All experts will write down 1 step of their thinking,
then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realises they're wrong at any point then they leave.

Below are several rows of abstracted symbols. The symbols follow a certain rule or pattern.
Row1: {dict['data']['train'][0]['input']} {dict['data']['train'][0]['output']}
Row2: {dict['data']['train'][1]['input']} {dict['data']['train'][1]['output']}
Your task is to predict the missing symbol based on the incomplete row:
Row3: {dict['data']['test']['input']} [missing_symbol]
Please first perform reasoning and then output your final answer in the following json dict format:"""+"""
You should respond in the following json dict format:
{
    "discussion": "full discussion and reasoning process of experts",
    "answer": "final agreed answer"
}
"""
    messages = [{"role": "user", "content": prompt}]
    return messages




def react_raven_prompt(dict):
    prompt = f"""
You should now solve the below question using the following pipeline:
Question: the input question you must answer
Thought: Think about what to do
Action: Your action process
Observation: the result of the action
(this Thought/Action/Observation can be repeated zero or more times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Below are several rows of abstracted symbols. The symbols follow a certain rule or pattern.
Row1: {dict['data']['train'][0]['input']} {dict['data']['train'][0]['output']}
Row2: {dict['data']['train'][1]['input']} {dict['data']['train'][1]['output']}
Your task is to predict the missing symbol based on the incomplete row:
Row3: {dict['data']['test']['input']} [missing_symbol]
Please first perform reasoning and then output your final answer in the following json dict format:"""+"""
You should respond in the following json dict format:
{
    "process": "your full problem-solving process",
    "answer": "your final answer"
}
"""
    messages = [{"role": "user", "content": prompt}]
    return messages