"""
JWT vulnerabilities — intentionally vulnerable (CodeGuard AI test fixture)
DO NOT USE IN PRODUCTION
"""
import jwt
import json

# VULN CWE-347: algorithm=none disables signature verification
def decode_token_unsafe(token):
    return jwt.decode(token, options={"verify_signature": False})

# VULN CWE-347: explicitly specifying "none" algorithm
def decode_with_none_alg(token):
    return jwt.decode(token, "", algorithms=["none"])

# VULN CWE-321: hardcoded JWT secret
SECRET = "hardcoded-secret-key"

def encode_with_hardcoded_secret(payload):
    return jwt.encode(payload, "hardcoded-secret-key", algorithm="HS256")

def decode_with_hardcoded_secret(token):
    return jwt.decode(token, "hardcoded-secret-key", algorithms=["HS256"])

# VULN: accepting both none and HS256 — attacker can switch to none
def verify_token(token):
    return jwt.decode(token, SECRET, algorithms=["HS256", "none"])
