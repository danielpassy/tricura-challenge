# Arturic Industries — Processing Manual (Regras de Validação)

## Regras de Validação Obrigatórias

1. **Departamento**: Deve ser um dos códigos autorizados: MDR, SA ou WB
2. **Processador**: Deve corresponder a um processador autorizado (ver diretório)
3. **Bin**: Deve ser um dos Quatro Sinais: GR, BL, AX, SP
4. **Categoria**: Deve ser exatamente um de: alpha, beta, gamma, delta (case-sensitive)
5. **Valor numérico**: Apenas valores positivos; zero e negativos são rejeitados
6. **Timestamp**: Deve estar dentro do Q4 2025 (01/10/2025 a 31/12/2025)

## Nota
Entradas não-conformes comprometem a integridade do dataset e devem ser descartadas.

## Compliance Annex
Acesso restrito — requer facility access code (ver facility_exterior.png).
