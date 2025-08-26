@echo off

rem set CurrDir=%~dp0%
set JavaMatlabDir=C:\Program Files\MATLAB\R2022\sys\java\jre\win64\jre\bin

for /F "tokens=2* delims= " %%f IN ('reg query HKCU\Environment /v PATH ^| findstr /i path') do set OLD_SYSTEM_PATH=%%g
rem echo "User path is now: %NandToolPath%;%OLD_SYSTEM_PATH%"
rem setx PATH "%JavaMatlabDir%;%CurrDir%;%OLD_SYSTEM_PATH%"
setx PATH "%JavaMatlabDir%;%OLD_SYSTEM_PATH%"
