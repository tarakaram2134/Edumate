from qa_chain import query_notes
from llm_generate import generate_answer

def get_response(user_question: str) -> tuple[str, str]:
    """
    Takes a user question, retrieves relevant context from notes,
    generates an answer using the LLM, and returns both.
    """
    context, sources = query_notes(user_question)
    answer = generate_answer(context, user_question)
    return answer, context
