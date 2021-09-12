#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
	"uuid": "BBEE694E-595C-48B3-9F1C-B430A78146D4",
	"name": "Dragon of the mount",
	"creator": "Twine",
	"creatorVersion": "2.3.14",
	"schemaName": "Harlowe 3 to JSON",
	"schemaVersion": "0.0.6",
	"createdAtMs": 1631402522074,
	"passages": [
		{
			"name": "The Altar",
			"tags": "",
			"id": "1",
			"text": "You find yourself in a large chamber carved from stone dimly lit by an array of softly glowing gemstones implanted into the ceiling and walls in regular patterns. You stand atop an altar amidst a ring of fading runes. Infront of you, daylight can be seen shining through a narrow tunnel. It appears to the only way forward.\n\n[[FORWARD->The Crossroads]]",
			"links": [
				{
					"linkText": "FORWARD",
					"passageName": "The Crossroads",
					"original": "[[FORWARD->The Crossroads]]"
				}
			],
			"hooks": [],
			"cleanText": "You find yourself in a large chamber carved from stone dimly lit by an array of softly glowing gemstones implanted into the ceiling and walls in regular patterns. You stand atop an altar amidst a ring of fading runes. Infront of you, daylight can be seen shining through a narrow tunnel. It appears to the only way forward."
		},
		{
			"name": "The Crossroads",
			"tags": "",
			"id": "2",
			"text": "You are now in a clearing  surrounded by trees, sunlight peaks through the branches and a pleasant breeze dances through the leaves. The tunnel you emerged from is gone, in the center of the clearing a wooden sign stands out from the dirt that says \n“Survive these challenges three oh traveler mine, and slay the dragon of the mountain, only then will you be allowed to return home.”\nFour paths lay around you leading to a mountain, a grassy plane, a desert, and a thicket.\n\n[[NORTH->The Mountain]]\n[[West->The Desert]]\n[[East->The Grassy plane]]\n[[South->The Thicket]]",
			"links": [
				{
					"linkText": "NORTH",
					"passageName": "The Mountain",
					"original": "[[NORTH->The Mountain]]"
				},
				{
					"linkText": "WEST",
					"passageName": "The Desert",
					"original": "[[West->The Desert]]"
				},
				{
					"linkText": "EAST",
					"passageName": "The Grassy plane",
					"original": "[[East->The Grassy plane]]"
				},
				{
					"linkText": "SOUTH",
					"passageName": "The Thicket",
					"original": "[[South->The Thicket]]"
				}
			],
			"hooks": [],
			"cleanText": "You are now in a clearing  surrounded by trees, sunlight peaks through the branches and a pleasant breeze dances through the leaves. The tunnel you emerged from is gone, in the center of the clearing a wooden sign stands out from the dirt that says \n“Survive these challenges three oh traveler mine, and slay the dragon of the mountain, only then will you be allowed to return home.”\nFour paths lay around you leading to a mountain, a grassy plane, a desert, and a thicket."
		},
		{
			"name": "The Desert",
			"tags": "",
			"id": "3",
			"text": "Dunes of sand and scorching sun stretch out as far as the eye can see, you find a water skin at your feet and a stone path stretching out before you.\n\n[[BACK->The Crossroads]] \n[[FORWARD->The old man]]",
			"links": [
				{
					"linkText": "BACK",
					"passageName": "The Crossroads",
					"original": "[[BACK->The Crossroads]]"
				},
				{
					"linkText": "FORWARD",
					"passageName": "The old man",
					"original": "[[FORWARD->The old man]]"
				}
			],
			"hooks": [],
			"cleanText": "Dunes of sand and scorching sun stretch out as far as the eye can see, you find a water skin at your feet and a stone path stretching out before you."
		},
		{
			"name": "The Mountain",
			"tags": "",
			"id": "4",
			"text": "The mountain path is long and winding full of narrow passes and craggy cliffs that spell certain doom with but one wrong step. After a time you come to another sign:\n“Beyond here be the dragon, king of the mount.”\n\n[[FORWARD->The Dragon]]\n[[BACK->The Crossroads]]",
			"links": [
				{
					"linkText": "FIGHT",
					"passageName": "The Dragon",
					"original": "[[FIGHT->The Dragon]]"
				},
				{
					"linkText": "BACK",
					"passageName": "The Crossroads",
					"original": "[[BACK->The Crossroads]]"
				}
			],
			"hooks": [],
			"cleanText": "The mountain path is long and winding full of narrow passes and craggy cliffs that spell certain doom with but one wrong step. After a time you come to another sign:\n“Beyond here be the dragon, king of the mount.”"
		},
		{
			"name": "The Grassy plane",
			"tags": "",
			"id": "5",
			"text": "A worn path leads to a grassy plane that seems to stretch out as far as your eyes can see. The weather is comfortable, and the path is level. The walk is easy, and you see a boulder jutting out from the grass in the distance.\n\n[[FORWARD->The Boulder]]\n[[BACK->The Crossroads]]",
			"links": [
				{
					"linkText": "FORWARD",
					"passageName": "The Boulder",
					"original": "[[FORWARD->The Boulder]]"
				},
				{
					"linkText": "BACK",
					"passageName": "The Crossroads",
					"original": "[[BACK->The Crossroads]]"
				}
			],
			"hooks": [],
			"cleanText": "A worn path leads to a grassy plane that seems to stretch out as far as your eyes can see. The weather is comfortable, and the path is level. The walk is easy, and you see a boulder jutting out from the grass in the distance."
		},
		{
			"name": "The Thicket",
			"tags": "",
			"id": "6",
			"text": "A stone path descends into a thicket of tangled vines covered in sharp and wretched thorns.\n\n[[FORWARD->Deep Thicket]]\n[[BACK->The Crossroads]]",
			"links": [
				{
					"linkText": "FORWARD",
					"passageName": "Deep Thicket",
					"original": "[[FORWARD->Deep Thicket]]"
				},
				{
					"linkText": "BACK",
					"passageName": "The Crossroads",
					"original": "[[BACK->The Crossroads]]"
				}
			],
			"hooks": [],
			"cleanText": "A stone path descends into a thicket of tangled vines covered in sharp and wretched thorns."
		},
		{
			"name": "The old man",
			"tags": "",
			"id": "7",
			"text": "To the side of the path in the meager shade of a large dune you find a frail looking old man clad in a well-worn cloak. Upon seeing you, he asks;\n“Excuse me good traveler, could you find it in your heart to spare this old man some water?”\n\n[[GIVE WATER->The Shield]]\n[[IGNORE->Ignore him]]",
			"links": [
				{
					"linkText": "GIVE WATER",
					"passageName": "The Shield",
					"original": "[[GIVE WATER->The Shield]]"
				},
				{
					"linkText": "IGNORE",
					"passageName": "Ignore him",
					"original": "[[IGNORE->Ignore him]]"
				}
			],
			"hooks": [],
			"cleanText": "To the side of the path in the meager shade of a large dune you find a frail looking old man clad in a well-worn cloak. Upon seeing you, he asks;\n“Excuse me good traveler, could you find it in your heart to spare this old man some water?”"
		},
		{
			"name": "The Shield",
			"tags": "",
			"id": "8",
			"score":10,
			"text": "You offer the old man your water skin, he takes it and drinks only a small swig before smiling happily at you.\n“Thank you kindly traveler! Here, as a token of my appreciation take this shield. It will protect you from the desert sun and even a dragon’s fire. I pray it will serve you well.”\nYou take the shield and the old man disappears.\n\n[[RETURN->The Crossroads]]",
			"links": [
				{
					"linkText": "RETURN",
					"passageName": "The Crossroads",
					"original": "[[RETURN->The Crossroads]]"
				}
			],
			"hooks": [],
			"cleanText": "You offer the old man your water skin, he takes it and drinks only a small swig before smiling happily at you.\n“Thank you kindly traveler! Here, as a token of my appreciation take this shield. It will protect you from the desert sun and even a dragon’s fire. I pray it will serve you well.”\nYou take the shield and the old man disappears."
		},
		{
			"name": "Ignore him",
			"tags": "",
			"id": "9",
			"text": "The path continues endlessly. Your feet are sore, and the sun’s heat bears down on you. Eventually you water runs dry, and the scorched heat claims you soon after.\n\n[[TRY AGAIN->The Altar]]",
			"links": [
				{
					"linkText": "TRY AGAIN",
					"passageName": "The Altar",
					"original": "[[TRY AGAIN->The Altar]]"
				}
			],
			"hooks": [],
			"cleanText": "The path continues endlessly. Your feet are sore, and the sun’s heat bears down on you. Eventually you water runs dry, and the scorched heat claims you soon after."
		},
		{
			"name": "Deep Thicket",
			"tags": "",
			"id": "10",
			"text": "The dense and twisting vines soon block out most of the light from the sun and the stinging thorns tear and scratch at your clothes and skin. You put up your arms to protect your face but it does little to help. It is painful though not lethal.\n\n[[FORWARD->The Clearing]]\n[[BACK->The Thicket]]",
			"links": [
				{
					"linkText": "FORWARD",
					"passageName": "The Clearing",
					"original": "[[FORWARD->The Clearing]]"
				},
				{
					"linkText": "BACK",
					"passageName": "The Thicket",
					"original": "[[BACK->The Thicket]]"
				}
			],
			"hooks": [],
			"cleanText": "The dense and twisting vines soon block out most of the light from the sun and the stinging thorns tear and scratch at your clothes and skin. You put up your arms to protect your face but it does little to help. It is painful though not lethal."
		},
		{
			"name": "The Clearing",
			"tags": "",
			"id": "11",
			"score":10,
			"text": "Emerging from the tangle of thorns and underbrush, you come to a clearing on the other side. In the center is a suit of armor and yet another sign.\n“For those who brave the path, this armor protects from thicket’s thorns and dragon’s talons alike.”\nYou don the armor.\n\n[[RETURN->The Crossroads]]",
			"links": [
				{
					"linkText": "RETURN",
					"passageName": "The Crossroads",
					"original": "[[RETURN->The Crossroads]]"
				}
			],
			"hooks": [],
			"cleanText": "Emerging from the tangle of thorns and underbrush, you come to a clearing on the other side. In the center is a suit of armor and yet another sign.\n“For those who brave the path, this armor protects from thicket’s thorns and dragon’s talons alike.”\nYou don the armor."
		},
		{
			"name": "The Boulder",
			"tags": "",
			"id": "12",
			"text": "You come to a boulder at the end of the path, a sword sticks out from the boulder and an inscription is carved into its blade:\n“Whomsoever can rest this sword from the stone shall gain themselves the power to slay the dragon”\n\n[[PULL->The Sword Resists]]\n[[BACK->The Grassy plane]]",
			"links": [
				{
					"linkText": "PULL",
					"passageName": "The Sword Resists",
					"original": "[[PULL->The Sword Resists]]"
				},
				{
					"linkText": "BACK",
					"passageName": "The Grassy plane",
					"original": "[[BACK->The Grassy plane]]"
				}
			],
			"hooks": [],
			"cleanText": "You come to a boulder at the end of the path, a sword sticks out from the boulder and an inscription is carved into its blade:\n“Whomsoever can rest this sword from the stone shall gain themselves the power to slay the dragon”"
		},
		{
			"name": "The Sword Resists",
			"tags": "",
			"id": "13",
			"text": "You pull and struggle yet for a time the sword seems unwilling to budge yet, right as you are about to give up you feel it move if only an inch.\n\n[[PULL->Free the Sword]]\n[[BACK->The Grassy plane]]",
			"links": [
				{
					"linkText": "PULL",
					"passageName": "Free the Sword",
					"original": "[[PULL->Free the Sword]]"
				},
				{
					"linkText": "BACK",
					"passageName": "The Grassy plane",
					"original": "[[BACK->The Grassy plane]]"
				}
			],
			"hooks": [],
			"cleanText": "You pull and struggle yet for a time the sword seems unwilling to budge yet, right as you are about to give up you feel it move if only an inch."
		},
		{
			"name": "Free the Sword",
			"tags": "",
			"id": "14",
			"score":10,
			"text": "With a truly mighty effort, you finally rest the sword free from the stone. It feels perfectly balanced in your hands and its blade seems sharp enough to cut even dragon scales.\n\n[[RETURN->The Crossroads]]",
			"links": [
				{
					"linkText": "RETURN",
					"passageName": "The Crossroads",
					"original": "[[RETURN->The Crossroads]]"
				}
			],
			"hooks": [],
			"cleanText": "With a truly mighty effort, you finally rest the sword free from the stone. It feels perfectly balanced in your hands and its blade seems sharp enough to cut even dragon scales."
		},
		{
			"name": "The Dragon",
			"tags": "",
			"id": "15",
			"text": "Atop the peak you find a lumbering dragon easily the size of a house with crimson scales thick as tree trunks, talons that could rip through steel, and a fire in its eyes as it gazes down upon you. But your shield shelters you from its fire, your armor brushes off its talons, and your sword cleaves its mighty scales. In the end you are able to defeat the beast.\n\n[[GO HOME->Home]]",
			"links": [
				{
					"linkText": "GO HOME",
					"passageName": "Home",
					"original": "[[GO HOME->Home]]"
				}
			],
			"hooks": [],
			"cleanText": "Atop the peak you find a lumbering dragon easily the size of a house with crimson scales thick as tree trunks, talons that could rip through steel, and a fire in its eyes as it gazes down upon you. But your shield shelters you from its fire, your armor brushes off its talons, and your sword cleaves its mighty scales. In the end you are able to defeat the beast."
		},
		{
			"name": "Home",
			"tags": "",
			"id": "16",
			"text": "You wake with a start, finding yourself sitting upright in your bed having peacefully returned to your home.",
			"links": [],
			"hooks": [],
			"cleanText": "You wake with a start, finding yourself sitting upright in your bed having peacefully returned to your home."
		}
	]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
			for passage in world["passages"]:
					if location_label == passage["name"]:
							return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
			#print("Moves: " + str(moves) + " Score: " + str(score))
			print("Moves: {}, Score: {}".format(moves, score))
			print("You are at the " + str(current_location["name"]))
			print(current_location["cleanText"] + "\n")
			for link in current_location["links"]:
					print( "> " + link["linkText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
			return location_label
	if "links" in current_location:
			for link in current_location["links"]:
					if link["linkText"] == response:
							return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label

# ----------------------------------------------------------------

location_label = "The Altar"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break

	moves = moves + 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
			
	# Death 
	if response == "FIGHT" and score < 30:
		print("Without the treasures, you are slain by the dragon.")
		location_label = "The Altar"
		current_location = find_current_location(location_label)

	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing!")
