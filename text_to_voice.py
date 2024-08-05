from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="""
THE FURY SILENT, SHE WAITS FOR the sky to fall, standing upon an island of volcanic
the sounds, a flapping banner of war held in her lover’s hand and the warm waves
that kiss her steel boots. Her heart is heavy. Her spirit wild. Peerless knights
tower behind her. Salt spray beads on their family crests—emerald centaurs,
screaming eagles, gold sphinxes, and the crowned skull of her father’s grim
house. Her golden eyes look to the heavens. Waiting. The water heaves in.
Out. The heartbeat of her silence.

THE CITY
Tyche, the jewel of Mercury, hunches in fear between the mountains and the
sun. Her famed glass and limestone spires are dark. The Ancestor Bridge is
empty. Here, Lorn au Arcos wept as a young man when
he saw the messenger
planet at sunset for the first time. Now, trash rolls through her streets, pushed
by salty summer wind. Gone are the calls of the fishmongers at the wharf.
Gone are the patter of pedestrian feet on the cobbles and the rumble of aircars
and the laughter of the lowColor children who jump from the bridges into the
waves on scorching summer days when the Trasmian sea winds are
still. The
city is quiet, its wealthy already gone to desert mountain retreats or
"""
)

response.stream_to_file(speech_file_path)