"""CLI application for the QA MLLM (Question 
Answering Multi Language Learning Model) application.
"""
from preprocessor.input_analysis import InputAnalyzer
from utils.helpers import Helpers
from utils.config import MODELS, EXIT_KEY
from models import model as AIModel


def load_models(input_analyzer: str, device: str) -> dict:
    qa_model = AIModel.QAModel(
        context=input_analyzer,
        device=device,
        model_name=MODELS["qa"]["model_name"],
        tokenizer_name=MODELS["qa"]["tokenizer_name"],
        pipeline_name=MODELS["qa"]["pipeline_name"],
    )

    summarization_model = AIModel.SummarizationModel(
        context=input_analyzer,
        device=device,
        model_name=MODELS["summarization"]["model_name"],
        tokenizer_name=MODELS["summarization"]["tokenizer_name"],
        pipeline_name=MODELS["summarization"]["pipeline_name"],
        framework_name=MODELS["summarization"]["framework_name"],
    )

    return {"qa": qa_model, "summarization": summarization_model}


def main():
    in_path, out_path, model_path, device = Helpers.get_app_args()
    confirmed_device = Helpers.get_device(device)
    input_analyzer = InputAnalyzer(in_path).analyze()
    if not input_analyzer:
        print(
            "Invalid input file, make sure it's a valid file and try again."
            f"\n Valid files are: {Helpers.ALLOWED_EXTENSIONS}"
        )
        return

    # Load the models
    models = load_models(input_analyzer, confirmed_device)
    qa_model = models["qa"]
    summarization_model = models["summarization"]

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
