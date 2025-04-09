def direct_cogs_prompt(dict):
    lines = []
    lines.append(f"Below are several examples of input and output strings. There exist a function that maps the input string to the output string.")
    for i in range(10):
        lines.append(f"""Input{i+1}: {dict['data']['train'][i]['input']} Output{i+1}: {dict['data']['train'][i]['output']}""")
    lines.append(f"""Now, based on the new input string, please directly provide the output string.""")
    lines.append(f"""Input: {dict['data']['test']['input']}""")
    lines.append(f"""Your output should very strictly follow the json dict format below. All your answers must be within the curly braces:"""+"""
{
"output": "your output string"
}
""")
    prompt = "\n".join(lines)
    messages = [{"role": "user", "content": prompt}]
    return messages

def cot_cogs_prompt(dict):
    lines = []
    lines.append(f"Below are several examples of input and output strings. There exist a function that maps the input string to the output string.")
    for i in range(10):
        lines.append(f"""Input{i+1}: {dict['data']['train'][i]['input']} Output{i+1}: {dict['data']['train'][i]['output']}""")
    lines.append(f"""Now, based on the new input string, please directly provide the output string.""")
    lines.append(f"""Input: {dict['data']['test']['input']}""")
    lines.append(f"""Your output should very strictly follow the json dict format below. All your answers must be within the curly braces:"""+"""
{
"reasoning": "your reasoning steps",
"output": "your output string"
}
""")
    prompt = "\n".join(lines)
    messages = [{"role": "user", "content": prompt}]
    return messages
    


def tot_cogs_prompt(dict):
    lines = []
    lines.append(f"""
Imagine three different experts are answering this question.
All experts will write down 1 step of their thinking,
then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realises they're wrong at any point then they leave.
                 """)
    lines.append(f"Below are several examples of input and output strings. There exist a function that maps the input string to the output string.")
    for i in range(10):
        lines.append(f"""Input{i+1}: {dict['data']['train'][i]['input']} Output{i+1}: {dict['data']['train'][i]['output']}""")
    lines.append(f"""Now, based on the new input string, please provide the output string.""")
    lines.append(f"""Input: {dict['data']['test']['input']}""")
    lines.append(f"""Your output should very strictly follow the json dict format below. All your answers must be within the curly braces:"""+"""
{
"discussion": "full discussion and reasoning process of exeperts",
"output": "final agreed answer"
}
""")
    prompt = "\n".join(lines)
    messages = [{"role": "user", "content": prompt}]
    return messages
    




def react_cogs_prompt(dict):
    lines = []
    lines.append(f"""
You should now solve the below question using the following pipeline:
Question: the input question you must answer
Thought: Think about what to do
Action: Your action process
Observation: the result of the action
(this Thought/Action/Observation can be repeated zero or more times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
                 """)
    lines.append(f"Below are several examples of input and output strings. There exist a function that maps the input string to the output string.")
    for i in range(10):
        lines.append(f"""Input{i+1}: {dict['data']['train'][i]['input']} Output{i+1}: {dict['data']['train'][i]['output']}""")
    lines.append(f"""Now, based on the new input string, please provide the output string.""")
    lines.append(f"""Input: {dict['data']['test']['input']}""")
    lines.append(f"""Your output should very strictly follow the json dict format below. All your answers must be within the curly braces:"""+"""
{
"process": "your full problem-solving process",
"output": "your final output string"
}
""")
    prompt = "\n".join(lines)
    messages = [{"role": "user", "content": prompt}]
    return messages
