from app.exceptions.splitter_exceptions import SplitterException
from app.ingestion.splitters.base_splitter import BaseSplitter
from app.ingestion.splitters.fixed_size_splitter import FixedSizeSplitter
from app.ingestion.splitters.text_splitter_config import TextSplitterConfig


class SplitterFactory:

    @staticmethod
    def get_splitter(
        splitter_type: str,
        config: TextSplitterConfig
    ) -> BaseSplitter:

        splitter_type = splitter_type.lower()

        if splitter_type == "fixed":
            return FixedSizeSplitter(config)

        raise SplitterException(
            f"Unsupported splitter type: {splitter_type}"
        )