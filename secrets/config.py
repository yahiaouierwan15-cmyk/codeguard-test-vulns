"""
Hardcoded secrets — intentionally vulnerable (CodeGuard AI test fixture)
DO NOT USE IN PRODUCTION — these are EXAMPLE values for scanner validation
"""

# VULN CWE-798: Hardcoded AWS credentials (AWS documentation example keys)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"  # matches AKIA[A-Z0-9]{16} pattern
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = "us-east-1"

# VULN CWE-798: Hardcoded Stripe test key
STRIPE_SECRET_KEY = "sk_test_51ExampleCodeguardTestFixture00000000000000"
STRIPE_PUBLISHABLE_KEY = "pk_test_51ExampleCodeguardTestFixture0000000000"

# VULN CWE-798: Hardcoded database password
DB_PASSWORD = "SuperS3cr3tP@ssword!"
DB_URL = os.environ.get("DATABASE_URL")

# VULN CWE-798: Hardcoded JWT secret (plain string)
JWT_SECRET = "my-hardcoded-jwt-secret-never-do-this"

# VULN: API key embedded as string literal
INTERNAL_API_KEY = "api_key_codeguard_test_0123456789abcdef0123456789abcdef"
WEBHOOK_SECRET = "whsec_EXAMPLECODEGUARDTESTFIXTURE1234567890="