# Valida formato do CPF
def validar_formato_cpf(cpf):
# XXX.XXX.XXX-XX
    if cpf[3] != '.':
        return False
    elif cpf[7] != '.':
        return False
    elif cpf[11] != '-':
        return False
    return True

def validar_cpf(cpf):
    if not validar_formato_cpf(cpf):
        cpf_limpo = cpf.replace('.','').replace('-','')
        contador = 10
        soma = 0
        for caractere in cpf_limpo:
            if contador > 1:
                soma += int(caractere) * contador
        contador = 10
        digitol = (soma * 10) % 11
        if digitol != int(cpf_limpo[9]):
            return False

