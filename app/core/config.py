import os

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover
    load_dotenv = None


if load_dotenv is not None:
    load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.llm_provider = os.getenv("LLM_PROVIDER", "openai_compatible")
        self.llm_base_url = os.getenv(
            "LLM_BASE_URL",
            "https://open.bigmodel.cn/api/paas/v4/",
        )
        self.llm_api_key = (
            os.getenv("LLM_API_KEY")
            or os.getenv("ZHIPUAI_API_KEY")
            or os.getenv("ZHIPU_API_KEY")
            or os.getenv("OPENAI_API_KEY")
            or "EMPTY"
        )
        self.llm_model = os.getenv("LLM_MODEL", "glm-4-flash")

    @property
    def supports_openai_compatible(self) -> bool:
        return self.llm_provider == "openai_compatible"


settings = Settings()
