@echo off

if [%1]==[] GOTO No1
if [%2]==[] GOTO No2

for /f %%i in ('git rev-parse --show-toplevel') do set root=%%i
cd %root%

cd .\results\animation\

if not exist .\%1\ mkdir %1

cd .\frames\
ti video -o ..\%1\%2.mp4
cd ..
rmdir .\frames\ /s /q
cd .\%1\
ti gif -i %2.mp4

goto End

:No1
  ECHO Missing parameter 'output directory name'
:No2
  ECHO Missing parameter 'filename'

:End
