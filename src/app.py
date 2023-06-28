import streamlit as st
from preprocessor.input_analysis import InputAnalyzer
from utils.helpers import Helpers
from utils.config import ALLOWED_EXTENSIONS, MODELS, MAX_INPUT_LENGTH
from models import model as AIModel

ICON_URL = "https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png"


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
    st.markdown(
        """
        <style>
            [data-testid=stSidebar] {
                background-color: #f0f2f6;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.image(ICON_URL, width=200)
        st.title("QA - MLLM")
        st.header("Question Answering using MLLM")
        st.info("This project application helps you to make questions about some data.")

    st.header("Upload")
    st.write("Import your context data file to be asked from")

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        data = uploaded_file.read()
        # Write the file to the filesystem
        path = Helpers.get_path_to_save_upload(uploaded_file.name)
        with open(path, "wb") as f:
            f.write(data)
        analyzed_input = InputAnalyzer(path).analyze()
        if not analyzed_input:
            st.error(
                "Invalid input file, make sure it's a valid file and try again."
                f"\n Valid files are: {ALLOWED_EXTENSIONS}"
            )
            return

        # Load the models
        models = load_models(Helpers.get_device(None))

        # Get the context for the summarization model
        context = get_context(analyzed_input, models["summarization"])

        qa_model: AIModel.QAModel = models["qa"]
        qa_model.context = context

        st.header("Ask questions")
        st.write(
            "Ask questions about the context data file and get the answers. "
            "The answers are composed by the awnser, the score and the start and "
            "end position of the answer in the context."
        )
        question = st.text_input("Question")
        if question:
            answer = qa_model.answer_question(question)
            st.write(answer)
        else:
            st.error("Please enter a question.")


if __name__ == "__main__":
    st.set_page_config(
        page_title="QA - MLLM",
        page_icon=ICON_URL,
        initial_sidebar_state="expanded",
    )
    main()
