@echo off

:: Verifique se pelo menos um nome de arquivo foi fornecido como argumento
if "%~1"=="" (
    echo Por favor, forneça pelo menos um nome de arquivo como argumento.
    exit /b 1
)

:: Itera sobre os argumentos de arquivo e executa as ferramentas de formatação em cada um
:loop
if "%~1"=="" goto end
set arquivo=%~1

echo Executando isort no arquivo %arquivo%...
isort %arquivo%
echo Isort concluido.

echo Executando ruff no arquivo %arquivo%...
ruff %arquivo%
echo Ruff concluido.

echo Executando black no arquivo %arquivo%...
black %arquivo%
echo Black concluido.

:: Vá para o próximo argumento de arquivo
shift
goto loop

:end
