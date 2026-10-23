# Sistema de triagem e fila clínica

## Objetivo

Prototipar o fluxo de atendimento: cadastro → senha → triagem → atendimento médico → finalização.

## Fluxo proposto

1. **Cadastro:** registrar os dados mínimos necessários e emitir uma senha.
2. **Triagem:** sinais vitais, sintomas, observações e classificação inicial.
3. **Atendimento médico:** visualizar dados da triagem, registrar avaliação, prioridade, conduta, exames/encaminhamentos e assinatura.
4. **Finalização:** encerrar o atendimento e atualizar a fila.
5. **Painel de fila:** exibir a chamada atual, próxima senha e estimativa de espera quando houver dados suficientes.

## Requisitos

- Faixas etárias prioritárias configuráveis.
- Registro de data/hora e usuário responsável por cada alteração.
- Exportação CSV controlada e auditável.
- Interface responsiva e acessível.
- Permissões distintas para recepção, triagem e equipe médica.

## Segurança e limites

Este é um escopo de projeto, não um sistema clínico validado. Dados de saúde são sensíveis. Uma implementação real precisa de autenticação, autorização por função, trilha de auditoria, minimização de dados, criptografia, políticas de retenção, testes de segurança e validação por profissionais de saúde. Não use pacientes reais em protótipos.

## Próximos passos

- Definir modelo de dados e papéis.
- Implementar primeiro um protótipo com dados fictícios.
- Criar testes de permissões e do fluxo de fila.
- Validar classificação e prioridades com responsáveis clínicos antes de qualquer uso real.
