# tests/poc_secret_presence_fail.py
import os
def test_poc_secret_presence_fail():
    """
    Detect presence of a secret env var named HF_TOKEN_TEST (or HF_TOKEN if you want to test the real name).
    This test intentionally fails if it finds the env var, printing 'SECRET_PRESENT' in the failure message.
    NOTE: Failing a test will mark the CI run as failed.
    """
    secret_name = "HF_TOKEN_TEST"  # or "HF_TOKEN" if you want to test the actual secret name
    present = secret_name in os.environ and bool(os.environ[secret_name])
    # If present, fail with a message that appears in logs
    assert not present, f"DETECTED_SECRET_{secret_name}=True"
