"""Shared model catalog for CLI selections and validation."""

from __future__ import annotations

from typing import Dict, List, Tuple

ModelOption = Tuple[str, str]
ProviderModeOptions = Dict[str, Dict[str, List[ModelOption]]]


MODEL_OPTIONS: ProviderModeOptions = {
    "openai": {
        "quick": [
            ("GPT-5.4 Mini - Fast, strong coding and tool use", "gpt-5.4-mini"),
            ("GPT-5.4 Nano - Cheapest, high-volume tasks", "gpt-5.4-nano"),
            ("GPT-5.4 - Latest frontier, 1M context", "gpt-5.4"),
            ("GPT-4.1 - Smartest non-reasoning model", "gpt-4.1"),
        ],
        "deep": [
            ("GPT-5.4 - Latest frontier, 1M context", "gpt-5.4"),
            ("GPT-5.2 - Strong reasoning, cost-effective", "gpt-5.2"),
            ("GPT-5.4 Mini - Fast, strong coding and tool use", "gpt-5.4-mini"),
            ("GPT-5.4 Pro - Most capable, expensive ($30/$180 per 1M tokens)", "gpt-5.4-pro"),
        ],
    },
    "anthropic": {
        "quick": [
            ("Claude Sonnet 4.6 - Best speed and intelligence balance", "claude-sonnet-4-6"),
            ("Claude Haiku 4.5 - Fast, near-instant responses", "claude-haiku-4-5"),
            ("Claude Sonnet 4.5 - Agents and coding", "claude-sonnet-4-5"),
        ],
        "deep": [
            ("Claude Opus 4.6 - Most intelligent, agents and coding", "claude-opus-4-6"),
            ("Claude Opus 4.5 - Premium, max intelligence", "claude-opus-4-5"),
            ("Claude Sonnet 4.6 - Best speed and intelligence balance", "claude-sonnet-4-6"),
            ("Claude Sonnet 4.5 - Agents and coding", "claude-sonnet-4-5"),
        ],
    },
    "google": {
        "quick": [
            ("Gemini 3 Flash - Next-gen fast", "gemini-3-flash-preview"),
            ("Gemini 2.5 Flash - Balanced, stable", "gemini-2.5-flash"),
            ("Gemini 3.1 Flash Lite - Most cost-efficient", "gemini-3.1-flash-lite-preview"),
            ("Gemini 2.5 Flash Lite - Fast, low-cost", "gemini-2.5-flash-lite"),
        ],
        "deep": [
            ("Gemini 3.1 Pro - Reasoning-first, complex workflows", "gemini-3.1-pro-preview"),
            ("Gemini 3 Flash - Next-gen fast", "gemini-3-flash-preview"),
            ("Gemini 2.5 Pro - Stable pro model", "gemini-2.5-pro"),
            ("Gemini 2.5 Flash - Balanced, stable", "gemini-2.5-flash"),
        ],
    },
    "xai": {
        "quick": [
            ("Grok 4.1 Fast (Non-Reasoning) - Speed optimized, 2M ctx", "grok-4-1-fast-non-reasoning"),
            ("Grok 4 Fast (Non-Reasoning) - Speed optimized", "grok-4-fast-non-reasoning"),
            ("Grok 4.1 Fast (Reasoning) - High-performance, 2M ctx", "grok-4-1-fast-reasoning"),
        ],
        "deep": [
            ("Grok 4 - Flagship model", "grok-4-0709"),
            ("Grok 4.1 Fast (Reasoning) - High-performance, 2M ctx", "grok-4-1-fast-reasoning"),
            ("Grok 4 Fast (Reasoning) - High-performance", "grok-4-fast-reasoning"),
            ("Grok 4.1 Fast (Non-Reasoning) - Speed optimized, 2M ctx", "grok-4-1-fast-non-reasoning"),
        ],
    },
    "openrouter": {
        "quick": [
            ("Kimi K2.5 - $0.42/1M, #1 agentic+tool use", "moonshotai/kimi-k2.5"),
            ("Kimi K2 0905 - $0.40/1M, strong agentic", "moonshotai/kimi-k2-0905"),
            ("Qwen3 235B A22B - $0.22/1M, 235B MoEn", "qwen/qwen3-235b-a22b"),
            ("Qwen 2.5 72B - $0.13/1M, reliable 72B", "qwen/qwen-2.5-72b-instruct"),
            ("Qwen3.6 Plus Preview (free) - 1M ctx", "qwen/qwen3.6-plus-preview:free"),
            ("NVIDIA Nemotron 120B (free)", "nvidia/nemotron-3-super-120b-a12b:free"),
            ("NVIDIA Nemotron 3 Nano 30B (free)", "nvidia/nemotron-3-nano-30b-a3b:free"),
            ("Z.AI GLM 4.5 Air (free)", "z-ai/glm-4.5-air:free"),
        ],
        "deep": [
            ("Kimi K2 Thinking - $0.47/1M, 1T MoE reasoning+tool", "moonshotai/kimi-k2-thinking"),
            ("Kimi K2 - $0.57/1M, 1T MoE, SWE-bench 65.8%", "moonshotai/kimi-k2"),
            ("DeepSeek R1 - $0.70/1M, top reasoning, MMLU-Pro 84.9%", "deepseek/deepseek-r1"),
            ("Qwen3 Max - $0.78/1M, top Qwen", "qwen/qwen3-max"),
            ("Qwen3 235B A22B - $0.22/1M, 235B MoE", "qwen/qwen3-235b-a22b"),
            ("Qwen3.6 Plus Preview (free) - 1M ctx", "qwen/qwen3.6-plus-preview:free"),
            ("NVIDIA Nemotron 120B (free)", "nvidia/nemotron-3-super-120b-a12b:free"),
            ("NVIDIA Nemotron 3 Nano 30B (free)", "nvidia/nemotron-3-nano-30b-a3b:free"),
            ("Z.AI GLM 4.5 Air (free)", "z-ai/glm-4.5-air:free"),
        ],
    },
    "ollama": {
        "quick": [
            ("Qwen3:latest (8B, local)", "qwen3:latest"),
            ("GPT-OSS:latest (20B, local)", "gpt-oss:latest"),
            ("GLM-4.7-Flash:latest (30B, local)", "glm-4.7-flash:latest"),
        ],
        "deep": [
            ("GLM-4.7-Flash:latest (30B, local)", "glm-4.7-flash:latest"),
            ("GPT-OSS:latest (20B, local)", "gpt-oss:latest"),
            ("Qwen3:latest (8B, local)", "qwen3:latest"),
        ],
    },
}


def get_model_options(provider: str, mode: str) -> List[ModelOption]:
    """Return shared model options for a provider and selection mode."""
    return MODEL_OPTIONS[provider.lower()][mode]


def get_known_models() -> Dict[str, List[str]]:
    """Build known model names from the shared CLI catalog."""
    return {
        provider: sorted(
            {
                value
                for options in mode_options.values()
                for _, value in options
            }
        )
        for provider, mode_options in MODEL_OPTIONS.items()
    }
