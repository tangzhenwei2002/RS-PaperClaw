from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from services.digest_builder import build_digest_with_llm, is_invalid_digest_institution
from services.paper_analysis import is_valid_institution_text


class InstitutionValidationTest(unittest.TestCase):
    def test_rejects_body_text_bleed_in_institution(self):
        value = (
            "Shen Yuan Honors College, Beihang University；"
            "the College of Computing and patches. While this processing strategy can capture abun-"
        )

        self.assertFalse(is_valid_institution_text(value))
        self.assertTrue(is_invalid_digest_institution(value))

    def test_accepts_common_affiliation_list(self):
        value = (
            "Faculty of Applied Sciences, Macao Polytechnic University；"
            "Pazhou Lab (Huangpu)；Macao Polytechnic University"
        )

        self.assertTrue(is_valid_institution_text(value))
        self.assertFalse(is_invalid_digest_institution(value))

    def test_builds_empty_digest_from_stats(self):
        digest = build_digest_with_llm(
            "20260524",
            [],
            stats={"candidate_count": 0, "llm_selected_count": 0},
        )

        self.assertIn("# 日报 20260524", digest)
        self.assertIn("最终纳入日报 0 篇", digest)
        self.assertIn("当日未检索到符合条件并纳入日报的论文", digest)


if __name__ == "__main__":
    unittest.main()
