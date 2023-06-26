import logging
from transformers import pipeline
from models import common

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class QAModel(common.Model):
    def __init__(
        self,
        context: str,
        device: str,
        model_name: str,
        tokenizer_name: str,
        pipeline_name: str,
    ) -> None:
        super().__init__(
            context=context,
            device=device,
            model_name=model_name,
            tokenizer_name=tokenizer_name,
            pipeline_name=pipeline_name,
        )

    def answer_question(self, question: str) -> dict:
        LOGGER.info(f"Answering question: {question}")
        if self.model is None:
            self.load_model()
        return self.model(question=question, context=self.context)


class SummarizationModel(common.Model):
    def __init__(
        self,
        context: str,
        device: str,
        model_name: str,
        tokenizer_name: str,
        pipeline_name: str,
        framework_name: str,
    ) -> None:
        super().__init__(
            context=context,
            device=device,
            model_name=model_name,
            tokenizer_name=tokenizer_name,
            pipeline_name=pipeline_name,
        )
        self.framework_name = framework_name
        self.min_length = 50

    def load_model(self) -> None:
        try:
            LOGGER.info("Loading model...")
            self.model = pipeline(
                self.pipeline_name,
                model=self.model_name,
                tokenizer=self.tokenizer_name,
                device=self.device,
                framework=self.framework_name,
            )
            LOGGER.info("Model loaded.")
        except Exception as e:
            LOGGER.error("Error loading model.")
            LOGGER.error(e)

    def summarize(self, max_length: int = 100) -> list[dict]:
        LOGGER.info(f"Summarizing text...")
        if self.model is None:
            self.load_model()
        return self.model(
            self.context, max_length=max_length, min_length=self.min_length
        )
