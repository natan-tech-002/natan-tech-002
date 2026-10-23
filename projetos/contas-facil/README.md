# Contas Fácil — PWA financeiro

**Objetivo:** um aplicativo instalável para organizar contas e movimentações financeiras, visualizar resumos e gráficos, exportar dados e futuramente sincronizar com segurança entre celular e computador.

## Funcionalidades do pacote mais recente

O pacote de trabalho mais recente chama-se `Contas-Facil-v6-Melhoria-e-Publicacao.zip`. Ele contém HTML, CSS e JavaScript da interface, configuração PWA, service worker, página de privacidade, documentação de publicação e um esquema SQL para Supabase.

> Este README documenta o projeto; não afirma que o backend esteja implantado. A URL e a chave pública do Supabase estão vazias no arquivo de configuração do pacote e precisam ser configuradas no ambiente correto.

## Arquitetura

- Front-end: HTML, CSS e JavaScript.
- PWA: `manifest.json` e `sw.js`.
- Backend planejado: Supabase/PostgreSQL com políticas RLS.
- Hospedagem prevista: Netlify ou outro host estático com HTTPS.
- Contato de suporte configurado no pacote: `ti.natansilva@gmail.com`.

## Antes de publicar

1. Configure projeto Supabase próprio e revise o esquema SQL.
2. Use apenas a chave pública/anon no navegador; **nunca exponha a chave `service_role`**.
3. Ative políticas RLS e teste isolamento de dados entre usuários/dispositivos.
4. Configure a sincronização privada entre dispositivos com um mecanismo seguro de vinculação e revogação.
5. Teste CRUD, gráficos, exportação, modo offline, restauração e acessibilidade.
6. Verifique as regras de privacidade e não use dados financeiros reais nos testes públicos.
7. Configure variáveis e domínios do ambiente de hospedagem; não coloque segredos no repositório.

## Estado do projeto

- Interface/PWA: existe um pacote de código-fonte.
- Supabase: requer configuração e testes reais.
- Publicação em produção: não confirmada.
- Sincronização entre dispositivos: não declarar pronta até testar autenticação, permissões e recuperação de acesso.

## Próximos passos

1. Revisar o código e o esquema SQL.
2. Executar localmente e registrar bugs.
3. Configurar Supabase e RLS em ambiente de teste.
4. Testar em desktop e celular.
5. Publicar uma versão de demonstração sem dados pessoais.
