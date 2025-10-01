import json
import logging
from typing import Any

from sentient_agent_framework.interface.agent import AbstractAgent
from sentient_agent_framework.interface.request import Query
from sentient_agent_framework.interface.session import Session
from sentient_agent_framework.interface.response_handler import ResponseHandler

from .prompt_builder import PromptBuilder
from .model_client import ModelClient

logger = logging.getLogger(__name__)

class Agent(AbstractAgent):
    def __init__(self, name: str = "Mr.Recipe"):
        super().__init__(name)
        self.prompt_builder = PromptBuilder()
        self.model_client = ModelClient()

    async def assist(self, session: Session, query: Query, response_handler: ResponseHandler) -> None:
        # get prompt from Query
        prompt = getattr(query, "prompt", "") or ""
        if not prompt:
            await response_handler.emit_error("Empty prompt", details={"field": "prompt"})
            await response_handler.complete()
            return

        # collect prompt (can add context if necessary)
        messages = self.prompt_builder.build(prompt)

        await response_handler.emit_text_block(
            "SEARCH", "Thinking about your query..."
        )

        try:
            model_response = await self.model_client.generate(messages)
        except Exception as exc:
            logger.error("Model call failed with an unexpected exception.", exc_info=True)
            await response_handler.emit_error(
                "An internal error occurred while generating the response. Please try again.", 
                details={"stage": "call_model", "error_type": type(exc).__name__}
            )
            await response_handler.complete()
            return

        # Sending the result to the framework
        try:
            # respond(event_name, payload) — framework expects Mapping or str
            await response_handler.respond("response", model_response)
        except Exception as exc:
            logger.error("Respond call failed unexpectedly.", exc_info=True)
            await response_handler.emit_error(
                "An internal error occurred while communicating the result.", 
                details={"stage": "respond", "error_type": type(exc).__name__}
            )
            await response_handler.complete()
