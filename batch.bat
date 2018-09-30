@echo off


for /f "tokens=*" %%a in (new.txt) do set varText=%varText%%%a

set varText=%varText%
python C:\xampp\htdocs\FINALS\neural_net.py %varText% %*
REM ECHO %varText%
break>c:\'C:\xampp\htdocs\FINALS'\demo.txt
pause