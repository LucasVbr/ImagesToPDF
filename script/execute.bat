:: execute.bat, 25/06/2021
:: no copyright
:: author: LucasVBR

@ECHO OFF

:: Execute script
if exist ./ToPDF.py (
	:: Create folder if it do not exist
	if not exist out mkdir out
	
	python ./ToPDF.py
) else (
	echo ToPDF.py doesn't exist
	pause
)