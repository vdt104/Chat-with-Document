from functools import partial
from .pinecone import build_retriever

# retriever_map = {
#     "pinecone_3": partial(build_retriever, k=3),
#     "pinecone_4": partial(build_retriever, k=4),
#     "pinecone_5": partial(build_retriever, k=5),
#     "pinecone_10": partial(build_retriever, k=10),
# }

retriever_map = {
    "pinecone_10": partial(build_retriever, k=10),
    "pinecone_11": partial(build_retriever, k=11),
}