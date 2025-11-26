import os
import tiktoken

def count_tokens(text: str, model: str = "gpt-4o") -> int:
    # Load tokenizer for the model
    enc = tiktoken.encoding_for_model(model)

    # Optional: Use a fixed encoding explicitly (e.g., for cross-model consistency)
    # Note: "o200k_base" is a general-purpose tokenizer shared across multiple
    # OpenAI models (GPT-4o, GPT-4o-mini, o1-preview, etc.). Using it manually can
    # help keep token counts consistent even when switching models, but it also
    # bypasses each model's default tokenizer behavior. If you choose this route,
    # make sure other parts of the function are updated accordingly, especially any
    # logic that assumes a model-specific tokenizer.
    # enc = tiktoken.get_encoding("o200k_base")

    # Verify the encode-decode process works correctly
    assert enc.decode(enc.encode(text)) == text, "Encoding/decoding mismatch!"

    # Encode and count tokens
    tokens = enc.encode(text)
    return len(tokens)


def main():
    while True:
        # Ask the user for a file path
        file_path = input("Enter the path to the text file: ").strip().strip('"').strip("'")

        try:
            # Read file contents
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            # Count tokens
            num_tokens = count_tokens(text)

            # Print the result
            file_name = os.path.basename(file_path)
            print(f"Number of tokens in '{file_name}': {num_tokens}\n")

        except FileNotFoundError:
            print(f"Error: File not found at '{file_path}'.\n")
        except AssertionError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Unexpected error: {e}\n")
        finally:
            cmd = input("Do you want to continue (y, n)? ")
            if cmd.lower() == "n":
                break


if __name__ == "__main__":
    main()
