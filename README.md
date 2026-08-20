# 🐍 Python — Fundamentos e Desenvolvimento de Sistemas

> Guia de estudos dos principais conceitos do Python, organizado para quem está começando no desenvolvimento de sistemas e quer construir uma base sólida na linguagem.

---

## 📌 Sobre o projeto

Este repositório foi criado para reunir conceitos fundamentais de **Python**, desde os primeiros comandos até estruturas utilizadas no desenvolvimento de aplicações.

O objetivo é servir como material de estudo e também como referência para projetos futuros.

### 🎯 Objetivos

* Aprender a sintaxe básica do Python
* Compreender variáveis e tipos de dados
* Trabalhar com operadores
* Utilizar estruturas condicionais
* Criar estruturas de repetição
* Trabalhar com listas, tuplas, conjuntos e dicionários
* Criar e utilizar funções
* Entender programação orientada a objetos
* Trabalhar com arquivos
* Utilizar tratamento de exceções
* Organizar projetos Python
* Conhecer boas práticas de desenvolvimento

---

# 🐍 Por que Python?

Python é uma linguagem de programação de alto nível, conhecida principalmente por sua:

* Simplicidade
* Legibilidade
* Grande quantidade de bibliotecas
* Comunidade ativa
* Versatilidade
* Facilidade para criação de protótipos e sistemas

Python pode ser utilizado em áreas como:

```text
Desenvolvimento Web
Automação
Inteligência Artificial
Ciência de Dados
Machine Learning
APIs
Sistemas
Scripts
Análise de Dados
DevOps
```

---

# 📚 Conceitos fundamentais do Python

## 1. Sintaxe

A sintaxe define como o código Python deve ser escrito.

Um dos principais diferenciais do Python é a utilização da **indentação** para definir blocos de código.

```python
idade = 18

if idade >= 18:
    print("Maior de idade")
```

A indentação não é apenas estética: ela faz parte da estrutura da linguagem.

---

# 2. Variáveis

Variáveis armazenam valores que podem ser utilizados durante a execução do programa.

```python
nome = "Douglas"
idade = 20
altura = 1.75
```

Python utiliza tipagem dinâmica, portanto não é necessário declarar explicitamente o tipo da variável.

```python
nome = "Douglas"
idade = 20

print(nome)
print(idade)
```

---

# 3. Tipos de dados

Os principais tipos básicos são:

| Tipo    | Exemplo          |
| ------- | ---------------- |
| `str`   | `"Python"`       |
| `int`   | `10`             |
| `float` | `10.5`           |
| `bool`  | `True` / `False` |
| `None`  | `None`           |

Exemplo:

```python
nome = "Python"
idade = 30
preco = 19.90
ativo = True
resultado = None
```

Podemos descobrir o tipo de uma variável utilizando `type()`:

```python
idade = 20

print(type(idade))
```

Resultado:

```text
<class 'int'>
```

---

# 4. Strings

Strings representam textos.

```python
nome = "Python"
```

Podemos realizar diversas operações:

```python
nome = "Python"

print(nome.upper())
print(nome.lower())
print(len(nome))
```

Também podemos utilizar f-strings para criar textos dinâmicos:

```python
nome = "Douglas"
idade = 20

mensagem = f"Meu nome é {nome} e tenho {idade} anos."

print(mensagem)
```

---

# 5. Operadores

## Operadores matemáticos

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Principais operadores:

```text
+    Soma
-    Subtração
*    Multiplicação
/    Divisão
//   Divisão inteira
%    Resto da divisão
**   Potência
```

---

# 6. Operadores de comparação

São utilizados para comparar valores.

```python
idade = 20

print(idade == 20)
print(idade != 18)
print(idade > 18)
print(idade < 30)
print(idade >= 18)
print(idade <= 30)
```

O resultado será `True` ou `False`.

---

# 7. Operadores lógicos

Os principais são:

```text
and
or
not
```

Exemplo:

```python
idade = 20
possui_documento = True

if idade >= 18 and possui_documento:
    print("Acesso permitido")
```

---

# 8. Estruturas condicionais

Permitem que o programa tome decisões.

## if

```python
idade = 18

if idade >= 18:
    print("Maior de idade")
```

## if / else

```python
idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

## if / elif / else

```python
nota = 8

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")
```

---

# 9. Listas

Listas armazenam múltiplos valores.

```python
frutas = ["maçã", "banana", "laranja"]

print(frutas)
```

Podemos acessar elementos através do índice:

```python
print(frutas[0])
```

O primeiro elemento possui índice `0`.

Também podemos adicionar e remover elementos:

```python
frutas.append("uva")
frutas.remove("banana")
```

---

# 10. Tuplas

Tuplas são semelhantes às listas, porém são imutáveis.

```python
coordenadas = (10, 20)

print(coordenadas)
```

São úteis quando queremos armazenar informações que não devem ser alteradas.

---

# 11. Conjuntos — set

Sets armazenam valores únicos.

```python
numeros = {1, 2, 3, 3, 4}

