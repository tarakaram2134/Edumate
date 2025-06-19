import os
from datetime import datetime
from qa_chain import query_notes
from llm_generate import generate_answer

# Step 1: Ask a question
question = "What is a Graph?"

# Step 2: Get context and source docs
context, sources = query_notes(question)

# Step 3: Generate answer
answer = generate_answer(context, question)

# Step 4: Print to terminal
print("\n📘 Retrieved Content:\n", context)
print("\n🤖 Generated Answer:\n", answer)

# Step 5: Save to log
os.makedirs("logs", exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

log_entry = f"""## 📅 {timestamp}
**Q:** {question}

**📚 Source(s):** {', '.join(sources) if sources else 'N/A'}

**🤖 Answer:** {answer}

---

"""

with open("logs/qa_log.md", "a", encoding="utf-8") as f:
    f.write(log_entry)
