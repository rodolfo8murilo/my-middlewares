# Scrapy Middlewares

Coleção de middlewares para projetos **Scrapy**, desenvolvidos para facilitar a integração com sites que utilizam diferentes mecanismos de proteção, fingerprinting e identificação de clientes HTTP.

O projeto reúne diferentes estratégias para realizar requisições HTTP em spiders Scrapy, permitindo alternar entre diferentes clientes conforme as necessidades de cada crawler.

## 🚀 Objetivo

O objetivo deste projeto é disponibilizar middlewares reutilizáveis para projetos Scrapy que precisam trabalhar com sites que apresentam diferentes níveis de dificuldade para automação.

Entre as tecnologias utilizadas estão:

* **Scrapy**
* **curl-cffi**
* **tls-client**
* **Scrapy Playwright**
* Python 3.12+

O projeto atualmente utiliza Scrapy `>=2.17.0,<3.0.0`, `curl-cffi`, `tls-client` e `scrapy-playwright`.

---

# 📁 Estrutura

```text
my-middlewares/
│
├── crawler/
│   └── ...
│
├── pyproject.toml
├── poetry.lock
├── scrapy.cfg
└── .gitignore
```

O projeto Scrapy é configurado através do `scrapy.cfg`, que utiliza `crawler.settings` como configuração padrão.

---

# 🧩 Middlewares

## curl_cffi

O `curl-cffi` permite realizar requisições HTTP utilizando uma implementação baseada em cURL com capacidade de imitar diferentes fingerprints de navegadores.

Isso pode ser útil quando um site diferencia requisições feitas por clientes HTTP tradicionais de requisições realizadas por navegadores.

### Quando utilizar

Pode ser utilizado quando:

* requisições Scrapy tradicionais são bloqueadas;
* o servidor verifica características do cliente HTTP;
* é necessário utilizar fingerprints semelhantes às de navegadores;
* uma API ou página funciona normalmente no navegador, mas apresenta bloqueios para clientes HTTP convencionais.

---

## TLS Client

O `tls-client` permite realizar requisições utilizando diferentes características de TLS e fingerprints de clientes.

Ele pode ser utilizado como uma alternativa quando uma aplicação web possui mecanismos que analisam características da conexão TLS para identificar clientes automatizados.

### Quando utilizar

É especialmente interessante para testar diferentes perfis de cliente quando uma requisição funciona no navegador, mas não funciona utilizando o downloader HTTP padrão do Scrapy.

---

## Scrapy Playwright

O `scrapy-playwright` permite integrar o **Playwright** ao fluxo de requisições do Scrapy.

Diferentemente de uma requisição HTTP tradicional, o Playwright permite executar páginas utilizando um navegador real, possibilitando trabalhar com aplicações que dependem de:

* JavaScript;
* renderização dinâmica;
* requisições executadas no navegador;
* conteúdo carregado após o carregamento inicial;
* cookies e estado de sessão;
* interações com elementos da página.

### Exemplo conceitual

Uma requisição pode ser enviada para o Playwright utilizando:

```python
yield scrapy.Request(
    url="https://example.com",
    meta={
        "playwright": True,
    },
)
```

Nesse cenário, a página é processada pelo navegador antes de ser entregue ao spider.

---

# ⚙️ Instalação

## Pré-requisitos

* Python >= 3.12
* Poetry
* Navegador Chromium/Chrome para utilização do Playwright

Clone o projeto:

```bash
git clone git@github.com:rodolfo8murilo/my-middlewares.git
cd my-middlewares
```

Instale as dependências:

```bash
poetry install
```

Entre no ambiente virtual:

```bash
poetry shell
```

Ou execute os comandos diretamente através do Poetry:

```bash
poetry run scrapy
```

---

# 🌐 Instalação do Playwright

Caso utilize o middleware baseado em Playwright, instale o navegador:

```bash
poetry run playwright install chromium
```

Em ambientes Linux, pode ser necessário instalar as dependências do navegador:

```bash
poetry run playwright install-deps chromium
```

---

# 🧪 Como testar

O projeto pode ser utilizado como base para testar diferentes estratégias de requisição dentro de um spider Scrapy.

Primeiro, verifique se o Scrapy está disponível:

```bash
poetry run scrapy version
```

Depois, liste os spiders disponíveis:

```bash
poetry run scrapy list
```

Execute um spider:

```bash
poetry run scrapy crawl NOME_DO_SPIDER
```

Para salvar os resultados:

```bash
poetry run scrapy crawl NOME_DO_SPIDER -O output.json
```

---

# 🔬 Testando diferentes clientes HTTP

Uma das principais finalidades deste projeto é permitir comparar diferentes estratégias de requisição.

Por exemplo:

```text
Scrapy HTTP
     │
     ├── curl-cffi
     │
     ├── TLS Client
     │
     └── Playwright
```

Dessa forma, um crawler pode utilizar uma estratégia diferente dependendo do comportamento do site.

### Exemplo de fluxo de teste

1. Testar a requisição padrão do Scrapy.
2. Verificar o status HTTP retornado.
3. Testar utilizando `curl-cffi`.
4. Comparar o resultado.
5. Testar `tls-client`, quando aplicável.
6. Utilizar Playwright quando a página depender de JavaScript ou comportamento de navegador.
7. Comparar estabilidade, tempo de resposta e conteúdo retornado.

---

# 📊 Por que utilizar diferentes middlewares?

Sites modernos podem utilizar diferentes mecanismos para diferenciar navegadores de clientes automatizados.

Uma única estratégia HTTP pode não funcionar para todas as fontes.

Por isso, este projeto busca fornecer uma arquitetura onde diferentes mecanismos possam ser utilizados conforme o cenário:

| Estratégia  | Uso principal                        |
| ----------- | ------------------------------------ |
| Scrapy HTTP | Sites simples e APIs                 |
| curl-cffi   | Fingerprint semelhante a navegadores |
| TLS Client  | Diferentes características TLS       |
| Playwright  | JavaScript e páginas renderizadas    |

---

# 🛠️ Tecnologias

* Python 3.12+
* Scrapy
* Poetry
* curl-cffi
* tls-client
* Scrapy Playwright
* Playwright

As dependências principais estão declaradas no `pyproject.toml`.

---

# 🎯 Casos de uso

Este projeto pode ser utilizado como base para:

* Web Scraping;
* Data Collection;
* Crawlers distribuídos;
* APIs que exigem clientes HTTP específicos;
* páginas renderizadas com JavaScript;
* automação de coleta de dados;
* experimentação com diferentes clientes HTTP;
* projetos de Engenharia de Dados.

---

# ⚠️ Uso responsável

Os middlewares devem ser utilizados apenas em sistemas e sites onde você tenha autorização para realizar requisições e coleta de dados.

Respeite:

* Termos de Uso;
* robots.txt quando aplicável;
* limites de requisições;
* políticas de acesso;
* legislação aplicável.

O objetivo deste projeto é **engenharia de software e pesquisa em automação de coleta de dados**, não a evasão de controles de acesso.

---

# 👨‍💻 Autor

**Rodolfo Murilo Barbosa Moura**

GitHub:
https://github.com/rodolfo8murilo

Projeto:
https://github.com/rodolfo8murilo/my-middlewares
