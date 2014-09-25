set WORKSPACE=%1

echo START TEST SUITE 
cd %WORKSPACE%
D:  
echo copy file
cmd /c copy /y \\10.10.3.247\ShareFile\ShareTest\TopAPI\workspace\TOP_API\db.xml %WORKSPACE%
cmd /c copy /y %WORKSPACE%\template.html %WORKSPACE%\report.html
echo generate report
cmd /c %WORKSPACE%\GenReport.py %WORKSPACE%\db.xml %WORKSPACE%\report.html

ping -n 10 127.1 >nul 2>nul

