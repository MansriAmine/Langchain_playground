# LangChain Project

This project demonstrates various use cases of the LangChain library with the Groq API, showcasing different ways to interact with language models.

## Project Structure

### Files

- **basic_chat.py**: Basic interaction with the Groq model using user input from the console.
- **system_prompt_injection.py**: Demonstrates system prompt injection and multi-turn conversations with the model.
- **language_translator.py**: Translation example using a prompt template for language translation tasks.
- **math_solver.py**: Solves math problems step-by-step with a custom output parser to extract the final answer.
- **list_generator.py**: Generates a comma-separated list of objects in a given category using a custom output parser.
- **requirements.txt**: List of Python dependencies required for the project.
- **.env**: Environment variables file containing the API key for the Groq API.

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory with your Groq API key:

    ```properties
    GROQ_API_KEY="your_api_key_here"
    ```

## Usage

### Running the Scripts

- **Basic Chat** - Interact with the model directly:
    ```sh
    python basic_chat.py
    ```

- **System Prompt Injection** - See how system prompts affect model responses:
    ```sh
    python system_prompt_injection.py
    ```

- **Language Translator** - Translate text between languages:
    ```sh
    python language_translator.py
    ```

- **Math Solver** - Solve math problems with step-by-step working:
    ```sh
    python math_solver.py
    ```

- **List Generator** - Generate categorized lists:
    ```sh
    python list_generator.py
    ```

## Requirements

- Python 3.8+
- Groq API key
- Dependencies listed in `requirements.txt`
