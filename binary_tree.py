import macros

class Nodulo:
    
    def __init__(self, value):
        self.Value = value
        self.Ponteiro_esquerda = None
        self.Ponteiro_direita = None
        self.Dano_ataque = None
        self.Dano_defesa = None
        self.Eh_magico = None
        self.Nome = ""
        self.Descricao = ""

    #JMM
    def Posicao_ponteiro_esquerda(self):
        if self.Ponteiro_esquerda is None:
            return "Não há nó à esquerda"
        else:
            return self.Ponteiro_esquerda.Value

    
    def Calcular_posicao_ponteiro_esquerda(posicao_x_pai, posicao_y_pai, nodulo_altura):
        """_summary_

        Args:
            posicao_x_pai (_type_): _description_
            posicao_y_pai (_type_): _description_
            nodulo_altura (_type_): _description_

        Returns:
            _type_: _description_
        """
    
        posicao_x_nodulo_esquerda = posicao_x_pai - ((macros.WINDOW_WIDTH - macros.X_PADDING) / pow(2, nodulo_altura))
        posicao_y_nodulo_esquerda = posicao_y_pai + macros.NODE_RADIUS * 4
        return (posicao_x_nodulo_esquerda, posicao_y_nodulo_esquerda)
    
    #JMM
    def Posicao_ponteiro_direita(self):
        if self.Ponteiro_direita is None:
            return "Não há nó à direita"
        else:
            return self.Ponteiro_direita.Value

    def Calcular_posicao_ponteiro_direita(posicao_x_pai, posicao_y_pai, nodulo_altura):
        """_summary_

        Args:
            posicao_x_pai (_type_): _description_
            posicao_y_pai (_type_): _description_
            nodulo_altura (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        posicao_x_nodulo_direita = posicao_x_pai + ((macros.WINDOW_WIDTH - macros.X_PADDING) / pow(2, nodulo_altura)) / 2
        posicao_y_nodulo_direita = posicao_y_pai + macros.NODE_RADIUS * 4
        return (posicao_x_nodulo_direita, posicao_y_nodulo_direita)


    def Inserir_no(self, value):
        if self.Value is None:  
            self.Value = value
        else:
            if value < self.Value:
                if self.Ponteiro_esquerda is None:
                    self.Ponteiro_esquerda = Nodulo(value)
                else:
                    self.Ponteiro_esquerda.Inserir_no(value)
            elif value > self.Value:
                if self.Ponteiro_direita is None:
                    self.Ponteiro_direita = Nodulo(value)
                else:
                    self.Ponteiro_direita.Inserir_no(value)
# Percorrer a árvore
    def Percorrer_infixo(self):
        result = [] #cria uma lista vazia
        # Percorre a árvore à esquerda
        if self.Ponteiro_esquerda:
            #extend adiciona os itens de uma lista ao final de outra lista
            result.extend(self.Ponteiro_esquerda.Percorrer_infixo())
        result.append(self.Value) #append adiciona um item ao final da lista
        if self.Ponteiro_direita:
            # Percorre a árvore à direita
            result.extend(self.Ponteiro_direita.Percorrer_infixo())#
        return result #retorna a lista result

    def Percorrer_posfixo(self):
        result = []#cria uma lista vazia
        if self.Ponteiro_esquerda:#
            result.extend(self.Ponteiro_esquerda.Percorrer_posfixo())
        if self.Ponteiro_direita:
            result.extend(self.Ponteiro_direita.Percorrer_posfixo())
        result.append(self.Value)
        return result

    def Percorrer_prefixo(self):
        result = [self.Value]
        if self.Ponteiro_esquerda:
            result.extend(self.Ponteiro_esquerda.Percorrer_prefixo())
        if self.Ponteiro_direita:
            result.extend(self.Ponteiro_direita.Percorrer_prefixo())
        return result


