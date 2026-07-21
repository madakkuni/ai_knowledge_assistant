from app.exceptions.splitter_exceptions import SplitterException
from app.ingestion.splitters.base_splitter import BaseSplitter
from app.ingestion.splitters.fixed_size_splitter import FixedSizeSplitter
from app.ingestion.splitters.text_splitter_config import TextSplitterConfig
from app.ingestion.splitters.faq_splitter import FAQSplitter


class SplitterFactory:

    @staticmethod
    def get_splitter(
        splitter_type: str,
        config: TextSplitterConfig
    ) -> BaseSplitter:

        splitter_type = splitter_type.lower()
        splitter_type = "faq"

        if splitter_type == "fixed":
            return FixedSizeSplitter(config)
        
        if splitter_type == "faq":
            return FAQSplitter()

        raise SplitterException(
            f"Unsupported splitter type: {splitter_type}"
        )