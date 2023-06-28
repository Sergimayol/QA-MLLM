"""CLI application for the QA MLLM (Question 
Answering Multi Language Learning Model) application.
"""
from preprocessor.input_analysis import InputAnalyzer
from utils.helpers import Helpers
from utils.config import MODELS, EXIT_KEY, MAX_INPUT_LENGTH, ALLOWED_EXTENSIONS
from models import model as AIModel


def load_models(device: str) -> dict[str, any]:
    qa_model = AIModel.QAModel(
        context=None,
        device=device,
        model_name=MODELS["qa"]["model_name"],
        tokenizer_name=MODELS["qa"]["tokenizer_name"],
        pipeline_name=MODELS["qa"]["pipeline_name"],
    )

    summarization_model = AIModel.SummarizationModel(
        context=None,
        device=device,
        model_name=MODELS["summarization"]["model_name"],
        tokenizer_name=MODELS["summarization"]["tokenizer_name"],
        pipeline_name=MODELS["summarization"]["pipeline_name"],
        framework_name=MODELS["summarization"]["framework_name"],
    )

    return {"qa": qa_model, "summarization": summarization_model}


def get_context(analyzed_input: str, model: AIModel.SummarizationModel) -> str:
    # If the input is too long, summarize it
    if len(analyzed_input) > MAX_INPUT_LENGTH:
        model.context = analyzed_input
        summarized_input = model.summarize(MAX_INPUT_LENGTH)
        return summarized_input

    return analyzed_input


def main():
    in_path, model_path, device, record = Helpers.get_app_args()
    confirmed_device = Helpers.get_device(device)
    analyzed_input = InputAnalyzer(in_path).analyze()
    if not analyzed_input:
        print(
            "Invalid input file, make sure it's a valid file and try again."
            f"\n Valid files are: {ALLOWED_EXTENSIONS}"
        )
        return

    # Load the models
    models = load_models(confirmed_device)

    # Get the context for the QA model
    context = get_context(analyzed_input, models["summarization"])

    qa_model: AIModel.QAModel = models["qa"]
    qa_model.context = context

    print(f"Type {EXIT_KEY} to quit the application.")
    # Main loop event
    while True:
        question = input("Ask a question: ")
        if question == EXIT_KEY:
            break

        answer = qa_model.answer_question(question)
        print(answer)


if __name__ == "__main__":
    main()
