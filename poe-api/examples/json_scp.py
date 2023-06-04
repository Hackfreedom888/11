import json
from collections import deque

queue = deque()

with open('samples.json', 'r') as f:
    data = json.load(f)

for index, instance in enumerate(data['instances'], start=1):
    input_text = instance['input']
    output_text = instance['output']
    data_structure = (index, input_text, output_text)
    queue.append(data_structure)

while queue:
    data_structure = queue.popleft()
    print(f"Index: {data_structure[0]}, Input: {data_structure[1]}, Output: {data_structure[2]}")
