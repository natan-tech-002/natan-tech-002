# Dashboard Django + Bokeh

## Objetivo

Criar uma aplicação Django que gere gráficos interativos no navegador com Bokeh, usando dados de exemplo inicialmente e banco de dados depois.

## Histórico técnico conhecido

O projeto foi trabalhado localmente em Windows, com arquivos como `manage.py`, projeto Django, apps `dashboard` e `graficos`, e banco SQLite de desenvolvimento. Um endpoint de gráfico com dados fixos foi executado anteriormente; a integração MySQL não estava concluída e havia migrações pendentes.

## Estrutura sugerida

```text
django-bokeh/
├── manage.py
├── config/
├── dashboard/
│   ├── views.py
│   ├── urls.py
│   └── templates/dashboard/grafico.html
├── requirements.txt
└── README.md
```

Os nomes reais dos módulos devem ser ajustados ao código-fonte local antes de mover os arquivos. Não sobrescreva o projeto local sem backup.

## Tecnologias

- Python
- Django
- Bokeh
- Pandas
- SQLite para desenvolvimento; MySQL apenas após configuração e testes

## Execução típica

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install django bokeh pandas
python manage.py check
python manage.py migrate
python manage.py runserver
```

Abra a rota de gráfico definida no `urls.py`. A rota exata depende da configuração existente.

## Próximas etapas

- Recuperar e copiar o projeto local completo para esta pasta.
- Registrar dependências e versões reais.
- Substituir dados fixos por consulta via ORM.
- Resolver migrações e testar a conexão com banco.
- Adicionar testes e instruções de implantação.
