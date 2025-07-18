from utils.file_parser import parse_documents

class IngestionAgent:
    def ingest(self, files, trace_id):
        parsed_docs = parse_documents(files)
        return {
            "sender": "IngestionAgent",
            "receiver": "RetrievalAgent",
            "type": "INGESTION_RESULT",
            "trace_id": trace_id,
            "payload": {"documents": parsed_docs}
        }
