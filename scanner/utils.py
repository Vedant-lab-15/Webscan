import re

def detect_xss_sql(payload):
    patterns = {
        "XSS": [r"<script.*?>.*?</script>", r"on\w+=['\"].*?['\"]"],
        "SQL Injection": [r"(\%27)|(\')|(\-\-)|(\%23)|(#)", r"(\bOR\b|\bAND\b).*(=|LIKE)"]
    }

    results = []
    for vuln, regexes in patterns.items():
        for regex in regexes:
            if re.search(regex, payload, re.IGNORECASE):
                results.append(vuln)
                break
    return list(set(results))
