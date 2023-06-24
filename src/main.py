from preprocessor.input_analysis import InputAnalyzer

FILE_PATH = "../file.test.txt"


def main():
    print("Hello World!")
    input_analyzer = InputAnalyzer(FILE_PATH)
    print(input_analyzer.analyze())


if __name__ == "__main__":
    main()
