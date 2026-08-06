from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@patch("app.main.service.create_json")
def test_create_json_endpoint(mock_create_json):
    mock_create_json.return_value = {"filename": "demo.json"}

    response = client.post(
        "/json",
        json={"job_description": "Python developer role", "filename": "demo"},
    )

    assert response.status_code == 200
    assert response.json() == {"status": "success", "output": {"filename": "demo.json"}}
    mock_create_json.assert_called_once_with(
        job_description="Python developer role",
        filename="demo",
        base_json_dir=None,
    )


@patch("app.main.service.create_json_without_agent")
def test_create_json_without_agent_endpoint(mock_create_json_without_agent):
    mock_create_json_without_agent.return_value = {"filename": "demo.json"}

    response = client.post(
        "/json/no-agent",
        json={"job_description": "Python developer role", "filename": "demo"},
    )

    assert response.status_code == 200
    assert response.json() == {"status": "success", "output": {"filename": "demo.json"}}
    mock_create_json_without_agent.assert_called_once_with(
        job_description="Python developer role",
        filename="demo",
        base_json_dir=None,
    )


@patch("app.main.service.create_english_json")
def test_create_english_json_endpoint(mock_create_english_json):
    mock_create_english_json.return_value = {"filename": "demo.json"}

    response = client.post(
        "/json/english",
        json={"job_description": "Python developer role", "filename": "demo"},
    )

    assert response.status_code == 200
    assert response.json() == {"status": "success", "output": {"filename": "demo.json"}}
    mock_create_english_json.assert_called_once_with(
        job_description="Python developer role",
        filename="demo",
        base_json_dir=None,
    )


@patch("app.main.service.translate_json")
def test_translate_json_endpoint(mock_translate_json):
    mock_translate_json.return_value = {"filename": "demo.json"}

    response = client.post(
        "/json/translate",
        json={"job_description": "Python developer role", "filename": "demo"},
    )

    assert response.status_code == 200
    assert response.json() == {"status": "success", "output": {"filename": "demo.json"}}
    mock_translate_json.assert_called_once_with(
        job_description="Python developer role",
        filename="demo",
        base_json_dir=None,
    )


@patch("app.main.service.create_pdf")
def test_create_pdf_endpoint(mock_create_pdf):
    mock_create_pdf.return_value = {"pdf_name": "demo.pdf"}

    response = client.post(
        "/pdf",
        json={"job_description": "Python developer role", "pdf_name": "demo"},
    )

    assert response.status_code == 200
    assert response.json() == {"status": "success", "output": {"pdf_name": "demo.pdf"}}
    mock_create_pdf.assert_called_once_with(
        job_description="Python developer role",
        output_dir=None,
        image_path=None,
        pdf_name="demo",
        job_json_path=None,
    )


@patch("app.main.service.create_english_pdf")
def test_create_english_pdf_endpoint(mock_create_english_pdf):
    mock_create_english_pdf.return_value = {"pdf_name": "demo.pdf"}

    response = client.post(
        "/pdf/english",
        json={"job_description": "Python developer role", "pdf_name": "demo"},
    )

    assert response.status_code == 200
    assert response.json() == {"status": "success", "output": {"pdf_name": "demo.pdf"}}
    mock_create_english_pdf.assert_called_once_with(
        job_description="Python developer role",
        output_dir=None,
        image_path=None,
        pdf_name="demo",
        job_json_path=None,
    )


@patch("app.main.service.create_cover_letter_pdf")
def test_create_cover_letter_pdf_endpoint(mock_create_cover_letter_pdf):
    mock_create_cover_letter_pdf.return_value = {"pdf_name": "demo.pdf"}

    response = client.post(
        "/pdf/cover-letter",
        json={"job_description": "Python developer role", "pdf_name": "demo"},
    )

    assert response.status_code == 200
    assert response.json() == {"status": "success", "output": {"pdf_name": "demo.pdf"}}
    mock_create_cover_letter_pdf.assert_called_once_with(
        job_description="Python developer role",
        output_dir=None,
        pdf_name="demo",
        job_json_path=None,
    )
