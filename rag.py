import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Refunds are allowed within 30 days of purchase.",
    "Shipping takes 5-7 days for standard delivery.",
    "Express shipping takes 1-2 days.",
    "Use 'Forgot Password' to reset your password.",
    "Orders can be tracked using tracking ID."
]

embeddings = model.encode(documents)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def retrieve(query, k=2):
    q_vec = model.encode([query])
    _, indices = index.search(np.array(q_vec), k)
    return [documents[i] for i in indices[0]]