"""Entry file for 'testing' the application.
"""
import torch
from preprocessor.input_analysis import InputAnalyzer
from models import model as AIModel
from utils.config import MODELS, DEBUG
from utils.helpers import Helpers

FILE_PATH = "../file.test.txt"


def main():
    in_path, out_path, model_path, device = Helpers.get_app_args()
    if DEBUG:
        in_path = FILE_PATH

    input_analyzer = InputAnalyzer(in_path)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # print(input_analyzer.analyze())

    model = AIModel.QAModel(
        context=input_analyzer.analyze(),
        device=device,
        model_name="deepset/bert-base-cased-squad2",
        tokenizer_name="deepset/bert-base-cased-squad2",
        pipeline_name="question-answering",
    )
    print(model)
    print(model.answer_question("What person works for an IT company?"))

    model = AIModel.SummarizationModel(
        context=input_analyzer.analyze(),
        device=device,
        model_name=MODELS["summarization"]["model_name"],
        tokenizer_name=MODELS["summarization"]["tokenizer_name"],
        pipeline_name=MODELS["summarization"]["pipeline_name"],
        framework_name=MODELS["summarization"]["framework_name"],
    )
    print(model)
    print(model.summarize(300))


if __name__ == "__main__":
    main()
