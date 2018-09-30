@echo off


for /f "tokens=*" %%a in (new.txt) do set varText=%varText%%%a

set varText=%varText%
python C:\xampp\htdocs\FINAL\knn_predict.py %varText% %*
REM ECHO %varText%
break>c:\'C:\xampp\htdocs\FINAL'\demo.txt
pause