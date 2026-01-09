# 🧠 Resumo Inteligente de Contratos

Aplicação web para **análise e comparação de contratos em PDF**,
utilizando Inteligência Artificial. O sistema gera um resumo técnico
estruturado e oferece a opção de **linguagem simples**, tornando o
conteúdo acessível a pessoas sem formação jurídica.

> ⚠️ Este projeto tem caráter **informativo** e **não substitui** a
> análise de um advogado.

------------------------------------------------------------------------

## ✨ Funcionalidades

-   📄 Análise de **1 contrato em PDF**
-   🔍 Comparação de **2 contratos**
-   🧾 Resumo estruturado com:
    -   Tipo de contrato
    -   Partes envolvidas
    -   Obrigações
    -   Prazos
    -   Penalidades
    -   Riscos jurídicos, financeiros e operacionais
-   🧠 Classificação do tipo contratual
-   🧩 Análise opinativa limitada (sem aconselhamento jurídico)
-   🔄 Opção de **linguagem simples**
-   🎨 Interface moderna com animações suaves

------------------------------------------------------------------------

## 🗂 Estrutura do Projeto

    contract-agent/
    │
    ├── backend/
    │   ├── agent/
    │   │   ├── ai_client.py
    │   │   ├── comparer.py
    │   │   ├── prompt.py
    │   │   ├── rate_limiter.py
    │   │   ├── summarizer.py
    │   │   ├── token_monitor.py
    │   │   └── validator.py
    │   │
    │   ├── extractor/
    │   │   └── pdf_reader.py
    │   │
    │   ├── db/
    │   │   ├── database.py
    │   │   └── models.py
    │   │
    │   ├── api.py
    │   ├── requirements.txt
    │   └── venv/
    │
    ├── frontend/
    │   ├── index.html
    │   ├── css/
    │   │   └── main.css
    │   └── js/
    │       └── main.js
    │
    └── README.md

------------------------------------------------------------------------

## 🛠 Requisitos

-   Python **3.10+**
-   Conta na **OpenAI** com créditos ativos
-   Navegador moderno (Chrome, Edge, Firefox)

------------------------------------------------------------------------

## ⚙️ Instalação (Backend)

1.  Acesse a pasta do backend:

``` bash
cd backend
```

2.  Crie o ambiente virtual:

``` bash
python -m venv venv
```

3.  Ative o ambiente virtual:

**Windows (PowerShell):**

``` bash
venv\Scripts\Activate.ps1
```

**Linux / Mac:**

``` bash
source venv/bin/activate
```

4.  Instale as dependências:

``` bash
pip install -r requirements.txt
```

5.  Configure sua chave da OpenAI:

``` bash
setx OPENAI_API_KEY "sua-chave-aqui"
```

------------------------------------------------------------------------

## ▶️ Executar o Backend

``` bash
uvicorn api:app --reload
```

A API ficará disponível em:

    http://localhost:8000

Documentação automática:

    http://localhost:8000/docs

------------------------------------------------------------------------

## 🌐 Executar o Frontend

1.  Entre na pasta `frontend`
2.  Abra o arquivo `index.html` no navegador

> Não é necessário servidor web --- o frontend é estático.

------------------------------------------------------------------------

## 🧩 Como Usar

### 🔹 Analisar 1 contrato

1.  Selecione **Analisar 1 contrato**
2.  Envie um PDF
3.  (Opcional) Ative **Usar linguagem simples**
4.  Clique em **Gerar resumo**

### 🔹 Comparar 2 contratos

1.  Selecione **Comparar 2 contratos**
2.  Envie os dois PDFs
3.  Clique em **Comparar contratos**

------------------------------------------------------------------------

## ⚠️ Limitações Importantes

-   O sistema **não fornece aconselhamento jurídico**
-   A análise depende exclusivamente do texto do contrato
-   Resultados podem variar conforme a clareza do documento
-   É necessário crédito ativo na OpenAI para funcionar

------------------------------------------------------------------------

## 🚀 Próximas Evoluções (Ideias)

-   Histórico de análises
-   Exportação em PDF
-   Níveis de linguagem (simples, intermediário, técnico)
-   Multi-idioma
-   Autenticação de usuários

------------------------------------------------------------------------

## 👨‍💻 Autor (Eduardo Monteiro)

Projeto desenvolvido para fins educacionais, técnicos e demonstrativos.

------------------------------------------------------------------------

## 📄 Licença

Uso livre para estudo e aprendizado.
