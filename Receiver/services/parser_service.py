import json
from datetime import datetime

def parse_output(output: str):
    start = output.find("{")
    stop = output.find("}")
    output = json.loads(output[start:stop+1].replace("'", '"'))
    output["sent_time"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return output