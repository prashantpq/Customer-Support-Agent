from dotenv import load_dotenv
import os
import asyncio

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, RoomOutputOptions

from livekit.plugins import google, cartesia, deepgram, silero, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel

from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message

load_dotenv()

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
assistant = pc.assistant.Assistant(assistant_name=os.environ["ASSISTANT_NAME"])

from livekit.agents.llm import function_tool

@function_tool
async def ask_knowledge_base(question: str) -> str:
    """Query the Pinecone Assistant knowledge base for information."""
    msg = Message(role="user", content=question)
    resp = assistant.chat(messages=[msg])
    return resp.message.content

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=(
                "You are an iPop customer service AI assistant. "
                "Use the 'ask_knowledge_base' tool for any iPop-related questions. "
                "Keep responses conversational and helpful. "
                "Format numbers and units naturally for speech — say 'five hundred and twelve gigabytes' instead of 'five one two GB', "
                "'one hundred and twenty-eight gigabytes' instead of 'one two eight GB', "
                "and 'one terabyte' instead of 'one TB'."
            ),
            tools=[ask_knowledge_base],
        )

async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=deepgram.STT(model="nova-3", language="multi"),
        llm=google.LLM(model="gemini-1.5-flash"),
        tts=cartesia.TTS(
            model="sonic-2",
            voice="f786b574-daa5-4673-aa0c-cbe3e8534c02"
        ),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
            close_on_disconnect=False,
        ),
        room_output_options=RoomOutputOptions(
            audio_enabled=True,
        ),
    )

    await session.generate_reply(
        instructions="Greet the user as an iPop customer service representative. Speak English."
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))

