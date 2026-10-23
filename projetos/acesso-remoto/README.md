# Acesso remoto simplificado

## Objetivo

Estudar uma alternativa de suporte remoto para computadores primeiro e dispositivos móveis posteriormente, usando o RustDesk como base técnica em vez de reimplementar protocolos remotos do zero.

## Direção técnica

- Personalizar identidade visual e experiência de configuração.
- Configurar/administrar servidor de relay e rendezvous conforme documentação do projeto-base.
- Suportar conexões autorizadas por dispositivo.
- Planejar suporte a acesso não supervisionado apenas com ativação explícita pelo proprietário.

## Requisitos de segurança

- Não contornar consentimento nem controles do sistema operacional.
- Armazenar credenciais de forma protegida e permitir revogação.
- Usar autenticação forte, logs de conexão e atualizações seguras.
- Não registrar senhas de sessão em texto claro.
- Testar instalação, atualização, compatibilidade e exposição de portas.
- Respeitar licença e atribuição do RustDesk; não copiar marca ou código proprietário do AnyDesk.

## Situação

Plano técnico em elaboração. Não é um aplicativo pronto para instalação ou uso em produção.

## Próximos passos

1. Definir plataforma e escopo do MVP.
2. Fazer fork/configuração documentada do RustDesk.
3. Criar build reproduzível e processo de atualização.
4. Fazer revisão de segurança antes de distribuir.