print(numeros)
```

Resultado:

```text
{1, 2, 3, 4}
```

O valor duplicado é eliminado.

---

# 12. Dicionários

Dicionários armazenam dados no formato:

```text
chave → valor
```

Exemplo:

```python
usuario = {
    "nome": "Douglas",
    "idade": 20,
    "ativo": True
}

print(usuario["nome"])
```

Dicionários são extremamente importantes no desenvolvimento de sistemas porque são muito utilizados para representar dados estruturados.

---

# 13. Estruturas de repetição

## for

Utilizado quando queremos percorrer uma sequência.

```python
frutas = ["maçã", "banana", "uva"]

for fruta in frutas:
    print(fruta)
```

## while

Executa um bloco enquanto uma condição for verdadeira.

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

---

# 14. break e continue

`break` interrompe o loop.

```python
for numero in range(10):
    if numero == 5:
        break

    print(numero)
```

`continue` pula para a próxima iteração.

```python
for numero in range(10):
    if numero == 5:
        continue

    print(numero)
```

---

# 15. Funções

Funções permitem organizar e reutilizar código.

```python
def saudacao():
    print("Olá, mundo!")

saudacao()
```

Funções podem receber parâmetros:

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Douglas")
```

Também podem retornar valores:

```python
def somar(a, b):
    return a + b

resultado = somar(10, 5)

print(resultado)
```

### 💡 Boa prática

Uma função deve, preferencialmente, possuir uma responsabilidade clara.

Evite criar funções gigantes que fazem várias coisas diferentes.

---

# 16. Escopo

Escopo define onde uma variável pode ser acessada.

```python
def exemplo():
    mensagem = "Olá"

    print(mensagem)

exemplo()
```

A variável `mensagem` pertence ao escopo da função.

É importante compreender a diferença entre:

```text
Variável local
Variável global
```

Em projetos maiores, prefira controlar cuidadosamente o escopo para evitar comportamentos inesperados.

---

# 17. Tratamento de erros

Erros podem acontecer durante a execução de um programa.

Python utiliza `try` e `except` para tratamento de exceções.

```python
try:
    numero = int(input("Digite um número: "))
    print(10 / numero)

except ValueError:
    print("Digite um número válido.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

Também podemos utilizar:

```python
finally:
    print("Execução finalizada.")
```

---

# 18. Entrada de dados

Podemos receber informações do usuário utilizando `input()`.

```python
nome = input("Digite seu nome: ")

print(f"Olá, {nome}!")
```

Por padrão, `input()` retorna uma string.

Para receber números:

```python
idade = int(input("Digite sua idade: "))
```

Ou:

```python
altura = float(input("Digite sua altura: "))
```

---

# 19. Módulos

Um módulo é um arquivo Python que pode conter funções, classes e variáveis reutilizáveis.

Por exemplo:

```python
import math

print(math.sqrt(25))
```

Também podemos importar partes específicas:

```python
from math import sqrt

print(sqrt(25))
```

---

# 20. Bibliotecas

Python possui uma grande quantidade de bibliotecas.

Exemplos:

```text
requests   → requisições HTTP
pandas     → análise de dados
numpy      → computação numérica
flask      → desenvolvimento web
django     → desenvolvimento web
fastapi    → criação de APIs
pytest     → testes
```

O uso de bibliotecas permite evitar a implementação manual de funcionalidades que já existem.

---

# 21. Programação Orientada a Objetos

A Programação Orientada a Objetos (POO) organiza o código utilizando **classes e objetos**.

Exemplo:

```python
class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}.")


pessoa = Pessoa("Douglas", 20)

pessoa.apresentar()
```

Conceitos importantes:

```text
Classe
Objeto
Atributo
Método
Encapsulamento
Herança
Polimorfismo
Abstração
```

---

# 22. Classes e objetos

Uma classe funciona como um modelo.

```python
class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
```

Podemos criar objetos:

```python
carro = Carro("Toyota", "Corolla")

print(carro.marca)
print(carro.modelo)
```

---

# 23. Arquivos

Python permite trabalhar com arquivos.

Exemplo:

```python
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
```

Para escrever:

```python
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, Python!")
```

O `with` é recomendado porque ajuda a garantir que o arquivo seja fechado corretamente.

---

# 24. List Comprehension

Python possui uma sintaxe bastante poderosa para criar listas.

Forma tradicional:

```python
numeros = []

for numero in range(10):
    numeros.append(numero * 2)
```

Com list comprehension:

```python
numeros = [numero * 2 for numero in range(10)]
```

Apesar de ser mais compacta, deve ser utilizada com equilíbrio. Código legível é mais importante do que código excessivamente curto.

---

# 25. Tipagem

Python possui tipagem dinâmica, mas também permite utilizar **type hints**.

```python
def somar(a: int, b: int) -> int:
    return a + b
