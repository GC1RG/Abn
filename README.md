# Abn

This project is a minimal example of a web app that can query different large language model providers such as Google's Gemini or Anthropic Claude. The app uses Flask for a simple backend and renders a basic HTML form.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set the provider you want to use with environment variables. Example:
   ```bash
   export LLM_PROVIDER=gemini
   export GEMINI_API_KEY=your_key_here
   ```
   or for Anthropic:
   ```bash
   export LLM_PROVIDER=anthropic
   export ANTHROPIC_API_KEY=your_key_here
   ```

3. Run the server:
   ```bash
   python app.py
   ```

Open your browser at `http://localhost:5000` and try a prompt.

## Running Tests

```
pytest
```

