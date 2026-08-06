from unittest.mock import MagicMock

from Agents.resumePackageAgent import ResumePackageInput, ResumeTailorAgent


def test_resume_package_input_defaults_missing_fields():
    payload = {
        "keywords": ["python", "azure"],
        "rationale": ["matched keywords"],
    }

    result = ResumePackageInput.model_validate(payload)

    assert result.about_me == ""
    assert result.keywords == ["python", "azure"]
    assert result.Job_1_suggested == []
    assert result.Job_2_suggested == []
    assert result.cover_letter_first == ""
    assert result.cover_letter_last == ""
    assert result.rationale == ["matched keywords"]


def test_run_uses_tool_observation_when_agent_output_is_missing():
    agent = ResumeTailorAgent.__new__(ResumeTailorAgent)
    agent.agent_executor = MagicMock()
    agent.agent_executor.invoke.return_value = {
        "output": "",
        "intermediate_steps": [
            {
                "action": MagicMock(tool="ResumePackageGenerator"),
                "observation": {"about_me": "summary", "keywords": ["python"]},
            }
        ],
    }
    agent.build_input = MagicMock(return_value="input")

    result = agent.run(
        job_description="job",
        about_me="about",
        job1=["one"],
        job2=["two"],
    )

    assert result == {"about_me": "summary", "keywords": ["python"]}
