from langchain.chains.summarize import load_summarize_chain
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from datetime import datetime


def summarize(chunks, mode="short", user_prompt=None):

    inicio = datetime.now()

    llm = Ollama(
        model="llama3",
        base_url="http://ollama:11434",
        temperature=0
    )

    system_prompt = """
    You are a professional AI summarization assistant.
    """

    if mode == "short":
        mode_prompt = "Create a concise high-level summary."
    else:
        mode_prompt = (
            "Create a detailed summary with important information."
        )

    # FIRST SUMMARY PROMPT
    question_prompt = PromptTemplate(
        template=f"""
        {system_prompt}

        {mode_prompt}

        User request:
        {user_prompt}

        Summarize the following text concisely:

        {{text}}
        """,
        input_variables=["text"]
    )

    # REFINE PROMPT
    refine_prompt = PromptTemplate(
        template=f"""
        {system_prompt}

        We already have an existing summary:

        {{existing_answer}}

        Improve the summary using the new context below.

        User request:
        {user_prompt}

        New context:
        {{text}}

        Return an updated concise summary.
        """,
        input_variables=[
            "existing_answer",
            "text"
        ]
    )

    chain = load_summarize_chain(
        llm,
        chain_type="refine",
        question_prompt=question_prompt,
        refine_prompt=refine_prompt,
        verbose=False
    )

    result = chain.invoke({
        "input_documents": chunks
    })

    fim = datetime.now()

    diferenca = fim - inicio

    horas, resto = divmod(
        int(diferenca.total_seconds()),
        3600
    )

    minutos, segundos = divmod(resto, 60)

    print(
        f"Time spent in process: "
        f"{horas}h {minutos}m {segundos}s"
    )

    return result["output_text"]