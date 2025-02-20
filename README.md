# 📌 INSS Benefícios API

Sistema comercial para consulta de benefícios do INSS via API oficial do **Gov.br**. Permite autenticação segura (OAuth2), consulta de benefícios ativos, verificação de indeferimentos e geração de relatórios em um painel web.

## 🚀 Tecnologias Utilizadas
- **Back-end**: Python, Flask
- **Autenticação**: OAuth2 via Gov.br
- **API**: Integração com Gov.br para consulta de benefícios
- **Banco de Dados**: [Adicionar se necessário]
- **Front-end**: [Adicionar a tecnologia escolhida]

## 📥 Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/inss-beneficios-api.git
   cd inss-beneficios-api
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure as variáveis de ambiente:
   ```bash
   cp .env.example .env  # Crie o arquivo de ambiente
   ```
   Edite o arquivo `.env` com suas credenciais:
   ```env
   CLIENT_ID=seu-client-id
   CLIENT_SECRET=seu-client-secret
   SECRET_KEY=sua-secret-key
   ```
5. Execute o servidor Flask:
   ```bash
   flask run
   ```

## 🔑 Autenticação com Gov.br
- O sistema usa **OAuth2** para autenticação segura.
- Para configurar o login, é necessário registrar sua aplicação no portal **Gov.br**.

## 📌 Funcionalidades
✅ Autenticação via Gov.br (OAuth2)  
✅ Consulta de benefícios ativos do INSS  
✅ Verificação de indeferimentos e motivos  
✅ Relatórios detalhados sobre status dos benefícios  

## 🛠 Próximos Passos
- [ ] Criar o front-end para exibição dos dados
- [ ] Melhorar segurança e armazenamento dos tokens
- [ ] Implementar banco de dados para salvar consultas

## 📄 Licença
Este projeto está sob a licença [Adicionar Licença].


