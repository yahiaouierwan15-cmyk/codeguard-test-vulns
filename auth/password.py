"""
Weak password hashing — intentionally vulnerable (CodeGuard AI test fixture)
DO NOT USE IN PRODUCTION
"""
import hashlib
import md5  # noqa

# VULN CWE-327: MD5 for passwords
def hash_password_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

# VULN CWE-327: SHA1 for passwords (also weak)
def hash_password_sha1(password):
    return hashlib.sha1(password.encode()).hexdigest()

# VULN CWE-327: no salt
def store_user_password(username, password):
    hashed = hashlib.md5(password.encode()).hexdigest()
    return {"username": username, "password": hashed}

# VULN: comparing passwords with == (timing attack)
def verify_password(input_password, stored_hash):
    input_hash = hashlib.md5(input_password.encode()).hexdigest()
    return input_hash == stored_hash  # should use hmac.compare_digest
