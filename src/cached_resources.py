import guardrails as gd
import streamlit as st

from src.models import LLMResponse
from src.prompt import PROMPT


@st.cache_resource
def get_guard() -> gd.Guard:
    """
    Create an output guard using GuardRails.
    """
    return gd.Guard.from_pydantic(output_class=LLMResponse, prompt=PROMPT)
