import re
from collections import defaultdict
from openai import OpenAI
client = OpenAI()

def load_book(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
conversation_history = [
    {"role": "system", "content":""""
You are a system that will receive mulitple prompts. Each prompt should be treated as a seperate request within the same conversation context. 
You are an expert audiobook narrator given the following chunk identify who the 'speaker' is. It could be one of the following characters or a narrator.

Darrow au Andromedus of Lykos, a.k.a. the "Reaper" and the "Morning Star": a Red physically remade into a Gold to infiltrate and destroy the Society. The former leader of the revolution known as "The Rising", Darrow is the ArchImperator of the new Solar Republic.
Virginia au Augustus, a.k.a. "Mustang" (Gold): daughter of the former ArchGovernor of Mars, Darrow's wife, and mother of their son Pax. She serves the new Solar Republic as its elected Sovereign.
Sevro au Barca, a.k.a. "Goblin" and "Ares" (Gold): Darrow's best friend and second-in-command.
Victra au Barca (Gold): Darrow's former lieutenant, Sevro's wife, and daughter of the Julii family.
Cassius au Bellona (Gold): Darrow's close friend-turned-bitter enemy, known as the Morning Knight under the previous Sovereign, Octavia au Lune. Though he and Darrow have reconciled, Cassius remains an independent freedom fighter far-removed from the Republic worlds.
Lysander au Lune (Gold): grandson and heir to Octavia au Lune. He has been raised and protected by Cassius since the rise of the Republic.
Kavax au Telemanus (Gold): longtime ally to Virginia and Darrow, father of Daxo and the deceased Pax au Telemanus.
Niobe au Telemanus (Gold): Kavax's wife.
Daxo au Telemanus (Gold): son and heir to Kavax.
Thraxa au Telemanus (Gold): daughter of Kavax and Niobe.
Magnus au Grimmus, a.k.a. the "Ash Lord" (Gold): former ArchImperator and supreme commander of the Sovereign's fleet, he and his allies are the remaining holdouts against the new Republic.
Atalantia au Grimmus (Gold): the Ash Lord's daughter, sister to Aja au Grimmus and Moira au Grimmus.
Julia au Bellona (Gold): Cassius' estranged mother and Darrow's enemy, a supporter of the Ash Lord, widow of Tiberius au Bellona.
Romulus au Raa (Gold): Sovereign of the Rim Dominion, home of a collection of Gold families who seceded from the Society in the distant past.
Dido au Raa (Gold): Romulus' wife.
Seraphina au Raa (Gold): daughter of Romulus and Dido.
Diomedes au Raa, a.k.a. the "Storm Knight" (Gold): son of Romulus and Dido.
Marius au Raa (Gold): Quaestor, and son of Romulus and Dido.
Alexandar au Arcos (Gold), Howler and eldest grandson of Lorn au Arcos, the former Rage Knight and Darrow's mentor.
Pax (Gold): son of Darrow and Virginia.
Electra au Barca (Gold): eldest daughter of Sevro and Victra.
Apollonius au Valii-Rath (Gold): imprisoned brother of Tactus.
Regulus ag Sun, a.k.a. "Quicksilver" (Silver): the richest man in the known worlds and co-founder of the Sons of Ares. He has almost singlehandedly rebuilt Luna following the fall of the Society.
Sefi (Obsidian): Queen of the Obsidian Valkyries, and sister to fallen hero Ragnar. She is a longtime ally of Darrow's, but now realizes the toll his war has taken on her people.
Wulfgar the Whitetooth (Obsidian): hero of the rising, now ArchWarden of the Republic.
Holiday ti Nakamura (Gray): Legionnaire and Darrow's deputy, formerly a mole for the Sons of Ares.
Ephraim ti Horn (Gray): former son of Ares whose fiancé, Holiday's brother Trigg, was killed rescuing Darrow and Victra from imprisonment. Ephraim works as a freelance thief.
Volga Fjorgan (Obsidian): one of Ephraim's associates.
Dano (Red): one of Ephraim's associates.
"Dancer" (Red): Darrow's mentor in the Sons of Ares, now a powerful senator in the Republic and leader of the Vox Populi faction.
Rhonna (Red): daughter of Darrow's brother, and one of his lancers.
Lyria of Lagalos (Red): Gamma Red from Mars who saves the life of Kavax au Telemanus, and joins his household.
Cyra si Lamensis (Green): locksmith and one of Ephraim's associates.
Pytha (Blue): pilot and companion of Cassius and Lysander.
Mickey (Violet): carver who remade Darrow."""
},
        {"role": "user", "content": "Prepare to receive multiple prompts for processing."}
    
]
    
def intial_prompt():
    response = client.chat.completions.create(
        model ="gpt-4o-mini-2024-07-18",
        messages=conversation_history)
    return response.choices[0].message.content
    
def chunk_text(text, chunk_size=3000):
    words = text.split();
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks


def identify_characters_and_narrator(chunk, conversation_history):
    conversation_history.append({"role": "system", "content": f"You are an expert audiobook narrator given the following chunk identify who the 'speaker' is for the chunk. is a narator or some character your job is identify each line and assign the line to a character or a narator.  :\n\n{chunk}"})
    response = client.chat.completions.create(
        model ="gpt-4o-mini-2024-07-18",
        messages= conversation_history
    )
    
    return response.choices[0].message.content

book_text = load_book('output.txt')
initResult = intial_prompt()

text_chunks = chunk_text(book_text)
print(len(text_chunks))
character_info = [identify_characters_and_narrator(chunk, conversation_history) for chunk in text_chunks]
print(character_info)
# characters = extract_characters(character_info)
# print(characters)