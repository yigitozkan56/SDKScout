import os
import tempfile

from fastapi.testclient import TestClient

from app import SDKScoutDB, parse_manifest_dependencies, web_app


def test_parse_requirements_and_package_json():
    req_txt = "fastapi>=0.110.0\npydantic==2.6.0\n"
    deps_py = parse_manifest_dependencies("requirements.txt", req_txt)
    assert len(deps_py) == 2
    assert deps_py[0]["registry"] == "PyPI"
    assert deps_py[0]["category"] == "Web API Framework"

    pkg_json = '{"dependencies": {"stripe": "^14.0.0", "tailwindcss": "^3.4.0"}}'
    deps_npm = parse_manifest_dependencies("package.json", pkg_json)
    assert len(deps_npm) == 2
    assert deps_npm[0]["registry"] == "npm"


def test_parse_pubspec_and_api():
    pubspec = "name: app\ndependencies:\n  riverpod: ^2.5.0\n  dio: ^5.4.0\n"
    deps_dart = parse_manifest_dependencies("pubspec.yaml", pubspec)
    assert len(deps_dart) == 2
    assert deps_dart[0]["registry"] == "pub.dev"

    with tempfile.TemporaryDirectory() as tmpdir:
        db = SDKScoutDB(db_path=os.path.join(tmpdir, "sdk.db"))
        assert len(db.list_packages()) >= 4

    client = TestClient(web_app)
    resp = client.get("/api/packages")
    assert resp.status_code == 200
    assert resp.json()["count"] >= 4
