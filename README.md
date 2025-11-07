# CP6-Dynamic-programming

# Problema da Mochila 0/1 — Estudo de Caso: Recursão, Memoização e Programação Dinâmica

## Membros do Grupo
- Miguel Marques Lourenço de Souza - RM555426
- Lorenzzo Vebdruscolo Dias - RM558305
- Gabriel Martins Vanucci - RM556883
- Pedro Henrique Ferronato - RM554757

---

# Introdução
O Problema da Mochila 0/1 é um clássico de otimização combinatória. Dada uma lista de itens, cada um com peso e valor, deseja-se maximizar o valor total transportado em uma mochila com capacidade limitada, escolhendo se cada item é incluído (1) ou não (0).

---

# Natureza do Problema
O problema é **NP-Completo**, pois exige verificar múltiplas combinações possíveis de itens para encontrar a solução ótima — uma característica típica de problemas de otimização.

---

# Definição de Programação Dinâmica
A **Programação Dinâmica (PD)** é uma técnica que resolve problemas complexos dividindo-os em subproblemas menores, resolvendo cada um uma única vez e armazenando seus resultados.

# Subestrutura Ótima
A solução ótima de um problema depende das soluções ótimas de seus subproblemas.

# Subproblemas Sobrepostos
Os mesmos subproblemas aparecem repetidamente durante a execução — a **memoização** e a **PD** evitam recomputação.

---

# Abordagens Implementadas

| Abordagem | Tipo | Complexidade de Tempo | Observações |
|------------|------|----------------------|--------------|
| Estratégia Gulosa | Iterativa | O(n log n) | Não garante solução ótima |
| Recursiva Simples | Top-Down | O(2^n) | Explora todas as combinações |
| Recursiva com Memoização | Top-Down | O(n * W) | Evita recomputação |
| Programação Dinâmica | Bottom-Up | O(n * W) | Solução ótima e eficiente |

---

# Conclusão
A **Programação Dinâmica (Bottom-Up)** se destaca como a abordagem mais eficiente e robusta, garantindo o valor ótimo com menor tempo computacional para grandes instâncias do problema.  
Ela ilustra perfeitamente a força da PD em lidar com **subestrutura ótima** e **subproblemas sobrepostos**.

---

# Reflexão
Dominar essas técnicas é essencial para resolver problemas de otimização em áreas como logística, finanças, IA e ciência de dados — onde decisões ótimas dependem de múltiplas restrições combinatórias.

---
