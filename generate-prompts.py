#!/usr/bin/env python3
"""
Generate 10,000+ diverse prompts for image generation testing and add to prompts.json
"""

import json
import random
from pathlib import Path

# Base templates for generating diverse prompts
SUBJECTS = [
    "cat", "dog", "bird", "horse", "elephant", "lion", "tiger", "bear", "wolf", "fox",
    "person", "woman", "man", "child", "elderly person", "businessman", "artist", "chef", "doctor", "teacher",
    "tree", "flower", "rose", "sunflower", "cactus", "bonsai", "oak tree", "pine tree", "cherry blossom",
    "mountain", "forest", "beach", "desert", "valley", "canyon", "waterfall", "river", "lake", "ocean",
    "building", "house", "castle", "temple", "church", "skyscraper", "cabin", "mansion", "cottage", "tower",
    "car", "truck", "bicycle", "motorcycle", "airplane", "helicopter", "boat", "ship", "train", "bus",
    "robot", "dragon", "unicorn", "phoenix", "mermaid", "fairy", "elf", "dwarf", "wizard", "knight",
    "apple", "orange", "banana", "strawberry", "grape", "watermelon", "pineapple", "mango", "peach", "cherry",
    "laptop", "phone", "camera", "book", "guitar", "piano", "violin", "drum", "trumpet", "flute",
    "planet", "star", "moon", "sun", "comet", "asteroid", "galaxy", "nebula", "black hole", "constellation"
]

SETTINGS = [
    "in a forest", "on a beach", "in a city", "in the mountains", "in a desert", "underwater",
    "in space", "in a garden", "in a park", "on a street", "in a room", "in a studio",
    "at sunset", "at sunrise", "at night", "during the day", "at dawn", "at dusk",
    "in winter", "in spring", "in summer", "in autumn", "in the rain", "in the snow",
    "in a fantasy world", "in a futuristic city", "in medieval times", "in ancient Rome",
    "on Mars", "on the moon", "in a jungle", "in a cave", "on a cliff", "by a river",
    "in a valley", "on a hilltop", "in a field", "in a meadow", "in a clearing",
    "inside a castle", "inside a temple", "inside a spaceship", "inside a laboratory",
    "at the beach", "at the mountains", "at a lake", "at the ocean", "at a waterfall"
]

STYLES = [
    "photorealistic", "oil painting", "watercolor", "pencil sketch", "digital art",
    "anime style", "cartoon style", "3D render", "pixel art", "vector art",
    "abstract art", "surrealist style", "impressionist style", "cubist style", "art deco",
    "minimalist", "maximalist", "vintage photograph", "retro style", "cyberpunk style",
    "steampunk style", "gothic style", "baroque style", "renaissance style", "modern art",
    "pop art", "graffiti art", "street art", "concept art", "matte painting",
    "illustration", "comic book style", "manga style", "cinematic", "dramatic lighting",
    "soft lighting", "neon lighting", "natural lighting", "studio lighting", "golden hour"
]

QUALITIES = [
    "highly detailed", "ultra realistic", "8k resolution", "professional photography",
    "masterpiece", "award winning", "trending on artstation", "featured on pixiv",
    "stunning", "beautiful", "gorgeous", "elegant", "majestic", "epic",
    "dramatic", "atmospheric", "moody", "vibrant", "colorful", "monochrome",
    "high contrast", "soft focus", "sharp focus", "bokeh", "depth of field",
    "wide angle", "close-up", "macro photography", "aerial view", "bird's eye view",
    "cinematic composition", "rule of thirds", "symmetrical", "asymmetrical"
]

ADJECTIVES = [
    "red", "blue", "green", "yellow", "purple", "orange", "pink", "black", "white", "golden",
    "silver", "bronze", "copper", "emerald", "sapphire", "ruby", "amber", "violet", "turquoise",
    "large", "small", "tiny", "huge", "massive", "giant", "miniature", "colossal",
    "old", "ancient", "modern", "futuristic", "vintage", "antique", "new", "weathered",
    "beautiful", "elegant", "majestic", "grand", "magnificent", "stunning", "gorgeous",
    "dark", "bright", "dim", "glowing", "shimmering", "sparkling", "radiant", "luminous",
    "mysterious", "magical", "enchanted", "mystical", "ethereal", "surreal", "dreamlike",
    "peaceful", "serene", "calm", "tranquil", "quiet", "still", "silent",
    "busy", "crowded", "bustling", "lively", "vibrant", "energetic", "dynamic",
    "lonely", "isolated", "abandoned", "desolate", "empty", "barren", "deserted"
]

ACTIONS = [
    "sitting", "standing", "running", "walking", "flying", "swimming", "jumping",
    "sleeping", "resting", "playing", "working", "reading", "writing", "painting",
    "dancing", "singing", "playing music", "cooking", "eating", "drinking",
    "looking at camera", "looking away", "smiling", "laughing", "crying", "thinking",
    "meditating", "exercising", "stretching", "climbing", "exploring", "discovering",
    "creating", "building", "destroying", "fighting", "embracing", "celebrating"
]

WEATHER = [
    "sunny", "cloudy", "rainy", "snowy", "foggy", "misty", "stormy", "windy",
    "clear sky", "overcast", "partly cloudy", "thunderstorm", "blizzard", "drizzle"
]

