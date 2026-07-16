from client import VercelAiSdkStreamHelperClient
client = VercelAiSdkStreamHelperClient()
print(client.join_chunks(["Hello ", "world", "!"]))