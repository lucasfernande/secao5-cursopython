import subprocess

# windows - ping

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,  # a saída do comando irá diretamente para o stdout
    text=True  # coloca a saida em formato de texto, e não em bytes (padrão)
)

print(proc.stderr)  # caso aconteça um erro
print(proc.stdout)  # saida do comando
print(proc.returncode)  # codigo de retorno (0 = nenhum erro)
print(proc.args)
