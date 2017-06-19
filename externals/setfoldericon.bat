@ECHO OFF
SET currentPath=%~fs1
FOR /f %%i IN ("%currentPath%\*.ico") DO SET iconFile=%%~nxi
ATTRIB -R "%currentPath%"
ATTRIB -H -R "%currentPath%\%iconFile%"  
ATTRIB -H -R "%currentPath%\Desktop.ini"  
ECHO [.ShellClassInfo] > "%currentPath%\Desktop.ini"  
ECHO IconFile=%iconFile% >> "%currentPath%\Desktop.ini"  
ECHO IconIndex=0 >> "%currentPath%\Desktop.ini"  
ATTRIB +H +R "%currentPath%\%iconFile%"
ATTRIB +H +R "%currentPath%\Desktop.ini"  
ATTRIB +R "%currentPath%"  