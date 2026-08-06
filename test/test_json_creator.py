import json
import os
import sys
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

os.environ.setdefault("CHAT_GPT_API", "test-key")
os.environ.setdefault("AZURE_OPENAI_ENDPOINT", "https://example.openai.azure.com")
os.environ.setdefault("AZURE_OPENAI_API_KEY", "test-key")
os.environ.setdefault("AZURE_OPENAI_API_VERSION", "2024-02-01")

from services.JsonCreator import JsonCreator


@pytest.fixture
def json_creator(tmp_path):
    class DummyChatGPTHandler:
        def __init__(self, model_name="gpt-5-nano"):
            self.model_name = model_name
            self.client = object()
            self.llm = object()

        def chat(self, messages):
            return "{}"

    with patch("services.JsonCreator.ChatGPTHandler", DummyChatGPTHandler):
        return JsonCreator(base_json_dir=str(tmp_path), job_discription="Software engineer role")


def test_build_agent_prompt_contains_expected_sections(json_creator):
    prompt = json_creator._build_agent_prompt(
        "Python developer role",
        ["Developed Python automation"],
        ["Built test dashboards"],
        "Experienced engineer",
    )

    assert "=== INPUT: Job description ===" in prompt
    assert "Python developer role" in prompt
    assert "=== INPUT: Job_1_details_FullTime" in prompt
    assert "Developed Python automation" in prompt
    assert "=== INPUT: Job_2_details_Workstudent" in prompt
    assert "Built test dashboards" in prompt
    assert "Return ONLY the JSON object" in prompt


def test_save_result_to_json_writes_combined_payload(json_creator, tmp_path):
    json_creator.save_result_to_json(
        '{"about_me": "English summary"}',
        '{"about_me": "German summary"}',
        "sample",
    )

    output_path = tmp_path / "sample.json"
    assert output_path.exists()

    content = json.loads(output_path.read_text(encoding="utf-8"))
    assert content["result_english"]["about_me"] == "English summary"
    assert content["result_german"]["about_me"] == "German summary"


def test_save_english_result_to_json_writes_expected_structure(json_creator, tmp_path):
    payload = {"about_me": "Tailored summary", "keywords": ["python", "testing"]}

    json_creator.save_english_result_to_json(payload, "english-output")

    output_path = tmp_path / "english-output.json"
    assert output_path.exists()

    content = json.loads(output_path.read_text(encoding="utf-8"))
    assert content == {"result_english": payload}


def test_update_json_with_translated_result_adds_german_and_job_description(json_creator, tmp_path):
    existing_path = tmp_path / "existing.json"
    existing_path.write_text(
        json.dumps({"result_english": {"about_me": "English summary"}}),
        encoding="utf-8",
    )

    json_creator.translate_the_result_in_german = Mock(return_value='{"about_me": "German summary"}')

    json_creator.update_json_with_translated_result("existing")

    content = json.loads(existing_path.read_text(encoding="utf-8"))
    assert content["result_german"]["about_me"] == "German summary"
    assert content["job_description"] == "Software engineer role"
