# Contas Fácil — arquitetura e roteiro

## Decisões e objetivos
- PWA responsivo para celular e computador.
- Contas e movimentações individuais.
- Uso offline com dados locais e fila de sincronização futura.
- Código privado para vincular dispositivos como etapa adicional, nunca como única credencial.
- Exportação de dados e suporte acessível.

## Arquitetura de produção proposta
1. Front-end PWA hospedado por HTTPS.
2. Supabase Auth para login e recuperação de acesso.
3. PostgreSQL com RLS; cada registro pertence a um usuário autenticado.
4. Fila offline em IndexedDB com IDs idempotentes, estados e resolução de conflitos.
5. Vinculação de dispositivo com código temporário validado no servidor, rate limit, expiração, rotação e revogação.
6. Fluxos de exportação e exclusão de dados e política de privacidade pública.

## Próximas etapas técnicas
- Configurar URL e chave pública do Supabase; nunca usar `service_role` no front-end.
- Implementar autenticação e garantir que dados financeiros só carreguem na sessão correta.
- Isolar dados locais por usuário.
- Implementar CRUD remoto, fila offline e tratamento de conflitos.
- Adicionar testes para isolamento entre usuários, repetição de operações, logout e recuperação de senha.
- Fazer auditoria de segurança antes de lançar.

## Estado
O pacote inclui interface/PWA e um esquema SQL inicial. Isso não comprova que autenticação, sincronização multiusuário ou vinculação de dispositivos estejam concluídas. Testar em ambiente de desenvolvimento antes de usar dados reais.
