import json
import os

project_dir = os.path.dirname(os.path.realpath(__file__))
meta_data = "test"
with open(os.path.join(project_dir, 'test'), 'w') as fb:
    json.dump(meta_data, fb, ensure_ascii=False)