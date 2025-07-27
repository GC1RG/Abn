import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import os
import llm_providers

class DummyProvider(llm_providers.LLMProvider):
    def send(self, prompt: str) -> str:
        return f"dummy:{prompt}"

llm_providers.PROVIDERS['dummy'] = DummyProvider

def test_send_prompt_env(monkeypatch):
    monkeypatch.setenv('LLM_PROVIDER', 'dummy')
    assert llm_providers.send_prompt('hi') == 'dummy:hi'

