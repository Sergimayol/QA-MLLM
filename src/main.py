from preprocessor.input_analysis import InputAnalyzer
from qa import qa_model
import torch

FILE_PATH = "../file.test.txt"


def main():
    print("Hello World!")
    input_analyzer = InputAnalyzer(FILE_PATH)
    # print(input_analyzer.analyze())
    model = qa_model.QAModel(
        context=input_analyzer.analyze(),
        device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu"),
        model_name="deepset/bert-base-cased-squad2",
        tokenizer_name="deepset/bert-base-cased-squad2",
        pipeline_name="question-answering",
    )
    print(model)

    print(model.answer_question("What person works for an IT company?"))


if __name__ == "__main__":
    main()
