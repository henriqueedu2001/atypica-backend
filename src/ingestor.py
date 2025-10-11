from langchain_community.document_loaders import PyPDFLoader

class Ingestor:
    """
    A class for ingesting and extracting raw text content from a PDF file.

    This class is designed to load evaluation, test, or exam PDFs and convert them
    into plain text that can later be processed by other components such as
    chunkers, retrievers, or embedding models.

    Attributes:
        file_path (str): The path to the PDF file to be ingested.
        raw_text (str): The concatenated text content extracted from all pages of the PDF.

    Example:
        >>> from ingestor import Ingestor
        >>> ingestor = Ingestor('tests/sample_exam.pdf')
        >>> print(ingestor.raw_text[:500])
        'Question 1: Define the main components of a neural network...'
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.raw_text: str = None
        self.load()
        return
    
    
    def load(self):
        """
        Load the PDF file and extract its text content.

        This method uses `PyPDFLoader` to parse the PDF file page by page,
        concatenating all page texts into a single string stored in `self.raw_text`.

        Example:
            >>> ingestor = Ingestor('sample.pdf')
            >>> ingestor.load()
            >>> len(ingestor.raw_text)
            8453

        Side effects:
            Updates `self.raw_text` with the concatenated text from all PDF pages.
        """
        loader = PyPDFLoader(self.file_path)
        documents = loader.load()
        self.raw_text = ''.join([page.page_content for page in documents])