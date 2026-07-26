PATTERNS = {

    "EMAIL":
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",

    "PHONE":
    r"\b\d{10}\b",

    "AADHAAR":
    r"\b\d{4}\s?\d{4}\s?\d{4}\b",

    "PAN":
    r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",

    "PASSWORD":
    r"(?i)(password\s*[:=]\s*)(\S+)",

    "CLIENT_ID":
    r"(?i)(client[\s_-]?id\s*[:=]\s*)(\S+)"
}