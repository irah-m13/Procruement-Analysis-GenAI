class PromptTemplates:
    """
    A collection of reusable prompt templates for AI services.
    """

    @staticmethod
    def summary_prompt():
        """
        Returns a template for generating a summary.
        """
        return (
            "Summarize the following content in bullet points, "
            "focusing on key information and insights."
        )

    @staticmethod
    def question_generation_prompt():
        """
        Returns a template for generating questions from content.
        """
        return (
            "Generate a list of questions that could be asked "
            "based on the following content."
        )

    @staticmethod
    def document_comparison_prompt():
        """
        Returns a template for comparing two documents.
        """
        return (
            "Compare the two provided documents and highlight the similarities, "
            "differences, and key points in bullet format."
        )

    @staticmethod
    def detailed_explanation_prompt():
        """
        Returns a template for providing detailed explanations.
        """
        return (
            "Explain the following content in detail, ensuring clarity "
            "and breaking down complex concepts into simpler terms."
        )
