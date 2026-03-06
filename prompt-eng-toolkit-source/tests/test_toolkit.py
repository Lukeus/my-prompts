import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import adapt_prompts  # noqa: E402
import generate_prompt_library  # noqa: E402
import scan_codebase  # noqa: E402


class PromptToolkitTests(unittest.TestCase):
    def test_build_replacements_handles_empty_frontend_lists(self):
        profile = {
            "project_name": "api-service",
            "languages": ["Python"],
            "frameworks": ["FastAPI"],
            "databases": [],
            "data_tools": [],
            "testing": {"frameworks": ["pytest"]},
            "infrastructure": {"ci_tool": "GitHub Actions"},
            "frontend": {"frameworks": [], "styling": []},
            "conventions": {"naming": "snake_case"},
            "architecture": "monolith",
        }

        replacements = adapt_prompts.build_replacements(profile)

        self.assertEqual(replacements["{{LANGUAGE}}"], "Python")
        self.assertEqual(replacements["{{FRAMEWORK}}"], "FastAPI")
        self.assertEqual(replacements["{{TEST_FRAMEWORK}}"], "pytest")
        self.assertEqual(replacements["{{FRONTEND_FRAMEWORK}}"], "{{FRONTEND_FRAMEWORK}}")
        self.assertEqual(replacements["{{STYLING}}"], "{{STYLING}}")

    def test_build_profile_detects_frontend_from_frameworks(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_path = Path(temp_dir)
            package_json = {
                "name": "web-app",
                "dependencies": {
                    "next": "15.0.0",
                    "react": "19.0.0",
                    "tailwindcss": "4.0.0",
                },
                "devDependencies": {
                    "vitest": "2.0.0",
                },
            }
            (repo_path / "package.json").write_text(json.dumps(package_json), encoding="utf-8")

            profile = scan_codebase.build_profile(repo_path)

            self.assertTrue(profile["frontend"]["detected"])
            self.assertIn("Next.js", profile["frameworks"])
            self.assertIn("React", profile["frontend"]["frameworks"])
            self.assertIn("Tailwind CSS", profile["frontend"]["styling"])
            self.assertIn("Vitest", profile["testing"]["frameworks"])

    def test_generate_prompt_library_writes_support_files_and_filters_stack_specific_prompts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_path = Path(temp_dir) / "sample-repo"
            output_dir = repo_path / ".claude" / "prompts"
            (repo_path / ".github" / "workflows").mkdir(parents=True)
            (repo_path / ".github" / "workflows" / "ci.yml").write_text("name: ci\n", encoding="utf-8")

            package_json = {
                "name": "sample-repo",
                "dependencies": {
                    "next": "15.0.0",
                    "react": "19.0.0",
                    "tailwindcss": "4.0.0",
                },
                "devDependencies": {
                    "jest": "30.0.0",
                    "@testing-library/react": "16.0.0",
                },
            }
            repo_path.mkdir(parents=True, exist_ok=True)
            (repo_path / "package.json").write_text(json.dumps(package_json), encoding="utf-8")

            result = generate_prompt_library.generate_prompt_library(
                repo_path=repo_path,
                output_dir=output_dir,
                tool="claude",
            )

            self.assertEqual(result["tool"], "claude")
            self.assertTrue((output_dir / "README.md").exists())
            self.assertTrue((output_dir / "INDEX.md").exists())
            self.assertTrue((output_dir / "_project-profile.yml").exists())
            self.assertTrue((output_dir / "software-development" / "templates" / "code-review.md").exists())
            self.assertTrue((output_dir / "ui-development" / "stack-specific" / "react.md").exists())
            self.assertTrue((output_dir / "codebase-research" / "exploration" / "repo-onboarding.md").exists())
            self.assertFalse((output_dir / "data-engineering" / "stack-specific" / "dbt.md").exists())

            readme = (output_dir / "README.md").read_text(encoding="utf-8")
            index_text = (output_dir / "INDEX.md").read_text(encoding="utf-8")

            self.assertIn("sample-repo", readme)
            self.assertIn(".claude/prompts", readme)
            self.assertIn("Claude Code", readme)
            self.assertIn("UI Development", index_text)


if __name__ == "__main__":
    unittest.main()
