import json

def apply_operation(document, operation):
    cursor_position = 0
    output_document = ""
    
    for op in operation:
        if "op" not in op:
            return None

        if op["op"] == "skip":
            if "count" not in op or cursor_position + op["count"] > len(document):
                return None
            output_document += document[cursor_position:cursor_position + op["count"]]
            cursor_position += op["count"]
        elif op["op"] == "insert":
            if "chars" not in op:
                return None
            output_document += op["chars"]
            cursor_position += len(op["chars"])
        elif op["op"] == "delete":
            if "count" not in op or cursor_position + op["count"] > len(document):
                return None
            cursor_position += op["count"]
        else:
            return None
    
    output_document += document[cursor_position:]
    return output_document

def validate_ot(stale_contents, latest_contents, operations_json):
    try:
        operations = json.loads(operations_json)
    except json.JSONDecodeError:
        return False

    result = apply_operation(stale_contents, operations)
    return result == latest_contents

# Test example
stale_contents = "Nice day!"
latest_contents ="Nice day!"
operations_json = '[{"op": "skip", "count": 4}, {"op": "insert", "chars": " day"}]'

print(validate_ot(stale_contents, latest_contents, operations_json))  # Should print True
