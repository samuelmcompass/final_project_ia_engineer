def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    except FileNotFoundError:
        return "Error: File not found."

    except UnicodeDecodeError:
        return "Error: Invalid file encoding."

    except Exception as error:
        return f"Unexpected error: {error}"