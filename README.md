 ## Estrutura 
 
-  Seguindo princípios de Clean Code

-  Arquitetura separadas

-  Comunicação  via MCP (Model Context Protocol)

## Agente Virtual Inteligente (Terminal)

- Agente virtual com comportamento especilizada no projeto

- Utilizado plataforma Hugging Face
  
- Integração com o modelo LLAMA

- Técnica RAG  aplicada



depêndencia Ai (necessario GPU):

```
pip install -q transformers einops accelerate bitsandbytes
pip install -q langchain langchain_community langchain-huggingface langchainhub langchain_chroma

```

Para usar o modelo precisa ter um gpu, para fins demostrativo e reserva apresento a solução usando google colab, que disponibiliza GPU

[Link do código google colab ](https://colab.research.google.com/drive/1TYnPwXZ6fbIwPcEs2cdSowiPTRlN8gIX#scrollTo=HV6F8YcLaWJp)
