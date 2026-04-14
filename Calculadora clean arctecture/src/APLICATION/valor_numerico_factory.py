from re import sub
from ..DOMINIO.VALUE_OBJECTS.valor_numerico import ValorNumerico

def valor_numerico_factory(entrada: float | int | str, forcar_normalizacao: bool = False)-> ValorNumerico:
        """
        Recebe uma entrada suja e adapta-a para poder virar um ValorNumerico.

        Se 'forcar_normalizacao' for 'True', pode modificar suavemente a
        entrada, tornando, por exemplo, '0.4' em '0'; do contrario, retornará
        um erro ao se deparar com essa situação.
        """
        if not type(entrada, (float, int, str)):
            raise TypeError(f"entrada '{entrada}' não poderia ser do tipo '{type(entrada)}'")
            
        if type(entrada, int):
            return float(entrada)
        
        elif type(entrada, str):
            entrada = sub(r"[^.,\d]", "", entrada.strip())
            if entrada == "": return valor_numerico_factory(0.0)

            entrada = entrada.replace(",", ".")
            if entrada.count(".") > 1:
                if forcar_normalizacao:
                    t_ultimo_ponto = len(entrada)-1 # -1 para ficar em formato index (0-9)
                    while True:
                        if entrada.find(".", t_ultimo_ponto) == -1:
                            t_ultimo_ponto -= 1
                            continue
                        else: 
                            t_num_pontos_invalidos = entrada.find(".", 0, t_ultimo_ponto-1) # -1 para ficar no formato 1-9
                            entrada = entrada.replace(".", "", t_num_pontos_invalidos)
                            break
                    return float(entrada)
                else:
                    raise ValueError(f"O valor passada tinha muito '.'; para garantir a autenticidade do valor, não será feita conversão. Ajuste o valor '{entrada}'!")
            return float(entrada)
        else: return entrada

def valor_numerico_str_normalizer(entrada: str):
    """
    Normaliza uma entrada str problemática de ValorNumerico em str convertível.
    """
    raise NotImplementedError("Função não implementada ainda! Apenas deixando" \
                              "esboço para necessidade futura. Talvez vá para a cama de Adapter no futuro!")

    if not isinstance(entrada, str): raise TypeError

    entrada = entrada.strip()

    # USAR GLOB PARA RETIRAR NÃO NUMERAIS QUE NÃO SEJAM "." OU "," 


# TODO autotest: entrada str 1.1.11
# TODO autotest: entrada str 1,1.11
# TODO autotest: entrada str 11,,.11
# TODO autotest: entrada str 11,11
# TODO autotest: entrada str ''
# TODO autotest: entrada str ,