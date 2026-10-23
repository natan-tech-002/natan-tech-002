# Supabase — próxima fase do Contas Fácil

**A conexão em nuvem está desativada no frontend da versão de demonstração.** Não cole chaves privadas nesta versão e não abra políticas RLS públicas para fazê-la funcionar. O SQL do pacote original é um ponto de partida, não uma integração pronta.

## Arquitetura planejada
1. Supabase Auth para cadastro, confirmação, login, logout e recuperação de senha.
2. Tabelas PostgreSQL com `user_id` e Row Level Security (RLS).
3. Fila offline persistente em IndexedDB, com IDs idempotentes e estados pendente/sincronizado/falhou.
4. Vinculação de dispositivo validada no servidor/Edge Function; o código não pode funcionar como senha-mestra.
5. Expiração, rotação, limite de tentativas e revogação de dispositivos.
6. Exclusão de conta/dados, backup/exportação e política de privacidade final.

## Configurar ambiente de desenvolvimento
1. Crie um projeto em https://supabase.com/dashboard.
2. Revise o arquivo SQL do pacote original antes de executá-lo em um projeto de teste.
3. Teste SELECT, INSERT, UPDATE e DELETE com duas contas diferentes.
4. Confirme que uma conta não consegue ler ou modificar os dados da outra.
5. Nunca coloque `service_role` ou segredo administrativo em arquivos enviados ao navegador.

## Antes de ativar a nuvem
- Implementar e testar autenticação ponta a ponta.
- Garantir que toda operação respeite RLS.
- Implementar fila offline, deduplicação e resolução de conflitos.
- Implementar vinculação e revogação de dispositivos no servidor.
- Fazer revisão de segurança. Até lá, use apenas dados locais e backups.
