# codeguard-test-vulns

> ⚠️ **INTENTIONALLY VULNERABLE** — Test fixtures for [CodeGuard AI](https://github.com) security scanner.
> 
> **DO NOT deploy this code. DO NOT use in production.**

This repository contains deliberately insecure code to validate CodeGuard AI's detection capabilities.

## Vulnerabilities included

| File | Vulnerability | CWE | OWASP |
|------|--------------|-----|-------|
| `python/sql_injection.py` | SQL Injection (concat, f-string, %) | CWE-89 | A03 |
| `javascript/sql_injection.js` | SQL Injection (template literals) | CWE-89 | A03 |
| `secrets/config.py` | Hardcoded AWS/OpenAI/Stripe secrets | CWE-798 | A07 |
| `auth/jwt_auth.py` | JWT algorithm=none, hardcoded secret | CWE-347/321 | A02 |
| `python/command_injection.py` | Command Injection (os.system, subprocess shell=True) | CWE-78 | A03 |
| `python/path_traversal.py` | Path Traversal (no sanitization) | CWE-22 | A01 |
| `javascript/xss.js` | XSS via innerHTML / eval | CWE-79 | A03 |
| `auth/password.py` | MD5/SHA1 password hashing | CWE-327 | A02 |

## Expected scanner results

- **Semgrep**: SQL injection, JWT algorithm=none, hardcoded JWT secrets, command injection, MD5 passwords
- **TruffleHog**: AWS keys, OpenAI key, Stripe live key, GitHub token

## Scanner command

```bash
semgrep --config=auto .
trufflehog filesystem .
```
