SYSTEM_NAME = str(input("Digite o nome do código: "))
MAX_ATTEMPTS = int(input("Digite o número máximo de tentativas: "))
ERROR_THRESHOLD = float(input("Digite o número de taxa limite de erro em porcentagem: "))
IS_ACTIVE = True

print(f"Sistema: {SYSTEM_NAME} | Tipo {type(SYSTEM_NAME)}")
print(f"Tentativas: {MAX_ATTEMPTS} | Tipo: {type(MAX_ATTEMPTS)}")
print(f"Limite erro: {ERROR_THRESHOLD} | Tipo: {type(ERROR_THRESHOLD)}")
print(f"Ativo: {IS_ACTIVE} | Tipo: {type(IS_ACTIVE)}")