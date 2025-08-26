@echo off

set CurrDir=%~dp0%

for /F "tokens=2* delims= " %%f IN ('reg query HKCU\Environment /v PATH ^| findstr /i path') do set OLD_SYSTEM_PATH=%%g
echo "User path is now: %NandToolPath%;%OLD_SYSTEM_PATH%"
setx PATH "%CurrDir%;%OLD_SYSTEM_PATH%"
