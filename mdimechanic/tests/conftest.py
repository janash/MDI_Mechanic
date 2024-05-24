"""
Fixtures for the mdimechanic tests.
"""

import pytest

from unittest.mock import MagicMock, patch

@pytest.fixture(autouse=True)
def mock_subprocess_run():
    with patch('subprocess.run') as mock_run:
        mock_run.side_effect = [
            # Simulate docker compose version success
            MagicMock(returncode=0),
            # Simulate docker-compose version success if needed
            MagicMock(returncode=0)
        ]
        yield mock_run

@pytest.fixture
def setup_temp_files(tmp_path):
    """Fixture to set up temporary .gitconfig and .ssh directories"""
    temp_gitconfig = tmp_path / '.gitconfig'
    temp_ssh = tmp_path / '.ssh'
    temp_ssh.mkdir()
    temp_gitconfig.write_text('')

    return temp_gitconfig, temp_ssh

@pytest.fixture
def mock_get_mdimechanic_yaml(mocker):
    """Fixture to mock get_mdimechanic_yaml function"""
    return mocker.patch('mdimechanic.utils.utils.get_mdimechanic_yaml', return_value={'docker': {'image_name': 'test_image'}})

@pytest.fixture(autouse=True)
def mock_determine_compose_command(mocker):
    """Fixture to mock get_compose_command function"""
    return mocker.patch('mdimechanic.utils.determine_compose.determine_compose', return_value='docker compose')

