import re
from security.regex_patterns import PATTERNS


def mask_sensitive_data(text):

    if not text:
        return text

    text = re.sub(
        PATTERNS["EMAIL"],
        "[EMAIL]",
        text
    )

    text = re.sub(
        PATTERNS["PHONE"],
        "[PHONE]",
        text
    )

    text = re.sub(
        PATTERNS["AADHAAR"],
        "[AADHAAR]",
        text
    )

    text = re.sub(
        PATTERNS["PAN"],
        "[PAN]",
        text
    )

    text = re.sub(
        PATTERNS["PASSWORD"],
        r"\1********",
        text
    )

    text = re.sub(
        PATTERNS["CLIENT_ID"],
        r"\1********",
        text
    )

    return text