```

Isso ajuda a documentar o código e melhora o suporte de ferramentas de desenvolvimento.

Exemplo:

```python
nome: str = "Douglas"
idade: int = 20
altura: float = 1.75
ativo: bool = True
```

---

# 26. Ambiente virtual

Em projetos reais, é importante isolar as dependências.

Podemos criar um ambiente virtual:

```bash
python -m venv .venv
```

Ativação no Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Depois podemos instalar dependências:

```bash
pip install requests
```

E gerar um arquivo de dependências:

```bash
pip freeze > requirements.txt
```

---

# 27. Estrutura recomendada de projeto

Uma estrutura simples pode ser:

```text
meu-projeto/
│
├── .venv/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── services.py
│
├── tests/
│   └── test_main.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── pyproject.toml
```

A estrutura pode variar de acordo com o tamanho e o tipo do projeto.

---

# 28. Git e GitHub

Para projetos Python, é importante não versionar arquivos desnecessários.

Um `.gitignore` básico pode conter:

```gitignore
.venv/
__pycache__/
*.pyc
.env
.pytest_cache/
```

Comandos básicos:

```bash
git init
git add .
git commit -m "Inicializa projeto"
git branch -M main
git remote add origin URL_DO_REPOSITORIO
git push -u origin main
```

---

# 🧠 Conceitos que você deve dominar

Para construir uma boa base em Python, recomendo estudar nesta ordem:

```text
1. Sintaxe
2. Variáveis
3. Tipos de dados
4. Operadores
5. Condicionais
6. Loops
7. Listas
8. Tuplas
9. Sets
10. Dicionários
11. Funções
12. Escopo
13. Exceções
14. Módulos
15. Pacotes
16. Arquivos
17. POO
18. Type hints
19. Ambientes virtuais
20. Testes
21. Git/GitHub
22. APIs
23. Banco de dados
24. Arquitetura de sistemas
```

---

# 🏗️ Do Python para desenvolvimento de sistemas

Depois de dominar os fundamentos, o próximo passo é aprender como transformar código Python em sistemas reais.

Uma possível evolução:

```text
Python
   │
   ├── Git/GitHub
   │
   ├── Programação Orientada a Objetos
   │
   ├── Banco de Dados
   │
   ├── SQL
   │
   ├── APIs
   │
   ├── Framework Web
   │      ├── Django
   │      ├── Flask
   │      └── FastAPI
   │
   ├── Testes
   │
   ├── Docker
   │
   └── Deploy
```

---

# 🧪 Exemplo de pequeno sistema

Um exemplo simples utilizando vários conceitos:

```python
usuarios = []


def cadastrar_usuario(nome, idade):
    usuario = {
        "nome": nome,
        "idade": idade
    }

    usuarios.append(usuario)


def listar_usuarios():
    for usuario in usuarios:
        print(
            f"Nome: {usuario['nome']} | "
            f"Idade: {usuario['idade']}"
        )


cadastrar_usuario("Douglas", 20)
cadastrar_usuario("Maria", 25)

listar_usuarios()
```

Esse pequeno exemplo já utiliza:

* Variáveis
* Listas
* Dicionários
* Funções
* Parâmetros
* Loops
* Estruturas de dados

---

# 🚀 Próximos projetos

Depois de estudar os fundamentos, alguns projetos interessantes para praticar são:

### 🟢 Nível iniciante

* Calculadora
* Conversor de unidades
* Sistema de notas
* Lista de tarefas
* Cadastro de usuários
* Sistema de caixa simples

### 🟡 Nível intermediário

* Sistema de estoque
* Sistema financeiro
* API REST
* Sistema de login
* CRUD com banco de dados
* Sistema de gerenciamento de funcionários

### 🔴 Nível avançado

* API com autenticação
* Sistema web completo
* Sistema com arquitetura em camadas
* Aplicação com Docker
* API integrada a banco de dados
* Sistema com testes automatizados
* Aplicação publicada em produção

---

# 📖 Boas práticas

Ao desenvolver sistemas em Python:

* Escreva código legível
* Utilize nomes de variáveis claros
* Evite repetir código
* Divida sistemas grandes em módulos
* Crie funções com responsabilidades específicas
* Utilize tratamento de exceções
* Escreva testes
* Utilize ambientes virtuais
* Documente seu projeto
* Utilize Git
* Não coloque senhas ou chaves de API no código
* Utilize `.env` para configurações sensíveis
* Mantenha as dependências organizadas

---

# 📌 Conclusão

Aprender Python não significa apenas memorizar comandos.

O mais importante é compreender **como resolver problemas utilizando lógica de programação**.

A evolução recomendada é:

```text
Lógica de programação
        ↓
Fundamentos do Python
        ↓
Estruturas de dados
        ↓
Funções
        ↓
POO
        ↓
Banco de dados
        ↓
APIs
        ↓
Frameworks
        ↓
Testes
        ↓
Arquitetura
        ↓
Deploy
        ↓
Desenvolvimento de sistemas
```

> 💡 **Regra principal:** antes de aprender frameworks e ferramentas complexas, construa uma base forte em lógica, Python, estruturas de dados, funções e orientação a objetos.

---

## 👨‍💻 Status

🚧 Em desenvolvimento — novos exemplos e projetos serão adicionados conforme os estudos avançarem.

---

## 📄 Licença

Este projeto pode ser utilizado para fins educacionais e de estudo.
