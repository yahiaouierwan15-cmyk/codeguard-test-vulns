"""
Hardcoded secrets — intentionally vulnerable (CodeGuard AI test fixture)
DO NOT USE IN PRODUCTION — these are EXAMPLE values for scanner validation
"""

# VULN CWE-798: Hardcoded AWS credentials (AWS documentation example keys)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"  # matches AKIA[A-Z0-9]{16} pattern
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = "us-east-1"

# VULN CWE-798: Hardcoded Stripe test key
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = "pk_test_51ExampleCodeguardTestFixture0000000000"

# VULN CWE-798: Hardcoded database password
DB_PASSWORD = "SuperS3cr3tP@ssword!"
DB_URL = "postgresql://admin:SuperS3cr3tP@ssword!@prod-db.internal:5432/appdb"

# VULN CWE-798: Hardcoded JWT secret (plain string)
JWT_SECRET = os.environ.get("JWT_SECRET")

# VULN: API key embedded as string literal
INTERNAL_API_KEY = "api_key_codeguard_test_0123456789abcdef0123456789abcdef"
WEBHOOK_SECRET = "whsec_EXAMPLECODEGUARDTESTFIXTURE1234567890="