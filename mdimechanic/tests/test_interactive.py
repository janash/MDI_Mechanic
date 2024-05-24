

from unittest.mock import patch
from mdimechanic.cmd_interactive import start


def test_start_linux_gitconfig_exists(setup_temp_files, tmp_path, mocker, mock_get_mdimechanic_yaml, mock_determine_compose_command):
    temp_gitconfig, temp_ssh = setup_temp_files

    # Patch os.path.expanduser to use tmp_path
    mocker.patch('os.path.expanduser', return_value=str(tmp_path))

    # Mock os.system to capture the command
    mock_os_system = mocker.patch('os.system')

    start('test_image', str(tmp_path))

    # Verify that os.system was called with the correct command
    assert mock_os_system.called
    run_command = mock_os_system.call_args[0][0]
    assert f"{temp_gitconfig}:/root/.gitconfig" in run_command
    assert f"{temp_ssh}:/root/.ssh" in run_command

def test_start_windows_gitconfig_exists(tmp_path, mocker, mock_get_mdimechanic_yaml, mock_determine_compose_command):
    temp_userprofile = tmp_path / 'TestUserProfile'
    temp_userprofile.mkdir()
    temp_gitconfig = temp_userprofile / '.gitconfig'
    temp_ssh = temp_userprofile / '.ssh'
    temp_ssh.mkdir()
    temp_gitconfig.write_text('')

    with patch.dict('os.environ', {'USERPROFILE': str(temp_userprofile)}):
        # Patch os.path.expanduser to return a different path
        mocker.patch('os.path.expanduser', return_value=str(tmp_path / 'SomeOtherPath'))

        # Mock os.system to capture the command
        mock_os_system = mocker.patch('os.system')

        start('test_image', str(tmp_path / 'SomeOtherPath'))

        # Verify that os.system was called with the correct command
        assert mock_os_system.called
        run_command = mock_os_system.call_args[0][0]
        assert f"{temp_gitconfig}:/root/.gitconfig" in run_command
        assert f"{temp_ssh}:/root/.ssh" in run_command

def test_start_no_gitconfig(setup_temp_files, tmp_path, mocker, mock_get_mdimechanic_yaml, mock_determine_compose_command):
    _, temp_ssh = setup_temp_files

    # Patch os.path.expanduser to use tmp_path
    mocker.patch('os.path.expanduser', return_value=str(tmp_path))

    # Remove .gitconfig to simulate its absence
    (tmp_path / '.gitconfig').unlink()

    # Mock os.system to capture the command
    mock_os_system = mocker.patch('os.system')

    start('test_image', str(tmp_path))

    # Verify that os.system was called with the correct command
    assert mock_os_system.called
    run_command = mock_os_system.call_args[0][0]
    assert "/root/.gitconfig" not in run_command
    assert f"{temp_ssh}:/root/.ssh" in run_command
