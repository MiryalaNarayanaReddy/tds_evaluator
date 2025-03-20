import re

def q1(s):
    version_match = re.search(r"Version:\s*Code\s*(\d+\.\d+\.\d+)", s)
    os_version_match = re.search(r"OS Version:", s)
    
    return bool(version_match and os_version_match)
