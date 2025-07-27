import os
import requests

class LLMProvider:
    def send(self, prompt: str) -> str:
        raise NotImplementedError

class GeminiProvider(LLMProvider):
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        self.endpoint = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateText'

    def send(self, prompt: str) -> str:
        if not self.api_key:
            return 'GEMINI_API_KEY not configured.'
        data = {
            'prompt': {
                'text': prompt
            }
        }
        params = {'key': self.api_key}
        resp = requests.post(self.endpoint, json=data, params=params, timeout=30)
        try:
            resp.raise_for_status()
            content = resp.json().get('candidates', [{}])[0].get('output', '')
        except Exception:
            content = f'Error: {resp.text}'
        return content

class AnthropicProvider(LLMProvider):
    def __init__(self):
        self.api_key = os.getenv('ANTHROPIC_API_KEY')
        self.endpoint = 'https://api.anthropic.com/v1/complete'

    def send(self, prompt: str) -> str:
        if not self.api_key:
            return 'ANTHROPIC_API_KEY not configured.'
        headers = {
            'x-api-key': self.api_key,
            'content-type': 'application/json'
        }
        data = {
            'prompt': prompt,
            'model': 'claude-2',
            'max_tokens': 256
        }
        resp = requests.post(self.endpoint, headers=headers, json=data, timeout=30)
        try:
            resp.raise_for_status()
            content = resp.json().get('completion', '')
        except Exception:
            content = f'Error: {resp.text}'
        return content

PROVIDERS = {
    'gemini': GeminiProvider,
    'anthropic': AnthropicProvider,
}


def send_prompt(prompt: str) -> str:
    provider_name = os.getenv('LLM_PROVIDER', 'gemini')
    ProviderClass = PROVIDERS.get(provider_name)
    if not ProviderClass:
        return f'Unknown provider {provider_name}'
    provider = ProviderClass()
    return provider.send(prompt)

