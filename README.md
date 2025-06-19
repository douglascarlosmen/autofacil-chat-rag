# 🤖 AutoFácil Chat RAG

Um sistema de chat inteligente baseado em RAG (Retrieval-Augmented Generation) desenvolvido para a empresa fictícia AutoFácil Veículos. Este projeto permite que funcionários e clientes façam perguntas sobre documentos internos da empresa e recebam respostas precisas baseadas no conhecimento corporativo.

## 🚀 Funcionalidades

- **Upload de Documentos**: Suporte para arquivos PDF e texto
- **Processamento Inteligente**: Divisão automática em chunks otimizados
- **Chat Interativo**: Interface web para conversas em tempo real
- **RAG Avanzado**: Combina busca semântica com geração de respostas
- **API REST**: Endpoints para integração com outros sistemas
- **Persistência**: Armazenamento local com ChromaDB

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido
- **LangChain**: Framework para aplicações de IA
- **OpenAI GPT-3.5**: Modelo de linguagem para geração de respostas
- **ChromaDB**: Banco de dados vetorial para busca semântica
- **PyMuPDF**: Processamento de arquivos PDF
- **HTML/CSS/JavaScript**: Interface web responsiva

## 📋 Pré-requisitos

- Python 3.8+
- Conta na OpenAI (API Key)
- Git

## 🔧 Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/douglascarlosmen/autofacil-chat-rag.git
   cd autofacil-chat-rag
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente**
   ```bash
   cp .env.example .env
   ```
   
   Edite o arquivo `.env` e adicione suas credenciais:
   ```env
   OPENAI_API_KEY=sua_chave_api_aqui
   CHROMA_DB_DIR=./vectorstore/db
   ```

4. **Execute a aplicação**
   ```bash
   uvicorn main:app --reload
   ```

## 🚀 Como Usar

### Interface Web
1. Acesse `http://localhost:8000/chat` no seu navegador
2. Faça perguntas sobre os documentos da empresa
3. Receba respostas baseadas no conhecimento corporativo

### API REST

#### Upload de Documentos
```bash
curl -X POST "http://localhost:8000/webhook/ingest" \
  -H "Content-Type: application/json" \
  -d '{
    "filename": "manual.pdf",
    "content": "base64_do_arquivo_aqui"
  }'
```

#### Chat via API
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Como funciona o processo de venda?"
  }'
```

## 📁 Estrutura do Projeto

```
autofacil-chat-rag/
├── main.py              # Aplicação principal FastAPI
├── requirements.txt     # Dependências Python
├── .env.example        # Exemplo de configuração
├── README.md           # Este arquivo
└── static/
    └── chat.html       # Interface web do chat
```

## 🔍 Endpoints da API

- `GET /` - Status da API
- `GET /chat` - Interface web do chat
- `POST /webhook/ingest` - Upload de documentos
- `POST /chat` - Chat via API

## 🎯 Casos de Uso

- **Atendimento ao Cliente**: Respostas rápidas sobre produtos e serviços
- **Treinamento de Funcionários**: Acesso ao conhecimento corporativo
- **Suporte Técnico**: Consulta a manuais e documentação
- **Vendas**: Informações sobre produtos e processos

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Douglas Men**
- GitHub: [@douglascarlosmen](https://github.com/douglascarlosmen)
- Blog: [Descomplica GPT](https://descomplicagpt.com.br/)
- YouTube: [Descomplica Dev](https://youtube.com/descomplicadev)

## 📚 Recursos Adicionais

- [Artigo sobre RAG no blog](https://descomplicagpt.com.br/)
- [Tutoriais no YouTube](https://youtube.com/descomplicadev)
- [Repositório no GitHub](https://github.com/douglascarlosmen/autofacil-chat-rag.git)

## 🆘 Suporte

Se você encontrar algum problema ou tiver dúvidas, sinta-se à vontade para:
- Abrir uma issue no GitHub
- Entrar em contato através do blog
- Comentar nos vídeos do YouTube

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório e me seguir!
