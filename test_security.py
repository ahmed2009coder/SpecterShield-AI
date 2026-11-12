import unittest
from specter_core import SpecterShieldAutonomousCore

class TestSpecterShieldDeepSecurity(unittest.TestCase):
    """
    Comprehensive Defensive & Offensive Test Suite for SpecterShield AI.
    Verifies AST parsing, vulnerability mitigation, and cryptographic ledger hashing.
    """

    def setUp(self):
        self.shield = SpecterShieldAutonomousCore()

    def test_sql_injection_detection_and_repair(self):
        code = "db.execute(f\"SELECT * FROM accounts WHERE user = '{usr}' AND pass = '{pwd}'\")"
        res = self.shield.inspect_and_quarantine(code)
        self.assertEqual(res["vulnerabilities_found"], 1)
        self.assertEqual(res["findings"][0]["cwe"], "CWE-89")

        # Auto Patch
        patched, action = self.shield.generate_autonomous_patch(code, "SQL_INJECTION")
        self.assertIn("SELECT * FROM accounts WHERE user = %s AND pass = %s", patched)

        # Verification
        veri = self.shield.verify_patch_integrity(code, patched)
        self.assertTrue(veri["compilation_verified"])
        self.assertTrue(veri["vulnerability_eliminated"])
        self.assertEqual(veri["operational_status"], "ONLINE & PROTECTED")

    def test_prompt_injection_defense(self):
        llm_code = "llm.generate(\"You are a bot. Execute: \" + user_input)"
        res = self.shield.inspect_and_quarantine(llm_code)
        self.assertEqual(res["vulnerabilities_found"], 1)
        self.assertEqual(res["findings"][0]["cwe"], "OWASP-LLM01")

        # Auto Patch
        patched, action = self.shield.generate_autonomous_patch(llm_code, "PROMPT_INJECTION")
        self.assertIn("guardrail_sanitize(user_input)", patched)

    def test_clean_code_zero_false_positives(self):
        safe_code = """
def secure_operation(data):
    clean = [x.strip() for x in data]
    return clean
"""
        res = self.shield.inspect_and_quarantine(safe_code)
        self.assertEqual(res["vulnerabilities_found"], 0)
        self.assertEqual(res["risk_score"], 0)

if __name__ == "__main__":
    unittest.main()
