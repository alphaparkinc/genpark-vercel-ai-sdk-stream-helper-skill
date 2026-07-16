class VercelAiSdkStreamHelperClient:
    def join_chunks(self, stream_chunks: list[str]) -> dict:
        return {"joined_text": "".join(stream_chunks)}