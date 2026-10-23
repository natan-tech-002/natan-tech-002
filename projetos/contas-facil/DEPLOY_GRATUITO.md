# Publicar Contas Fácil — demonstração

Esta versão publica a interface PWA e o painel financeiro local. Ela **não ativa automaticamente login, iToken ou sincronização segura em nuvem**.

## Preparar
1. Use o pacote de código-fonte mais recente disponível no histórico do projeto.
2. Extraia todos os arquivos mantendo `index.html`, `app.js`, `style.css`, `manifest.json`, `sw.js`, `config.js`, `privacidade.html`, `privacy.css` e `icons/` na raiz.
3. Confira que a configuração do cliente não contém segredos.

## Hospedagem estática
1. Abra https://app.netlify.com/drop.
2. Arraste a pasta extraída para o fluxo de publicação manual.
3. Aguarde a URL HTTPS e teste no computador e no celular.
4. Verifique a página `privacidade.html`, instalação PWA, exportação e modo offline.

## Segurança
- Faça backup da versão anterior antes de substituir uma publicação existente.
- Não use dados financeiros reais na demonstração.
- A sincronização permanece desativada até autenticação, políticas de acesso e testes de isolamento estarem concluídos.
- Não exponha a chave Supabase `service_role` no browser.

## Referências
- Netlify: https://app.netlify.com/
- Planos Netlify: https://www.netlify.com/pricing/
- Supabase: https://supabase.com/dashboard
- Supabase RLS: https://supabase.com/docs/guides/database/postgres/row-level-security
