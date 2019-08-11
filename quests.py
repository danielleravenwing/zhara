QUESTS = {}
QUESTS['A fish for Loella'] = {'accepted': False, 'completed': False, 'rewarded': False, 'inventory check': False,
                               'description': 'Catch a goldfish for Loella\'s fish tank in the town of Dewcastle.',
                               'accept text': ['Oh, thank you so much! I\'m so excited!'],
                               'deny text': ['Oh... ok. I hope my daddy will get home soon to help me.'],
                               'completed text': ['I love my new fish!'],
                               'waiting text': ['Have you found a fish for me yet? I hope you find one soon. I\'m so excited. Please hurry.'],
                               'reward': ['potion of major healing'],
                               'reward text': ['Thank you so much for the fish. Please take this healing potion as a token of my appreciation.'],
                               'next quest': 'A friend for Loella',
                               'next dialogue': 'LOELLA_DLG2'}

QUESTS['A friend for Loella'] = {'accepted': False, 'completed': False, 'rewarded': False, 'inventory check': False,
                               'description': 'Loella needs help finding a friend in the town of Dewcastle.',
                               'accept text': ['Oh, thank you so much! I\'m so excited to meet my new friend!'],
                               'deny text': ['Oh... ok. I guess I\'ll have to go out and make friends like a normal kid.'],
                               'completed text': ['I\'m really enjoying playing with Kimmy!'],
                               'waiting text': ['Have you found a friend for me yet? I hope you find one soon. I\'m so excited. Please hurry.'],
                               'reward': ['potion of major stamina'],
                               'reward text': ['Thank you so much for introducing me to Kimmy! Please take this stamina potion as a token of my appreciation.'],
                               'next quest': None,
                               'next dialogue': None}

QUESTS['A mace for Steve'] = {'accepted': False, 'completed': False, 'rewarded': False, 'inventory check': True, 'needed item': 'mace',
                               'description': 'Steve is a slacker and lost his mace. He needs help finding a new one in the town of Dewcastle.',
                               'accept text': ['Oh, thank you so much! You\'re a life saver.'],
                               'deny text': ['Thanks okay. I can see you\'re busy.'],
                               'completed text': ['This new mace is awesome. You really saved my neck.'],
                               'waiting text': ['Have you found that mace for me yet? The captain will have my head for this. Please hurry.'],
                               'has item text': ['I see you brought me a mace. May I have it?YN'],
                               'refuse to give text': ['That\'s not at all what we agreed to. How rude.'],
                               'reward': ['baked potato', 'cheese wedge', 'gold12'],
                               'reward text': ['Thanks so much. Sorry, I don\'t have much to reward you with, but here\'s my lunch and what\'s left of yesterday\'s wages.'],
                               'next quest': None,
                               'next dialogue': 'STEVE_DLG2'}

QUESTS['Ant eggs for Tamolin'] = {'accepted': False, 'completed': False, 'rewarded': False, 'inventory check': True, 'needed item': 'giant ant eggs',
                               'description': 'Tamolin of Dewcastle wants you to find giant ant eggs so he can create powerful new potions. Search the ant tunnels to the south and see if you can find any eggs.',
                               'accept text': ['Oh, thank you. I would have gone myself, but I\'d have no one to watch the shop for me.'],
                               'deny text': ['Not up to it huh? Perhaps I can find someone else who is brave enough.'],
                               'completed text': ['These eggs are beautiful. They are much larger than I expected.'],
                               'waiting text': ['Any luck finding those ant eggs for me?'],
                               'has item text': ['Wonderful! I see you found some giant ant eggs. May I have them?YN'],
                               'refuse to give text': ['Oh, so you want them for yourself huh? Ok, good luck figuring out what to do with them.'],
                               'reward': ['gold2000'],
                               'reward text': ['Amazing! I can tell you are a brave adventurer.'],
                               'next quest': None,
                               'next dialogue': 'TAMOLIN_DLG2'}

QUESTS['Clay for Tamolin'] = {'accepted': False, 'completed': False, 'rewarded': False, 'inventory check': True, 'needed item': 'giant ant eggs',
                               'description': 'Tamolin of Dewcastle wants you to eggs.',
                               'accept text': ['Oh, thank you. I would have gone myself, but I\'d have no one to watch the shop for me.'],
                               'deny text': ['Not up to it huh? Perhaps I can find someone else who is brave enough.'],
                               'completed text': ['These eggs are beautiful. They are much larger than I expected.'],
                               'waiting text': ['Any luck finding those ant eggs for me?'],
                               'has item text': ['Wonderful! I see you found some giant ant eggs. May I have them?YN'],
                               'refuse to give text': ['Oh, so you want them for yourself huh? Ok, good luck figuring out what to do with them.'],
                               'reward': ['gold2000'],
                               'reward text': ['Amazing! I can tell you are a brave adventurer.'],
                               'next quest': None,
                               'next dialogue': 'TAMOLIN_DLG2'}

