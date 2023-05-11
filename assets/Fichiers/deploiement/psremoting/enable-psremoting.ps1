$computer = Read-Host "nom de la machine cible"

C:\deploiement\psremoting\PsExec.exe \\$computer -s powershell.exe enable-psremoting -force