# Catálogo de projetos — Natan Silva

Este documento reúne projetos que desenvolvi, planejei ou prototipei durante meus estudos e conversas de desenvolvimento. **A situação de cada item é indicada para não confundir uma ideia com um produto concluído.** Os projetos sem link próprio ainda precisam ser organizados em repositórios independentes.

## Contas Fácil

**Objetivo:** criar um aplicativo instalável (PWA) para organizar contas e acompanhar a situação financeira em celulares e computadores.

**Funcionalidades planejadas ou presentes no protótipo**
- Cadastro, edição e acompanhamento de contas pagas e pendentes.
- Resumo financeiro e gráficos por categoria e situação.
- Interface responsiva, transições suaves e instalação como PWA.
- Exportação de dados em CSV.
- Página inicial, seção “Quem somos” e contato de suporte.

**Tecnologias previstas:** HTML, CSS, JavaScript, PWA e Supabase/PostgreSQL.

**Situação real:** protótipo front-end preparado e orientações de hospedagem discutidas. Autenticação, sincronização entre dispositivos, controle de acesso, políticas de segurança do banco e funcionamento offline completo ainda precisam ser implementados e testados antes de tratar o app como serviço público.

## Sistema de triagem e fila clínica

**Objetivo:** organizar o fluxo de atendimento desde o cadastro até a finalização da consulta.

**Fluxo proposto**
1. Cadastro do paciente e emissão de senha.
2. Triagem para registrar sinais vitais, sintomas, observações e classificação inicial.
3. Atendimento médico com acesso aos dados da triagem, avaliação, prioridade, conduta, encaminhamentos e assinatura.
4. Finalização e acompanhamento da fila, com indicação do próximo atendimento e estimativa de espera.

**Requisitos considerados:** prioridade por faixa etária, painel de acompanhamento e exportação CSV.

**Situação real:** requisitos e fluxo funcional definidos; não apresentar como sistema clínico implantado. Um desenvolvimento real exige controle de acesso, auditoria, proteção de dados pessoais e de saúde, validação profissional e testes.

## Dashboard Django + Bokeh

**Objetivo:** exibir gráficos interativos em uma aplicação web Django.

**Implementação explorada:** rota de dashboard, view para gerar gráfico Bokeh e template que incorpora o gráfico na página.

**Tecnologias:** Python, Django, Bokeh e, como etapa planejada, MySQL.

**Situação real:** protótipo local de gráfico com dados de exemplo. Integração final com banco de dados, migrações, dados reais e publicação precisam ser concluídas e verificadas.

## Plataforma de monitoria e quizzes

**Objetivo:** criar um site de apoio aos estudos com experiência gamificada.

**Funcionalidades propostas**
- Cadastro de usuário e progresso por atividade.
- Perguntas e feedback, resumos e revisão de dez questões.
- XP, títulos, ranking e desafios de maior dificuldade.
- Personagem de professor para dicas e orientação.
- Prática de código e possível geração de questões com IA.
- Temas claro e escuro.

**Situação real:** especificação de produto construída; recursos não devem ser considerados implementados sem código e testes verificáveis.

## Acesso remoto simplificado

**Objetivo:** estudar uma alternativa de acesso remoto para computadores, com possibilidade de suporte a celulares posteriormente.

**Direção técnica:** personalizar e configurar o RustDesk, com identidade visual própria e fluxo de conexão por ID e senha para acesso autorizado.

**Prioridades de segurança:** autenticação robusta, consentimento e autorização claros, registro de sessões, armazenamento seguro de credenciais, configuração protegida do servidor e possibilidade de revogar dispositivos. Acesso não supervisionado deve ser explícito, configurável e restrito a dispositivos autorizados.

**Situação real:** plano técnico em elaboração. Não há produto pronto para distribuição até que a implementação e os testes de segurança e compatibilidade sejam feitos.

## Color Clash — Arduino e LEDs

**Objetivo:** criar um jogo competitivo para apresentação acadêmica, com dois jogadores ou adversário controlado pelo computador.

**Ideias de funcionamento**
- Joysticks para mirar e disparar ações virtuais.
- Matriz de LEDs RGB para representar território e mudanças de cor.
- Placar e exibição dos campeões.
- Identidade visual própria e possível troféu para impressão 3D.

**Situação real:** conceito e seleção de componentes discutidos; hardware, alimentação elétrica, montagem e jogabilidade precisam ser validados na prática.

## Próxima etapa recomendada

Priorizar um projeto de cada vez. Para cada repositório, incluir:
- Problema que o projeto resolve.
- Capturas de tela ou demonstração real.
- Tecnologias efetivamente usadas.
- Instruções para instalar e executar.
- Testes, limitações conhecidas e próximos passos.
- Um README que diferencie claramente protótipo, versão funcional e funcionalidades futuras.

**Nota:** este catálogo documenta a trajetória de desenvolvimento e não afirma que todos os projetos estejam concluídos ou publicados.