QUESTS['Fuel for Felius'] = {'accepted': False, 'completed': False, 'rewarded': False, 'inventory check': True, 'needed item': 'airship fuel', 'action': 'companion',
                               'description': 'Find some fuel for Felius\' airship, so he can go back home.',
                               'accept text': ['Oh, thank you so much! Please take as many of those empty barrels by my house as you can carry. You\'ll need them to bring the fuel back in.', 'Good luck my friend!'],
                               'deny text': ['Oh, I hope you change your mind. I\'m not sure how much longer I can survive out here.'],
                               'completed text': ['This is perfect! You really saved my life. You won\'t regret this!'],
                               'waiting text': ['Any luck finding airship fuel? I could probably make some if I had an alchemy lab.', 'An alchemist friend of mine made the fuel, using oil and alcohol.'],
                               'has item text': ['Wonderful! You found the fuel. May I have it?YN'],
                               'refuse to give text': ['Oh, well that\'s cruel of you to bring it all this way just to taunt me.'],
                               'reward': [],
                               'reward text': ['Thank you so much! Now I can be with my family again. I don\'t have anything to offer except for my airship. I think I\'ve done enough exploring for one lifetime. Accompany me home and the key is yours.'],
                               'next quest': 'Take Felius Home',
                               'next dialogue': 'FELIUS_DLG2'}

QUESTS['Take Felius Home'] = {'accepted': False, 'completed': False, 'rewarded': False, 'inventory check': False, 'autoaccept': True,
                               'description': 'Escort Felius back to his home in Norwald.',
                               'completed text': ['I\'m so happy to be home.'],
                               'waiting text': ['I hope it doesn\'t take us too much longer to get home.', 'It\'s a long way home to Norwald. I\'m glad to have a warrior like you accompanying me.', 'I\'ll fight for you so long as we are together friend.'],
                               'reward': ['airship key'],
                               'reward text': ['Thank you so much! I\'m so happy to be with my family again. Here\'s the key to my airship. Please take good care of her.'],
                               'next quest': None,
                               'next dialogue': 'FELIUS_DLG2'}
QUESTS['Turtle Armor for Jaz'] = {"accepted": False, "completed": False, "rewarded": False, "inventory check": True, "needed item": "turtle plate armor", "description": "Forge Jaz some turtle plate armor, so she can be ready for her epic quest.", "accept text": ["Oh, thank you so much. I wish I had the smithing skills to make my own armor, but I'm so glad you decided to help me."], "deny text": ["Oh, well that's okay. Maybe I can learn how to make some for myself."], "completed text": ["This new armor is awesome. Thanks so much!"], "waiting text": ["Have you made me that armor yet?"], "has item text": ["I see you made some turtle armor for me. May I have it?YN"], "refuse to give text": ["Oh, you decided to keep it for yourself huh? Well, it is really nice. I don't blame you. I'll just have to make my own."], "reward text": ["Amazing! Here's a little cash for your efforts and some lunch."], "next quest": 'Let Jaz join your quest', "next dialogue": "JAZ_DLG2", "reward": ["roasted bluefish","gold225"]}
QUESTS['Let Jaz join your quest'] = {'action': 'companion', "autocomplete": True, "accepted": False, "completed": False, "rewarded": False, "inventory check": False, "needed item": None, "description": "Let Jaz join your quest.", "accept text": ["Oh, thank you so much. I'll do my best to make a great companion on your journey."], "deny text": ["Oh, I guess you'd rather travel alone. I'm sure I can find an epic quest myself."], "completed text": ["I'm excited. Lead the way!"], "waiting text": [""], "has item text": [""], "refuse to give text": [""], "reward text": ["Here's some more food for our journey."], "next quest": None, "next dialogue": "JAZ_DLG3", "reward": ['cheese wedge', 'french bread']}
QUESTS['Jamal the body guard'] = {'action': 'companion', "accepted": False, "completed": False, "rewarded": False, "inventory check": True, "needed item": "1c000gold", "autocomplete": False, "autoaccept": False, "description": "Pay Jamal 1000 gold to protect you.", "accept text": ["Great. You won't regret this."], "deny text": ["Well, maybe next time."], "completed text": ["I'll shoot anything that gets in our way."], "waiting text": ["Got that money yet?"], "has item text": ["I see you have the cash. Want to pay me now?YN"], "refuse to give text": ["I'd reconsider if I were you."], "reward text": ["Nice. I've got your back."], "next quest": None, "next dialogue": "JAMAL_DLG2", "reward": [""]}