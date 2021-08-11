@echo off
setlocal

set PYTHON=%~1
if defined PYTHON set PATH=%PYTHON%;%PYTHON%\Scripts;%PATH%

set SCRIPTSDIR=%~dp0
pushd "%SCRIPTSDIR%" && pushd ..

echo. > Install pip requirements
pip3 install -r requirements.txt

popd && popd

echo.
echo. Finished.
endlocal
