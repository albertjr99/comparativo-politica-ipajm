"""
Módulo para comparação de documentos e análise de diferenças.
"""
from difflib import SequenceMatcher, unified_diff
from typing import Dict, List, Tuple
import re


class DocumentComparator:
    """Classe para comparar documentos e identificar diferenças."""

    @staticmethod
    def calculate_similarity(text1: str, text2: str) -> float:
        """
        Calcula similaridade entre dois textos (0 a 1).

        Args:
            text1: Primeiro texto
            text2: Segundo texto

        Returns:
            float: Índice de similaridade (0-1)
        """
        return SequenceMatcher(None, text1, text2).ratio()

    @staticmethod
    def find_differences(text1: str, text2: str) -> List[str]:
        """
        Encontra diferenças linha por linha entre dois textos.

        Args:
            text1: Texto original
            text2: Texto modificado

        Returns:
            List de strings com as diferenças
        """
        lines1 = text1.splitlines()
        lines2 = text2.splitlines()

        diff = list(unified_diff(lines1, lines2, lineterm=''))
        return diff

    @staticmethod
    def compare_topics(topics1: Dict[str, str], topics2: Dict[str, str]) -> Dict[str, Dict]:
        """
        Compara tópicos entre dois documentos.

        Args:
            topics1: Dicionário de tópicos do documento 1
            topics2: Dicionário de tópicos do documento 2

        Returns:
            Dict com comparação de cada tópico
        """
        comparison = {}

        for topic in topics1.keys():
            text1 = topics1.get(topic, "")
            text2 = topics2.get(topic, "")

            similarity = DocumentComparator.calculate_similarity(text1, text2)

            comparison[topic] = {
                'texto_2025': text1,
                'texto_2026': text2,
                'similaridade': similarity,
                'status': DocumentComparator._get_status(similarity),
                'tem_alteracao': similarity < 0.95
            }

        return comparison

    @staticmethod
    def _get_status(similarity: float) -> str:
        """
        Retorna status baseado na similaridade.

        Args:
            similarity: Índice de similaridade

        Returns:
            str: Status da comparação
        """
        if similarity >= 0.95:
            return "Sem alterações significativas"
        elif similarity >= 0.7:
            return "Alterações moderadas"
        else:
            return "Alterações significativas"

    @staticmethod
    def highlight_changes(text1: str, text2: str) -> Tuple[str, str]:
        """
        Destaca mudanças entre dois textos.

        Args:
            text1: Texto original
            text2: Texto modificado

        Returns:
            Tupla com textos marcados com mudanças
        """
        matcher = SequenceMatcher(None, text1, text2)

        highlighted1 = []
        highlighted2 = []

        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == 'equal':
                highlighted1.append(text1[i1:i2])
                highlighted2.append(text2[j1:j2])
            elif tag == 'delete':
                highlighted1.append(f"**[REMOVIDO: {text1[i1:i2]}]**")
            elif tag == 'insert':
                highlighted2.append(f"**[ADICIONADO: {text2[j1:j2]}]**")
            elif tag == 'replace':
                highlighted1.append(f"**[ALTERADO: {text1[i1:i2]}]**")
                highlighted2.append(f"**[NOVO: {text2[j1:j2]}]**")

        return ''.join(highlighted1), ''.join(highlighted2)

    @staticmethod
    def extract_key_metrics(comparison: Dict[str, Dict]) -> Dict[str, any]:
        """
        Extrai métricas chave da comparação.

        Args:
            comparison: Dicionário de comparação

        Returns:
            Dict com métricas
        """
        total_topics = len(comparison)
        altered_topics = sum(1 for v in comparison.values() if v['tem_alteracao'])
        avg_similarity = sum(v['similaridade'] for v in comparison.values()) / total_topics if total_topics > 0 else 0

        return {
            'total_topicos': total_topics,
            'topicos_alterados': altered_topics,
            'topicos_sem_alteracao': total_topics - altered_topics,
            'similaridade_media': avg_similarity,
            'percentual_alteracao': (altered_topics / total_topics * 100) if total_topics > 0 else 0
        }
