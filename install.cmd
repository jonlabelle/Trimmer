set PYTHON=%~1
set PATH=%PYTHON%;%PYTHON%\Scripts;%PATH%

python install -r requirements.txt
