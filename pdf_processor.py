"""
Módulo para processamento e extração de texto de arquivos PDF.
"""
import pdfplumber
from typing import Dict, List
import re


class PDFProcessor:
    """Classe para processar e extrair informações de PDFs."""

    @staticmethod
    def extract_text(pdf_file) -> str:
        """
        Extrai todo o texto de um arquivo PDF.

        Args:
            pdf_file: Arquivo PDF carregado

        Returns:
            str: Texto extraído do PDF
        """
        text = ""
        try:
            with pdfplumber.open(pdf_file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            raise Exception(f"Erro ao processar PDF: {str(e)}")

        return text

    @staticmethod
    def extract_topics(text: str, topics: List[str]) -> Dict[str, str]:
        """
        Extrai conteúdo relacionado a tópicos específicos do texto.

        Args:
            text: Texto completo do documento
            topics: Lista de tópicos a serem buscados

        Returns:
            Dict com tópicos e seus conteúdos
        """
        results = {}
        text_lower = text.lower()

        for topic in topics:
            topic_lower = topic.lower()
            # Procura pelo tópico e extrai contexto ao redor
            pattern = r'(.{0,500}' + re.escape(topic_lower) + r'.{0,500})'
            matches = re.findall(pattern, text_lower, re.IGNORECASE | re.DOTALL)

            if matches:
                # Une todos os matches encontrados
                results[topic] = "\n\n".join(set(matches))
            else:
                results[topic] = f"Tópico '{topic}' não encontrado no documento."

        return results

    @staticmethod
    def count_pages(pdf_file) -> int:
        """
        Conta o número de páginas de um PDF.

        Args:
            pdf_file: Arquivo PDF

        Returns:
            int: Número de páginas
        """
        try:
            with pdfplumber.open(pdf_file) as pdf:
                return len(pdf.pages)
        except:
            return 0
