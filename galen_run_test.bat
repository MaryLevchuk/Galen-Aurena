For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-2 delims=/:" %%a in ("%TIME%") do (set mytime=%%a%%b)
galen test "/Projects/GalenTests/Galen-Aurena/aurena-frontpage.test" --htmlreport ./GalenReports/%mydate%_%mytime%