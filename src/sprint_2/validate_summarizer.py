from langchain_community.llms import Ollama
from datetime import datetime


def validate_summary(summary_text, chunks):

    start = datetime.now()

    llm = Ollama(
        model="llama3",
        base_url="http://ollama:11434",
        temperature=0
    )

    # Convert chunks into original text
    original_text = "\n".join(
        chunk.page_content
        for chunk in chunks
    )

    prompt = f"""
    You are an AI evaluator.

    Compare the generated summary with the original text.

    ORIGINAL TEXT:
    {original_text}

    GENERATED SUMMARY:
    {summary_text}

    Answer the following:

    1. Is the summary accurate?
    2. Were the main points covered?
    3. Is there any hallucinated or invented information?
    4. Were any important points omitted?
    5. Give a score from 0 to 10.
    6. Explain your evaluation.

    Provide the answer in a structured format.
    """

    result = llm.invoke(prompt)

    end = datetime.now()

    print(f"\n\n---------VALIDATION RESULT---------\n {result}")

    delta = end - start

    hours, remainder = divmod(
        int(delta.total_seconds()),
        3600
    )

    minutes, seconds = divmod(remainder, 60)

    print(
        f"Validation time: "
        f"{hours}h {minutes}m {seconds}s"
    )

    return result