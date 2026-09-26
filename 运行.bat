@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo ========  csg plan  v0.0.1  ========
echo.
python run.py parts.csv
if errorlevel 1 (
  py run.py parts.csv
)
echo.
echo ====================================
echo   运行结束。按任意键关闭这个窗口。
pause >nul
