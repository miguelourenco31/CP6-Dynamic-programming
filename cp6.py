def knapsack(pesos, valores, W):
    """
    Estratégia Gulosa (Iterativa) para o Problema da Mochila 0/1.

    A função seleciona itens com base na razão valor/peso, tentando maximizar
    o valor total sem ultrapassar a capacidade. Não garante solução ótima.

    Parâmetros:
    ----------
    pesos : list[int]
        Lista de pesos dos itens disponíveis.
    valores : list[int]
        Lista de valores correspondentes aos itens.
    W : int
        Capacidade máxima da mochila.

    Retorno:
    -------
    int
        Valor total estimado (não necessariamente o ótimo),
        respeitando a capacidade W.
    """
    n = len(pesos)
    # Cria uma lista com (razão, peso, valor)
    itens = sorted(
        [(valores[i] / pesos[i], pesos[i], valores[i]) for i in range(n)],
        key=lambda x: x[0],
        reverse=True
    )

    total_valor = 0
    total_peso = 0
    itens_escolhidos = []

    for ratio, peso, valor in itens:
        if total_peso + peso <= W:
            total_peso += peso
            total_valor += valor
            itens_escolhidos.append((peso, valor, ratio))

    print("Itens escolhidos (peso, valor, razão):", itens_escolhidos)
    print("Peso total:", total_peso, " | Valor total:", total_valor)
    return total_valor

# ===============================================
# 2. Função Recursiva Pura (sem Memoização)
# ===============================================

def knapsackRec(pesos, valores, W, n=None):
    """
    Abordagem Recursiva Pura (sem memoização).

    A função tenta todas as combinações possíveis de itens (inclusão ou exclusão)
    para encontrar o valor máximo possível sem ultrapassar a capacidade da mochila.

    Parâmetros:
    ----------
    pesos : list[int]
        Lista de pesos dos itens.
    valores : list[int]
        Lista de valores dos itens.
    W : int
        Capacidade máxima da mochila.
    n : int
        Quantidade de itens (usado internamente na recursão).

    Retorno:
    -------
    int
        Valor máximo possível que cabe na mochila.

    Complexidade:
    -------------
    - Tempo: O(2^n)
    - Espaço: O(n) (profundidade da recursão)
    - Melhor caso (Ω): Ω(n)
    - Pior caso (O): O(2^n)
    - Médio caso (Θ): Θ(2^n)
    """
    if n is None:
        n = len(pesos)
    if n == 0 or W == 0:
        return 0

    if pesos[n-1] > W:
        return knapsackRec(pesos, valores, W, n-1)
    else:
        incluir = valores[n-1] + knapsackRec(pesos, valores, W - pesos[n-1], n-1)
        excluir = knapsackRec(pesos, valores, W, n-1)
        return max(incluir, excluir)

# ===============================================
# 3. Função Recursiva com Memoização (Top-Down)
# ===============================================

def knapsackMemo(pesos, valores, W, n=None, memo=None):
    """
    Abordagem Recursiva com Memoização (Top-Down).

    Esta versão armazena resultados intermediários de subproblemas
    já resolvidos para evitar recomputações desnecessárias.

    Parâmetros:
    ----------
    pesos : list[int]
        Lista de pesos dos itens.
    valores : list[int]
        Lista de valores dos itens.
    W : int
        Capacidade máxima da mochila.
    n : int
        Quantidade de itens.
    memo : dict
        Dicionário usado para armazenar resultados intermediários.

    Retorno:
    -------
    int
        Valor máximo possível que cabe na mochila.

    Complexidade:
    -------------
    - Tempo: O(n * W)
    - Espaço: O(n * W)
    - Melhor caso (Ω): Ω(n)
    - Pior caso (O): O(n * W)
    - Médio caso (Θ): Θ(n * W)
    """
    if n is None:
        n = len(pesos)
    if memo is None:
        memo = {}

    if (n, W) in memo:
        return memo[(n, W)]

    if n == 0 or W == 0:
        result = 0
    elif pesos[n-1] > W:
        result = knapsackMemo(pesos, valores, W, n-1, memo)
    else:
        incluir = valores[n-1] + knapsackMemo(pesos, valores, W - pesos[n-1], n-1, memo)
        excluir = knapsackMemo(pesos, valores, W, n-1, memo)
        result = max(incluir, excluir)

    memo[(n, W)] = result
    return result

# ===============================================
# 4. Programação Dinâmica (Bottom-Up)
# ===============================================

def knapsackPD(pesos, valores, W):
    """
    Solução com Programação Dinâmica (Bottom-Up).

    Constrói uma tabela dp onde dp[i][w] representa o valor máximo
    que pode ser obtido considerando os primeiros i itens e capacidade w.

    Parâmetros:
    ----------
    pesos : list[int]
        Lista de pesos dos itens.
    valores : list[int]
        Lista de valores dos itens.
    W : int
        Capacidade máxima da mochila.

    Retorno:
    -------
    int
        Valor máximo possível (ótimo global) que cabe na mochila.

    Complexidade:
    -------------
    - Tempo: O(n * W)
    - Espaço: O(n * W)
    - Melhor caso (Ω): Ω(n)
    - Pior caso (O): O(n * W)
    - Médio caso (Θ): Θ(n * W)
    """
    n = len(pesos)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if pesos[i-1] <= w:
                dp[i][w] = max(
                    valores[i-1] + dp[i-1][w - pesos[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

pesos = [2, 3, 4, 1]
valores = [10, 12, 20, 3]
capacidade_max = 6

print("Guloso:", knapsack(pesos, valores, capacidade_max))
print("Recursivo:", knapsackRec(pesos, valores, capacidade_max))
print("Memoização:", knapsackMemo(pesos, valores, capacidade_max))
print("PD (Bottom-Up):", knapsackPD(pesos, valores, capacidade_max))



