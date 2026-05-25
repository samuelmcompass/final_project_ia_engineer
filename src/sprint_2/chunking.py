from transformers import AutoTokenizer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rich.console import Console
from rich.panel import Panel

console = Console()

colors = [
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan"
]

# HuggingFace tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Split documents into REAL token chunks
def split_text(documents):

    splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
        tokenizer,
        chunk_size=150,
        chunk_overlap=20
    )

    chunks = splitter.split_documents(documents)

    return chunks


# Print chunk previews
def print_chunks(chunks, preview_size=300):

    for index, chunk in enumerate(chunks):

        color = colors[index % len(colors)]

        text = chunk.page_content

        # Count REAL tokens
        token_count = len(
            tokenizer.encode(text)
        )

        console.print(
            Panel(
                text[:preview_size],
                title=f"Chunk {index + 1}",
                border_style=color
            )
        )

        console.print(
            f"[bold white]Characters:[/bold white] {len(text)}"
        )

        console.print(
            f"[bold white]Words:[/bold white] {len(text.split())}"
        )

        console.print(
            f"[bold white]Tokens:[/bold white] {token_count}"
        )

        console.print(
            "\n" + "=" * 60 + "\n"
        )