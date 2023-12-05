import re


extract_patterns = [
    {
        "match": r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    },
    {
        "match": r"https?://\w*\.(?:\w*\.){1,4}.*\/\""
    }
]

for pattern in extract_patterns:
    pattern["compiled_match"] = re.compile(pattern["match"])


with open("sample-log.log", "r") as file:
    logs = file.readlines()

    for log in logs:
        for pattern in extract_patterns:
            matched = pattern["compiled_match"].findall(log)
            if matched:
                print(matched)
