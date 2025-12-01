# Sistema de Pesquisa Eleitoral

## 📌 Descrição
O **Sistema de Pesquisa Eleitoral** é um projeto desenvolvido para gerenciar pesquisas eleitorais, permitindo criar pesquisas, cadastrar perguntas, registrar respostas e realizar análises básicas. O sistema conta com API, módulos internos estruturados e scripts SQL para criação e alimentação do banco de dados.

## 📂 Organização do Projeto

```bash
Sistema-de-Pesquisa-Eleitoral/
│
├── api/
│   └── routes/              # Rotas da API
│
├── core/                    # Lógica central do sistema
│
├── modules/                 # Módulos adicionais do sistema
│
├── AlimentarBancoDados.sql  # Script para popular o banco
├── BancoDados.sql           # Script de criação do banco
│
├── main.py                  # Arquivo principal de execução
├── requirements.txt         # Dependências do projeto
