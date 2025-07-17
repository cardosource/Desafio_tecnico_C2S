from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import torch
from dotenv import load_dotenv

load_dotenv()

def quant_config():
    return BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )

def carregando_model_tokenizer(model_id):
    def inner(quant_config):
        model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=quant_config)
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        return model, tokenizer
    return inner

def levantando_pipeline(model, tokenizer):
    return pipeline(
        model=model,
        tokenizer=tokenizer,
        task="text-generation",
        temperature=0.1,
        max_new_tokens=500,
        do_sample=True,
        repetition_penalty=1.1,
        return_full_text=False,
    )

def criando_llm(pipeline):
    return HuggingFacePipeline(pipeline=pipeline)

def prompts(template: str):
    return PromptTemplate.from_template(template)

def chain_carregando(prompt_template, llm):
    return prompt_template | llm | StrOutputParser()


model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
quant_config = quant_config()
model, tokenizer = carregando_model_tokenizer(model_id)(quant_config)
pipe = levantando_pipeline(model, tokenizer)
llm = criando_llm(pipe)

template_rag = """
<|begin_of_text|>
<|start_header_id|>system<|end_header_id|>
Você é um assistente virtual prestativo especializado em analisar e extrair 
informações de tabelas de dados. Quando o usuário fizer uma pergunta sobre 
os dados contidos em uma tabela, use os seguintes pedaços de contexto recuperado para responder.
Se você não sabe a resposta, apenas diga que não sabe. Mantenha a resposta concisa.
<|eot_id|>
<|start_header_id|>user<|end_header_id|>
Pergunta: {pergunta}
Contexto: {contexto}
<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""

prompt_rag = prompts(template_rag)
chain_rag = chain_carregando(prompt_rag, llm)

def query_iniciar(pergunta: str, contexto: str):
    return chain_rag.invoke({"pergunta": pergunta, "contexto": contexto})
