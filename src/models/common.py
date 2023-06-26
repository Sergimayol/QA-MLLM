"""This file contains the common code for the models, basically is the 
core of the models used in this application.
"""
import logging
from transformers import pipeline

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Model:
    def __init__(
        self,
        context: str,
        device: str,
        model_name: str,
        tokenizer_name: str,
        pipeline_name: str,
    ) -> None:
        self.context = context
        self.device = device
        self.model_name = model_name
        self.tokenizer_name = tokenizer_name
        self.pipeline_name = pipeline_name
        self.model = None

    def load_model(self) -> None:
        try:
            LOGGER.info("Loading model...")
            self.model = pipeline(
                self.pipeline_name,
                model=self.model_name,
                tokenizer=self.tokenizer_name,
                device=self.device,
            )
            LOGGER.info("Model loaded.")
        except Exception as e:
            LOGGER.error("Error loading model.")
            LOGGER.error(e)

    def __str__(self) -> str:
        MAX = 25
        print_context = (
            self.context[:MAX] + "..."
            if len(self.context.split(" ")) > MAX
            else self.context
        )
        return (
            f"Model(context={print_context}, device={self.device}, "
            f"model_name={self.model_name}, tokenizer_name={self.tokenizer_name}, "
            f"pipeline_name={self.pipeline_name})"
        )
