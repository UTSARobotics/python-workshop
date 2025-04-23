# python-workshop

Requires raylib and numpy

# Setup

[Extra Instructions for VENV](https://docs.python.org/3/library/venv.html)

```sh
python -m venv .venv

source .venv/bin/activate

pip install raylib numpy

python maze_path.py
```

| Platform | Shell   | Command to Activate Virtual Environment  |
| ------- | ---------- | -------------------------------------- |
| POSIX   | bash/zsh   | `source <venv>/bin/activate`           |
| POSIX   | fish       | `source <venv>/bin/activate.fish`      |
| POSIX   | csh/tcsh   | `source <venv>/bin/activate.csh`       |
| POSIX   | powershell | `<venv>/bin/Activate.ps1`              |
| Windows | cmd.exe    | `<venv>\Scripts\activate.bat`          |
| Windows | powershell | `<venv>\Scripts\Activate.ps1`          |

>Note
>
>On Microsoft Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the user. You can do this by issuing the following PowerShell command:
>
>`PS C:\> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
