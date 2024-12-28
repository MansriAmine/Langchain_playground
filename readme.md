 LangChain Project

This project demonstrates the use of the LangChain library with various models and prompts to interact with a language model.

## Project Structure
.env .gitignore 1.py 2.py 3.py 4.py 5.py requirements.txt
### Files

- **1.py**: Basic interaction with the model using user input from the console.
- **2.py**: Interaction with the model using predefined messages.
- **3.py**: Translation example using the model.
- **4.py**: Math problem-solving example with a custom output parser.
- **5.py**: Generating a comma-separated list of objects in a category with a custom output parser.
- **requirements.txt**: List of dependencies required for the project.
- **.env**: Environment variables file containing the API key for the model.

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory with the following content:

    ```properties
    GROQ_API_KEY = "your_api_key_here"
    ```

## Usage

### Running the Scripts

- **1.py**: Run the script and enter your message when prompted.

    ```sh
    python 1.py
    ```

- **2.py**: Run the script to see the predefined messages interaction.

    ```sh
    python 2.py
    ```

- **3.py**: Run the script to see the translation example.

    ```sh
    python 3.py
    ```

- **4.py**: Run the script to see the math problem-solving example.

    ```sh
    python 4.py
    ```

- **5.py**: Run the script to see the comma-separated list generation example.

    ```sh
    python 5.py
    ```
