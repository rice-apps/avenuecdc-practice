import os
from dotenv import load_dotenv
from flask import Flask, request
from retell import Retell
from twilio.twiml.voice_response import VoiceResponse

load_dotenv()

app = Flask(__name__)
retell = Retell(api_key=os.environ["RETELL_API_KEY"])
AGENT_ID = os.environ["AGENT_ID"]

@app.post("/voice")
def voice():
    call = retell.call.register_phone_call(
        agent_id=os.environ["AGENT_ID"],
        from_number=request.form.get("From"),
        to_number=request.form.get("To"),
        direction="inbound",
    )
    resp = VoiceResponse()
    resp.dial().sip(f"sip:{call.call_id}@sip.retellai.com;transport=tcp")
    return str(resp), 200, {"Content-Type": "text/xml"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5002)))