TIMES = [
    "morning", "afternoon", "evening", "night", "midnight", "dawn", "dusk",
    "sunrise", "sunset", "golden hour", "blue hour", "twilight", "noon"
]

def generate_simple_prompts(count):
    """Generate simple subject-based prompts"""
    prompts = []
    for _ in range(count):
        subject = random.choice(SUBJECTS)
        prompts.append(f"a {subject}")
    return prompts

def generate_descriptive_prompts(count):
    """Generate prompts with adjectives and subjects"""
    prompts = []
    for _ in range(count):
        adj = random.choice(ADJECTIVES)
        subject = random.choice(SUBJECTS)
        prompts.append(f"a {adj} {subject}")
    return prompts

def generate_contextual_prompts(count):
    """Generate prompts with subjects in settings"""
    prompts = []
    for _ in range(count):
        subject = random.choice(SUBJECTS)
        setting = random.choice(SETTINGS)
        prompts.append(f"a {subject} {setting}")
    return prompts

def generate_action_prompts(count):
    """Generate prompts with subjects performing actions"""
    prompts = []
    for _ in range(count):
        subject = random.choice(SUBJECTS)
        action = random.choice(ACTIONS)
        prompts.append(f"a {subject} {action}")
    return prompts

def generate_styled_prompts(count):
    """Generate prompts with specific art styles"""
    prompts = []
    for _ in range(count):
        subject = random.choice(SUBJECTS)
        style = random.choice(STYLES)
        prompts.append(f"a {subject}, {style}")
    return prompts

def generate_complex_prompts(count):
    """Generate complex multi-element prompts"""
    prompts = []
    for _ in range(count):
        adj = random.choice(ADJECTIVES)
        subject = random.choice(SUBJECTS)
        action = random.choice(ACTIONS)
        setting = random.choice(SETTINGS)
        prompts.append(f"a {adj} {subject} {action} {setting}")
    return prompts

def generate_quality_prompts(count):
    """Generate prompts with quality descriptors"""
    prompts = []
    for _ in range(count):
        subject = random.choice(SUBJECTS)
        quality = random.choice(QUALITIES)
        prompts.append(f"a {subject}, {quality}")
    return prompts

def generate_weather_time_prompts(count):
    """Generate prompts with weather and time"""
    prompts = []
    for _ in range(count):
        subject = random.choice(SUBJECTS)
        weather = random.choice(WEATHER)
        time = random.choice(TIMES)
        prompts.append(f"a {subject} during {weather} weather at {time}")
    return prompts

def generate_ultra_detailed_prompts(count):
    """Generate highly detailed prompts with multiple elements"""
    prompts = []
    for _ in range(count):
        adj1 = random.choice(ADJECTIVES)
        adj2 = random.choice(ADJECTIVES)
        subject = random.choice(SUBJECTS)
        action = random.choice(ACTIONS)
        setting = random.choice(SETTINGS)
        style = random.choice(STYLES)
        quality = random.choice(QUALITIES)
        prompts.append(f"{adj1} {adj2} {subject} {action} {setting}, {style}, {quality}")
    return prompts

def generate_scenario_prompts(count):
    """Generate complete scene descriptions"""
    prompts = []
    scenarios = [
        "a cozy coffee shop interior with people reading books",
        "a bustling marketplace with vendors and colorful stalls",
        "a peaceful zen garden with koi pond and stone path",
        "a high-tech laboratory with holographic displays",
        "a medieval tavern with wooden tables and fireplace",
        "a futuristic cityscape with flying vehicles",
        "a mystical forest clearing with glowing mushrooms",
        "a desert oasis with palm trees and clear water",
        "a mountain temple at sunrise with prayer flags",
        "an underwater coral reef with tropical fish"
    ]
    for _ in range(count):
        base_scenario = random.choice(scenarios)
        style = random.choice(STYLES)
        prompts.append(f"{base_scenario}, {style}")
    return prompts

def main():
    """Generate prompts and update prompts.json"""
    print("Generating 10,000+ prompts...")
    
    # Generate different categories of prompts
    all_prompts = []
    all_prompts.extend(generate_simple_prompts(500))
    all_prompts.extend(generate_descriptive_prompts(1000))
    all_prompts.extend(generate_contextual_prompts(1500))
    all_prompts.extend(generate_action_prompts(1000))
    all_prompts.extend(generate_styled_prompts(1500))
    all_prompts.extend(generate_complex_prompts(2000))
    all_prompts.extend(generate_quality_prompts(1000))
    all_prompts.extend(generate_weather_time_prompts(800))
    all_prompts.extend(generate_ultra_detailed_prompts(1500))
    all_prompts.extend(generate_scenario_prompts(500))
    
    # Remove duplicates while preserving order
    seen = set()
    unique_prompts = []
    for prompt in all_prompts:
        if prompt not in seen:
            seen.add(prompt)
            unique_prompts.append(prompt)
    
    print(f"Generated {len(unique_prompts)} unique prompts")
    
    # Convert to required format
    prompt_objects = [{"positivePrompt": p} for p in unique_prompts]
    
    # Read existing prompts.json
    prompts_file = Path(__file__).parent / "prompts.json"
    with open(prompts_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Add new category
    data["text_to_image"]["generated_bulk_10k"] = prompt_objects
    
    # Write back to file
    with open(prompts_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully added {len(unique_prompts)} prompts to prompts.json")
    print(f"New category: text_to_image.generated_bulk_10k")

if __name__ == "__main__":
    main()
