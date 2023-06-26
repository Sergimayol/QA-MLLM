import argparse
import torch


class Helpers:
    def __init__(self):
        pass

    @staticmethod
    def get_device(device: str) -> str:
        if device == "cpu" or device == "cuda":
            return device

        if not torch.cuda.is_available():
            return "cpu"

        # Get all the devices that torch sees
        devices = [torch.device(f"cuda:{i}") for i in range(torch.cuda.device_count())]
        # Get the first device
        device = devices[0]
        return device

    @staticmethod
    def get_app_args() -> tuple:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--input",
            "-i",
            type=str,
            required=True,
            help="Path to the input file (text file, pdf, docx, images, etc.)",
        )
        parser.add_argument(
            "--output",
            "-o",
            type=str,
            required=False,
            help="Path to the output video file",
        )
        parser.add_argument(
            "--model",
            "-m",
            type=str,
            required=False,
            help="Path to the model file",
        )
        parser.add_argument(
            "--device",
            "-d",
            type=str,
            required=False,
            help="Device to use (cpu or cuda), default will be cuda if available",
        )

        args = parser.parse_args()
        return args.input, args.output, args.model, args.device
