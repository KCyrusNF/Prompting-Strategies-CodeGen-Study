import os
import tiktoken

def count_tokens(text: str, model: str = "gpt-4o") -> int:
    # Load tokenizer for the model
    enc = tiktoken.encoding_for_model(model)

    # Optional: use a fixed encoding explicitly (e.g., for cross-model consistency)
    # If you switch to a manual encoding (like below), make sure to update other
    # parts of the function accordingly—particularly any logic that depends on
    # the 'model' parameter or its associated tokenizer.
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
            if cmd == "n":
                break


if __name__ == "__main__":
    main()
