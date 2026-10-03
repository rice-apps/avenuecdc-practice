import os
from retell import Retell

client = Retell(
    api_key=os.environ.get("RETELL_API_KEY") 
)

agent_response = client.agent.create(
    response_engine={
        "llm_id": "",
        "type": "retell-llm",
    },
    voice_id="minimax-Cimo"
)

