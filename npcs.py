from settings import *
from random import choice, randrange
from armor import *
from character_positions import *

# Stores
BLACKSMITH_STORE = {'markup': 1.5, 'pvalue': 0.8, 'inventory': {'weapons': ['steel sword', 'iron dagger'], 'hats': ['steel helmet'], 'hair': [None], 'tops': ['leather armor M', 'leather armor F'], 'bottoms': ['leather leggings M', 'leather leggings F'], 'shoes': ['steel boots'], 'gloves': ['steel gauntlets'], 'gold': 0, 'items': ['steel ingot', 'iron ingot', 'gold ingot', 'silver ingot', 'charcoal', 'wood block', 'leather', 'leather strips'], 'magic': [None]}}
LACERTOLIAN_BLACKSMITH_STORE = {'markup': 1, 'pvalue': 0.8, 'inventory': {'weapons': ['bronze mace', 'iron dagger'], 'hats': ['steel helmet'], 'hair': [None], 'tops': ['leather armor M', 'leather armor F'], 'bottoms': ['leather leggings M', 'leather leggings F'], 'shoes': ['steel boots'], 'gloves': ['steel gauntlets'], 'gold': 0, 'items': ['bronze ingot', 'iron ingot', 'copper ingot', 'brass ingot', 'charcoal', 'wood block', 'leather', 'leather strips'], 'magic': [None]}}
ELF_BLACKSMITH_STORE = {'markup': 1.5, 'pvalue': 0.8, 'inventory': {'weapons': ['steel dagger', 'iron dagger'], 'hats': ['steel helmet', 'elf hat'], 'hair': [None], 'tops': ['leather armor M', 'leather armor F'], 'bottoms': ['leather leggings M', 'leather leggings F'], 'shoes': ['steel boots'], 'gloves': ['steel gauntlets'], 'gold': 0, 'items': ['steel ingot', 'iron ingot', 'gold ingot', 'silver ingot', 'charcoal', 'wood block', 'leather', 'leather strips'], 'magic': [None]}}
SHAKTELE_BLACKSMITH_STORE = {'markup': 1.5, 'pvalue': 0.8, 'inventory': {'weapons': ['pistol', 'grenade launcher', 'mini gun', 'auto grenade launcher', 'shotgun', 'assault rifle'], 'hats': ['tactical helmet', 'military helmet'], 'hair': [None], 'tops': ['shaktele guard armor', 'leather armor M', 'leather armor F'], 'bottoms': ['leather leggings M', 'leather leggings F'], 'shoes': ['steel boots', 'black combat'], 'gloves': ['steel gauntlets', 'leather gauntlets'], 'gold': 0, 'items': ['steel ingot', 'iron ingot', 'aluminum', 'brass ingot', 'lead ingot', 'charcoal', 'gun powder', 'wood block', 'leather', 'leather strips'], 'magic': [None]}}
MIEWDRA_BLACKSMITH_STORE = {'markup': 1.5, 'pvalue': 0.8, 'inventory': {'weapons': ['miewdra blade', 'steel dagger'], 'hats': ['steel helmet'], 'hair': [None], 'tops': ['leather armor M', 'leather armor F'], 'bottoms': ['leather leggings M', 'leather leggings F'], 'shoes': ['steel boots'], 'gloves': ['steel gauntlets'], 'gold': 0, 'items': ['steel ingot', 'iron ingot', 'copper ingot', 'brass ingot', 'gold ingot', 'silver ingot', 'charcoal', 'wood block', 'leather', 'leather strips'], 'magic': [None]}}
MECHANIMA_BLACKSMITH_STORE = {'markup': 1.5, 'pvalue': 0.8, 'inventory': {'weapons': ['steel sword', 'steel dagger', 'mechanima blaster'], 'hats': ['tactical helmet'], 'hair': [None], 'tops': ['guard armor', 'steel plate armor', 'leather armor M', 'leather armor F'], 'bottoms': ['chainmail leggings M', 'chainmail leggings F', 'leather leggings M', 'leather leggings F'], 'shoes': ['steel boots'], 'gloves': ['steel gauntlets'], 'gold': 0, 'items': ['steel ingot', 'iron ingot', 'aluminum ingot', 'machine screws', 'springs', 'copper ingot', 'brass ingot', 'bronze ingot', 'large laser ammo module', 'medium laser ammo module', 'gold ingot', 'silver ingot', 'charcoal', 'wood block', 'leather', 'leather strips'], 'magic': [None]}}
TAMOLIN_STORE = {'markup': 1.2, 'pvalue': 0.7, 'inventory': {'weapons': [None], 'hats': ['red cloak', 'blue cloak', 'black cloak'], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 0, 'items': ['potion of moderate healing', 'potion of major healing', 'potion of moderate stamina', 'potion of moderate magica', 'empty bottle', 'yarrow', 'sulphur', 'potassium nitrate crystals', 'charcoal', 'red crystal', 'yellow crystal', 'green crystal', 'healing spell tome', 'fire spray spell tome', 'fireball tome'], 'magic': [None]}}
DANGERMAN_STORE = {'markup': 0.2, 'pvalue': 0.1, 'inventory': {'weapons': [None], 'hats': [None], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 0, 'items': ['lock pick'], 'magic': [None]}}
FELIUS_STORE = {'markup': 2, 'pvalue': 0.5, 'inventory': {'weapons': [None], 'hats': [None], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 0, 'items': ['wolf skin', 'deer skin', 'leather'], 'magic': [None]}}
KEVIN_STORE = {'markup': 2.5, 'pvalue': 0.9, 'inventory': {'weapons': [None], 'hats': [None], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 0, 'items': ['distilled alcohol', 'squid ink', 'candle', 'potion of major healing', 'gun powder', 'charcoal', 'surphur', 'potassium nitrate crystals'], 'magic': [None]}}
ANNA_STORE = {'markup': 1.2, 'pvalue': 0.1, 'inventory': {'weapons': [None], 'hats': [None], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 0, 'items': ['carrot', 'horse bridle'], 'magic': [None]}}
LIZ_STORE = {'markup': 1.2, 'pvalue': 0.7, 'inventory': {'weapons': [None], 'hats': ['red cloak'], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 0, 'items': ['potion of moderate healing', 'potion of major healing', 'potion of moderate stamina', 'potion of moderate magica', 'empty bottle', 'yarrow', 'charcoal', 'red crystal', 'blue crystal', 'green crystal', 'healing spell tome', 'fireball tome', 'clay', 'cut wood', 'squid ink', 'squid eye', 'spider venom'], 'magic': [None]}}


NPC_TYPE_LIST = ['people', 'animals']
# NPCs Settings
PEOPLE = {}
# Agression variable is used to determine the behavior of NPC when detected and attacked. awd = attack when detected, awp = attack when provoked, fwp = flee when provoked, fwd = flee when detected, fup = flee until provoked, sap = stationary then aggressive when provoked
PEOPLE['melerous'] = {'name': 'Melerous', 'protected': False, 'health': 100, 'touch damage': True, 'damage': 10, 'knockback': 0, 'walk speed': (75, 150), 'run speed': 200, 'detect radius': 500, 'avoid radius': 10, 'aggression': 'awd', 'armed': False, 'dual wield': False,
    'collide': [],
    'gender': 'male', 'race': 'blackwraith',
    'dialogue': None, 'store': None,
    'inventory': {'weapons': ['karang'], 'hats': ['dark wizard hood'], 'hair': [None], 'tops': ['melerous armor'], 'bottoms': ['chainmail leggings M'], 'shoes': ['demon boots'], 'gloves': ['demon gauntlets'], 'gold': 0, 'items': ['random BLACKWRAITH_'], 'magic': ['fireball']},
    'animations': {None}}
PEOPLE['vadashay'] = {'name': 'Vadashay', 'protected': False, 'health': 100, 'touch damage': True, 'damage': 10, 'knockback': 20, 'walk speed': (75, 150), 'run speed': 200, 'detect radius': 600, 'avoid radius': 100, 'aggression': 'awd', 'armed': False, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables'],
    'gender': 'random', 'race': 'vadashay',
    'dialogue': None, 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 100, 'items': ['dead bluefish'], 'magic': [None]},
    'animations': {None}}
PEOPLE['demon'] = {'name': 'demon', 'protected': False, 'health': 666, 'touch damage': True, 'damage': 10, 'knockback': 20, 'walk speed': (100, 150), 'run speed': 260, 'detect radius': 650, 'avoid radius': 100, 'aggression': 'awd', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables'],
    'gender': 'random', 'race': 'demon',
    'dialogue': None, 'store': None,
    'inventory': {'weapons': ['random DEMON_'], 'hats': ['random DEMON_'], 'hair': ['random DEMON_'], 'tops': ['random DEMON_'], 'bottoms': ['random DEMON_'], 'shoes': [None], 'gloves': ['random DEMON_'], 'gold': 666, 'items': ['random DEMON_'], 'magic': [None]},
    'animations': {None}}

DEMON_HATS = [None, 'demon helmet']
DEMON_HAIR = RACE_HAIR['demon']
DEMON_GLOVES = [None, 'demon gauntlets']
DEMON_TOPS = [None, 'demon armor M', 'demon armor F']
DEMON_BOTTOMS = [None, 'leather leggings M', 'chainmail leggings M']
DEMON_WEAPONS = [None, 'ancient viking sword', 'bone club', 'steel mace', 'grenade launcher', 'auto grenade launcher', 'shotgun']
DEMON_ITEMS = [None, 'charcoal', 'charcoal', 'sulphur', 'sulphur', 'sulphur', 'sulphur', 'jar', 'empty bottle', 'potion of major magica', 'sheep horn', 'gun powder']
PEOPLE['clay golem guard'] = {'name': 'clay golem Guard', 'protected': False, 'health': 400, 'touch damage': False, 'damage': 50, 'knockback': 50, 'walk speed': (70, 100), 'run speed': 200, 'detect radius': 700, 'avoid radius': 100, 'aggression': 'awp', 'armed': False, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables'],
    'gender': 'random', 'race': 'golem',
    'dialogue': None, 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 300, 'items': ['clay', 'clay', 'clay', 'clay'], 'magic': [None]},
    'animations': {None}}
PEOPLE['ice golem'] = {'name': 'ice golem', 'protected': False, 'health': 400, 'touch damage': False, 'damage': 50, 'knockback': 50, 'walk speed': (70, 100), 'run speed': 200, 'detect radius': 700, 'avoid radius': 100, 'aggression': 'awd', 'armed': False, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables'],
    'gender': 'random', 'race': 'icegolem',
    'dialogue': None, 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 300, 'items': ['living water', 'living water', 'living water', 'living water'], 'magic': [None]},
    'animations': {None}}
PEOPLE['goblin'] = {'name': 'goblin', 'protected': False, 'health': 200, 'touch damage': False, 'damage': 10, 'knockback': 5, 'walk speed': (100, 200), 'run speed': 300, 'detect radius': 700, 'avoid radius': 100, 'aggression': 'awd', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables'],
    'gender': 'random', 'race': 'goblin',
    'dialogue': None, 'store': None,
    'inventory': {'weapons': ['random SKELETON_'], 'hats': [None], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 100, 'items': ['random SKELETON_'], 'magic': [None]},
    'animations': {None}}
PEOPLE['goblin king'] = {'name': 'Tronold Grump', 'protected': False, 'health': 10000, 'touch damage': False, 'damage': 100, 'knockback': 20, 'walk speed': (50, 75), 'run speed': 90, 'detect radius': 400, 'avoid radius': 80, 'aggression': 'sap', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'water', 'jumpables', 'climbables'],
    'gender': 'male', 'race': 'goblin',
    'dialogue': 'GOBLIN_KING_DLG', 'store': None,
    'inventory': {'weapons': ['live goldfish'], 'hats': ['golden crown'], 'hair': ['The Golden Toupee'], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 1000000000, 'items': [None], 'magic': [None]},
    'animations': {None}}
PEOPLE['goblin guard'] = {'name': 'Goblin Guard', 'protected': True, 'health': 350, 'touch damage': False, 'damage': 15, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 200, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'water', 'jumpables', 'climbables'],
    'gender': 'random', 'race': 'goblin',
    'dialogue': 'random GUARD_DLG', 'store': None,
    'inventory': {'weapons': ['bone club'], 'hats': ['skull helmet'], 'hair': [None], 'tops': ['iron plate armor'], 'bottoms': ['leather leggings M'], 'shoes': [None], 'gloves': [None], 'gold': 250, 'items': ['random'], 'magic': [None]},
    'animations': {None}}
PEOPLE['goblin slave'] = {'name': 'slave', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 0, 'knockback': 2, 'walk speed': (90, 100), 'run speed': 300, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'fwp', 'armed': False, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables', 'lava'],
    'gender': 'random', 'race': 'random HUMAN_RACES',
    'dialogue': 'random GOBLIN_SLAVE_DLG', 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': ['random'], 'tops': ['random VILLAGER_'], 'bottoms': ['random VILLAGER_'], 'shoes': ['random'], 'gloves': [None], 'gold': 100, 'items': ['random'], 'magic': [None]},
    'animations': {None}}
HUMAN_RACES = ['shaktele', 'osidine']
PEOPLE['immortui'] = {'name': 'Immortui', 'protected': False, 'health': 100, 'touch damage': True, 'damage': 10, 'knockback': 20, 'walk speed': (75, 150), 'run speed': 200, 'detect radius': 600, 'avoid radius': 50, 'aggression': 'awd', 'armed': False, 'dual wield': False,
    'collide': ['obstacles', 'vehicles'],
    'gender': 'random', 'race': 'immortui',
    'dialogue': None, 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': ['random'], 'tops': ['random IMMORTUI_'], 'bottoms': ['random IMMORTUI_'], 'shoes': ['random'], 'gloves': [None], 'gold': 100, 'items': ['random IMMORTUI_'], 'magic': [None]},
    'animations': {'walk': ZOMBIE_WALK}}
IMMORTUI_TOPS = ['decayed shirt F', 'decayed shirt M', 'tshirt M', 'tshirt F', 'dark tshirt M', 'dark tshirt F']
IMMORTUI_BOTTOMS = CASUAL_BOTTOMS_LIST
IMMORTUI_ITEMS = ['zombie extract', 'zombie extract', 'zombie extract', 'zombie extract', 'zombie extract', 'charcoal', 'charcoal', 'sulphur', 'cheese wedge', 'potato', 'garlic', 'empty bottle', 'jar', 'potion of minor magica', 'potion of minor healing', 'potion of minor stamina']
PEOPLE['blackwraith'] = {'name': 'black wraith', 'protected': False, 'health': 100, 'touch damage': True, 'damage': 10, 'knockback': 0, 'walk speed': (75, 150), 'run speed': 200, 'detect radius': 500, 'avoid radius': 10, 'aggression': 'awd', 'armed': False, 'dual wield': False,
    'collide': [],
    'gender': 'random', 'race': 'blackwraith',
    'dialogue': None, 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 0, 'items': ['random BLACKWRAITH_'], 'magic': ['fireball']},
    'animations': {'walk': ZOMBIE_WALK}}
BLACKWRAITH_ITEMS = ['demon dust', 'ectoplasm']
PEOPLE['whitewraith'] = {'name': 'white wraith', 'protected': False, 'health': 100, 'touch damage': True, 'damage': 10, 'knockback': 0, 'walk speed': (75, 150), 'run speed': 200, 'detect radius': 500, 'avoid radius': 300, 'aggression': 'awd', 'armed': False, 'dual wield': False,
    'collide': [],
    'gender': 'random', 'race': 'whitewraith',
    'dialogue': None, 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 0, 'items': ['random BLACKWRAITH_'], 'magic': [None]},
    'animations': {'walk': ZOMBIE_WALK}}
PEOPLE['skeleton'] = {'name': 'skeleton', 'protected': False, 'health': 300, 'touch damage': False, 'damage': 10, 'knockback': 5, 'walk speed': (100, 200), 'run speed': 300, 'detect radius': 700, 'avoid radius': 150, 'aggression': 'awd', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'water', 'jumpables', 'climbables'],
    'gender': 'random', 'race': 'skeleton',
    'dialogue': None, 'store': None,
    'inventory': {'weapons': ['random SKELETON_'], 'hats': [None], 'hair': [None], 'tops': [None], 'bottoms': [None], 'shoes': [None], 'gloves': [None], 'gold': 100, 'items': ['random SKELETON_'], 'magic': [None]},
    'animations': {None}}
SKELETON_WEAPONS = ['ancient viking sword', 'bone club']
SKELETON_ITEMS = ['charcoal', 'charcoal', 'sulphur', 'sulphur', 'sulphur', 'sulphur', 'jar', 'empty bottle', 'yarrow', 'sheep horn', 'gun powder']

PEOPLE['blacksmith'] = {'name': 'Blacksmith', 'protected': True, 'health': 500, 'touch damage': False, 'damage': 30, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['obstacles', 'vehicles'],
    'gender': 'female', 'race': 'osidine',
    'dialogue': 'BLACKSMITH_DLG', 'store': BLACKSMITH_STORE,
    'inventory': {'weapons': ['steel sword'], 'hats': [None], 'hair': ['long black pony'], 'tops': ['black racerback tank top'], 'bottoms': ['leather leggings F'], 'shoes': ['brown boots'], 'gloves': ['leather gauntlets'], 'gold': randrange(100, 1000), 'items': ['dewcastle blacksmith chest key'], 'magic': [None]},
    'animations': {None}}
PEOPLE['tamolin'] = {'name': 'Tamolin the Mage', 'quest': 'Ant eggs for Tamolin', 'protected': True, 'health': 550, 'touch damage': False, 'damage': 25, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['obstacles', 'vehicles'],
    'gender': 'male', 'race': 'shaktele',
    'dialogue': 'TAMOLIN_DLG', 'store': TAMOLIN_STORE,
    'inventory': {'weapons': ['bronze mace'], 'hats': ['red cloak'], 'hair': ['short brown'], 'tops': ['blue mage robe top M'], 'bottoms': ['blue mage robe bottom'], 'shoes': ['brown boots'], 'gloves': [None], 'gold': randrange(100, 1000), 'items': ['random'], 'magic': [None]},
    'animations': {None}}
PEOPLE['kimmy'] = {'name': 'Kimmy', 'protected': True,'health': 1000, 'touch damage': False, 'damage': 15, 'knockback': 1, 'walk speed': (300, 400), 'run speed': 400, 'detect radius': 200, 'avoid radius': 100, 'aggression': 'fwp', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables'],
    'gender': 'female', 'race': 'elf',
    'dialogue': 'KIMMY_DLG', 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': ['long blond'], 'tops': ['tshirt F'], 'bottoms': ['red mini dress skirt'], 'shoes': [None], 'gloves': [None], 'gold': randrange(100, 200), 'items': ['random'], 'magic': [None]},
    'animations': {'walk': RUNNING}}
PEOPLE['loella'] = {'name': 'Loella', 'quest': 'A fish for Loella', 'protected': True,'health': 1000, 'touch damage': False, 'damage': 0, 'knockback': 1, 'walk speed': (200, 300), 'run speed': 400, 'detect radius': 200, 'avoid radius': 100, 'aggression': 'fwp', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables', 'water'],
    'gender': 'female', 'race': 'elf',
    'dialogue': 'LOELLA_DLG', 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': ['long straight brown'], 'tops': ['dark tshirt F'], 'bottoms': ['green mini dress skirt'], 'shoes': [None], 'gloves': [None], 'gold': randrange(100, 200), 'items': ['random'], 'magic': [None]},
    'animations': {None}}
PEOPLE['steve'] = {'name': 'Steve the Guard', 'quest': 'A mace for Steve', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 15, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 200, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'water', 'jumpables', 'climbables'],
    'gender': 'male', 'race': 'osidine',
    'dialogue': 'STEVE_DLG', 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': ['short messy'], 'tops': ['guard armor'], 'bottoms': ['random GUARD_'], 'shoes': ['steel boots'], 'gloves': ['steel gauntlets'], 'gold': 12, 'items': ['baked potato', 'cheese wedge'], 'magic': [None]},
    'animations': {None}}
PEOPLE['anna'] = {'name': 'Anna the Stable Guard', 'quest': None, 'protected': True, 'health': 100, 'touch damage': False, 'damage': 15, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 400, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'water', 'jumpables', 'climbables'],
    'gender': 'female', 'race': 'osidine',
    'dialogue': 'ANNA_DLG', 'store': ANNA_STORE,
    'inventory': {'weapons': ['steel dagger'], 'hats': [None], 'hair': ['long blond pony'], 'tops': ['leather armor F'], 'bottoms': ['leather leggings F'], 'shoes': ['steel boots'], 'gloves': ['leather gauntlets'], 'gold': 12, 'items': ['cheese wedge', 'carrot'], 'magic': [None]},
    'animations': {None}}
PEOPLE['guard'] = {'name': 'Guard', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 15, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 200, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'water', 'jumpables', 'climbables'],
    'gender': 'random', 'race': 'osidine',
    'dialogue': 'random GUARD_DLG', 'store': None,
    'inventory': {'weapons': ['random GUARD_'], 'hats': ['random GUARD_'], 'hair': ['random'], 'tops': ['guard armor'], 'bottoms': ['random GUARD_'], 'shoes': ['steel boots'], 'gloves': ['random GUARD_'], 'gold': 250, 'items': ['random'], 'magic': [None]},
    'animations': {None}}
GUARD_WEAPONS = ['steel sword', 'steel mace']
GUARD_HATS = ['guard helmet', 'steel helmet']
GUARD_GLOVES = ['steel gauntlets', 'leather gauntlets']
GUARD_BOTTOMS = ['chainmail leggings F', 'leather leggings F', 'chainmail leggings M', 'leather leggings M']
PEOPLE['villager'] = {'name': 'Villager', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 0, 'knockback': 2, 'walk speed': (90, 100), 'run speed': 300, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'fwp', 'armed': False, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables', 'lava'],
    'gender': 'random', 'race': 'osidine',
    'dialogue': 'random VILLAGER_DLG', 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': ['random'], 'tops': ['random VILLAGER_'], 'bottoms': ['random VILLAGER_'], 'shoes': ['random'], 'gloves': [None], 'gold': 100, 'items': ['random'], 'magic': [None]},
    'animations': {None}}
VILLAGER_TOPS = CASUAL_TOPS_LIST
VILLAGER_BOTTOMS = CASUAL_BOTTOMS_LIST

PEOPLE['shaktelevillager'] = {'name': 'Villager', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 0, 'knockback': 2, 'walk speed': (90, 100), 'run speed': 300, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'fwp', 'armed': False, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables', 'lava'],
    'gender': 'random', 'race': 'shaktele',
    'dialogue': 'random VILLAGER_DLG', 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': ['random SHAKTELEVILLAGER_'], 'tops': ['random VILLAGER_'], 'bottoms': ['random VILLAGER_'], 'shoes': ['random'], 'gloves': [None], 'gold': 100, 'items': ['random'], 'magic': [None]},
    'animations': {None}}
SHAKTELEVILLAGER_HAIR = RACE_HAIR['shaktele']
PEOPLE['shaktele blacksmith'] = {'name': 'Blacksmith', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 30, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['obstacles', 'vehicles'],
    'gender': 'male', 'race': 'shaktele',
    'dialogue': 'BLACKSMITH_DLG', 'store': SHAKTELE_BLACKSMITH_STORE,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': ['dreadlocks'], 'tops': ['tshirt M'], 'bottoms': ['leather leggings F'], 'shoes': ['brown boots'], 'gloves': ['leather gauntlets'], 'gold': randrange(100, 1000), 'items': ['random'], 'magic': [None]},
    'animations': {None}}

PEOPLE['shakteleguard'] = {'name': 'Guard', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 15, 'knockback': 10, 'walk speed': (190, 200), 'run speed': 260, 'detect radius': 450, 'avoid radius': 130, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'water', 'jumpables', 'climbables'],
    'gender': 'random', 'race': 'shaktele',
    'dialogue': 'random GUARD_DLG', 'store': None,
    'inventory': {'weapons': ['assault rifle'], 'hats': ['tactical helmet'], 'hair': ['random'], 'tops': ['shaktele guard armor'], 'bottoms': ['random GUARD_'], 'shoes': ['black combat'], 'gloves': ['leather gauntlets'], 'gold': 250, 'items': ['random'], 'magic': [None]},
    'animations': {None}}

PEOPLE['kevin'] = {'name': 'Kevin', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 15, 'knockback': 10, 'walk speed': (190, 200), 'run speed': 260, 'detect radius': 450, 'avoid radius': 130, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'water', 'jumpables', 'climbables'],
    'gender': 'male', 'race': 'shaktele',
    'dialogue': 'KEVIN_DLG', 'store': KEVIN_STORE,
    'inventory': {'weapons': ['steel dagger'], 'hats': [None], 'hair': ['dreadlocks'], 'tops': ['shaktele guard armor'], 'bottoms': ['leather leggings M'], 'shoes': ['black combat'], 'gloves': [None], 'gold': 200, 'items': ['random'], 'magic': [None]},
    'animations': {None}}

PEOPLE['miewdravillager'] = {'name': 'Miewdra Villager', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 0, 'knockback': 2, 'walk speed': (90, 100), 'run speed': 300, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'fwp', 'armed': False, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables', 'lava'],
    'gender': 'random', 'race': 'miewdra',
    'dialogue': 'random MIEWDRA_VILLAGER_DLG', 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': ['random MIEWDRAVILLAGER_'], 'tops': ['random MIEWDRAVILLAGER_'], 'bottoms': ['random MIEWDRAVILLAGER_'], 'shoes': ['random'], 'gloves': [None], 'gold': 100, 'items': ['random'], 'magic': [None]},
    'animations': {None}}
MIEWDRAVILLAGER_TOPS = CASUAL_TOPS_LIST
MIEWDRAVILLAGER_BOTTOMS = CASUAL_BOTTOMS_LIST
MIEWDRAVILLAGER_HAIR = RACE_HAIR['miewdra']
PEOPLE['miewdra blacksmith'] = {'name': 'Blacksmith', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 30, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['obstacles', 'vehicles'],
    'gender': 'male', 'race': 'miewdra',
    'dialogue': 'BLACKSMITH_DLG', 'store': MIEWDRA_BLACKSMITH_STORE,
    'inventory': {'weapons': ['steel dagger'], 'hats': ['elf hat'], 'hair': ['cat tufts'], 'tops': ['leather armor M'], 'bottoms': ['leather leggings M'], 'shoes': ['brown boots'], 'gloves': ['leather gauntlets'], 'gold': randrange(100, 1000), 'items': ['random'], 'magic': [None]},
    'animations': {None}}
PEOPLE['felius'] = {'name': 'Felius', 'quest': 'Fuel for Felius', 'protected': True, 'health': 1000, 'touch damage': False, 'damage': 50, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['obstacles', 'vehicles'],
    'gender': 'male', 'race': 'miewdra',
    'dialogue': 'FELIUS_DLG', 'store': FELIUS_STORE,
    'inventory': {'weapons': ['miewdra blade'], 'hats': [None], 'hair': ['cat tufts'], 'tops': ['demon armor M'], 'bottoms': ['chainmail leggings M'], 'shoes': ['demon boots'], 'gloves': ['demon gauntlets'], 'gold': randrange(100, 1000), 'items': ['fireball tome'], 'magic': ['fireball']},
    'animations': {None}}
PEOPLE['catrina'] = {'name': 'Catrina', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 0, 'knockback': 2, 'walk speed': (90, 100), 'run speed': 300, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'fwp', 'armed': False, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables', 'lava'],
    'gender': 'female', 'race': 'miewdra',
    'dialogue': 'CATRINA_DLG', 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': ['white cat'], 'tops': ['red dress top'], 'bottoms': ['blue dress skirt'], 'shoes': ['brown boots'], 'gloves': [None], 'gold': 100, 'items': ['random'], 'magic': [None]},
    'animations': {None}}

PEOPLE['elfvillager'] = {'name': 'Elf Villager', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 0, 'knockback': 2, 'walk speed': (90, 100), 'run speed': 300, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'fwp', 'armed': False, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables', 'lava'],
    'gender': 'random', 'race': 'elf',
    'dialogue': 'random ELF_VILLAGER_DLG', 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': ['random ELFVILLAGER_'], 'tops': ['random ELFVILLAGER_'], 'bottoms': ['random ELFVILLAGER_'], 'shoes': ['random'], 'gloves': [None], 'gold': 100, 'items': ['random'], 'magic': [None]},
    'animations': {None}}
ELFVILLAGER_HAIR = ['brown elf braids', 'blond elf braids', 'white elf braids', 'short brown', 'short blond', 'long black pony', 'long brown side pony', 'long blond side pony']
ELFVILLAGER_TOPS = CASUAL_TOPS_LIST
ELFVILLAGER_BOTTOMS = CASUAL_BOTTOMS_LIST
PEOPLE['elf blacksmith'] = {'name': 'Blacksmith', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 30, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['obstacles', 'vehicles'],
    'gender': 'female', 'race': 'elf',
    'dialogue': 'BLACKSMITH_DLG', 'store': ELF_BLACKSMITH_STORE,
    'inventory': {'weapons': ['steel dagger'], 'hats': ['elf hat'], 'hair': ['white elf braids'], 'tops': ['black racerback tank top'], 'bottoms': ['leather leggings F'], 'shoes': ['brown boots'], 'gloves': ['leather gauntlets'], 'gold': randrange(100, 1000), 'items': ['random'], 'magic': [None]},
    'animations': {None}}

PEOPLE['elfqueen'] = {'name': 'Elf Queen', 'protected': True, 'health': 200, 'touch damage': False, 'damage': 30, 'knockback': 10, 'walk speed': (100, 110), 'run speed': 200, 'detect radius': 500, 'avoid radius': 10, 'aggression': 'sap', 'armed': True, 'dual wield': False,
    'collide': ['obstacles', 'vehicles'],
    'gender': 'female', 'race': 'elf',
    'dialogue': 'ELF_QUEEN_DLG', 'store': None,
    'inventory': {'weapons': ['steel dagger'], 'hats': ['paladin crown'], 'hair': ['white elf braids'], 'tops': ['wedding dress top'], 'bottoms': ['red mini dress skirt'], 'shoes': ['brown boots'], 'gloves': ['dress gloves'], 'gold': randrange(100, 1000), 'items': ['random'], 'magic': [None]},
    'animations': {None}}

PEOPLE['elfguard'] = {'name': 'Elf Guard', 'protected': True, 'health': 400, 'touch damage': False, 'damage': 25, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 200, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'water', 'jumpables', 'climbables'],
    'gender': 'random', 'race': 'elf',
    'dialogue': 'random ELF_GUARD_DLG', 'store': None,
    'inventory': {'weapons': ['random GUARD_'], 'hats': [None], 'hair': ['random ELFVILLAGER_'], 'tops': ['guard armor'], 'bottoms': ['random GUARD_'], 'shoes': ['steel boots'], 'gloves': ['random GUARD_'], 'gold': 250, 'items': ['random'], 'magic': [None]},
    'animations': {None}}

PEOPLE['dangerman'] = {'name': 'Elron Dangerman', 'protected': True, 'health': 800, 'touch damage': False, 'damage': 30, 'knockback': 10, 'walk speed': (20, 25), 'run speed': 160, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'sap', 'armed': True, 'dual wield': False,
    'collide': ['obstacles', 'vehicles'],
    'gender': 'male', 'race': 'elf',
    'dialogue': 'DANGERMAN_DLG', 'store': DANGERMAN_STORE,
    'inventory': {'weapons': [None], 'hats': ['red cloak'], 'hair': ['white beard'], 'tops': ['red mage robe top M'], 'bottoms': ['red mage robe bottom'], 'shoes': ['bronze boots'], 'gloves': [None], 'gold': randrange(1, 10), 'items': ['potato', 'lock pick'], 'magic': [None]},
    'animations': {None}}


PEOPLE['lacertolianvillager'] = {'name': 'Lacertolian Villager', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 0, 'knockback': 2, 'walk speed': (90, 100), 'run speed': 300, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'fwp', 'armed': False, 'dual wield': False,
    'collide': ['vehicles', 'walls', 'jumpables', 'climbables', 'lava'],
    'gender': 'random', 'race': 'lacertolian',
    'dialogue': 'random LACERTOLIAN_VILLAGER_DLG', 'store': None,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': [None], 'tops': ['random VILLAGER_'], 'bottoms': ['random VILLAGER_'], 'shoes': ['random'], 'gloves': [None], 'gold': 100, 'items': ['random'], 'magic': [None]},
    'animations': {None}}
LACERTOLIANVILLAGER_TOPS = CASUAL_TOPS_LIST
LACERTOLIANVILLAGER_BOTTOMS = CASUAL_BOTTOMS_LIST
PEOPLE['lacertolian blacksmith'] = {'name': 'Blacksmith', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 30, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['obstacles', 'vehicles'],
    'gender': 'male', 'race': 'lacertolian',
    'dialogue': 'BLACKSMITH_DLG', 'store': LACERTOLIAN_BLACKSMITH_STORE,
    'inventory': {'weapons': ['steel sword'], 'hats': [None], 'hair': ['lizard spikes'], 'tops': ['leather armor M'], 'bottoms': ['leather leggings M'], 'shoes': [None], 'gloves': ['leather gauntlets'], 'gold': randrange(100, 1000), 'items': ['random'], 'magic': [None]},
    'animations': {None}}
PEOPLE['liz'] = {'name': 'Liz', 'protected': True, 'health': 100, 'touch damage': False, 'damage': 20, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['obstacles', 'vehicles'],
    'gender': 'female', 'race': 'lacertolian',
    'dialogue': 'LIZ_DLG', 'store': LIZ_STORE,
    'inventory': {'weapons': ['iron dagger'], 'hats': [None], 'hair': [None], 'tops': ['pink dress top'], 'bottoms': ['leather leggings F'], 'shoes': [None], 'gloves': [None], 'gold': randrange(100, 1000), 'items': ['random'], 'magic': ['fireball']},
    'animations': {None}}

PEOPLE['mechanima blacksmith'] = {'name': 'Blacksmith', 'protected': True, 'health': 600, 'touch damage': False, 'damage': 30, 'knockback': 10, 'walk speed': (90, 100), 'run speed': 160, 'detect radius': 300, 'avoid radius': 100, 'aggression': 'awp', 'armed': True, 'dual wield': False,
    'collide': ['obstacles', 'vehicles'],
    'gender': 'male', 'race': 'mechanima',
    'dialogue': 'BLACKSMITH_DLG', 'store': MECHANIMA_BLACKSMITH_STORE,
    'inventory': {'weapons': [None], 'hats': [None], 'hair': ['LED skin'], 'tops': ['guard armor'], 'bottoms': ['chainmail leggings M'], 'shoes': ['black combat'], 'gloves': ['steel gauntlets'], 'gold': randrange(100, 1000), 'items': ['random'], 'magic': [None]},
    'animations': {None}}

#Animation patterns:
BASIC3 = [1, 2, 3, 2]
FLY4 = [1, 2, 3, 4, 3, 2]
ANIMAL_ANIMATIONS = {}
ANIMAL_ANIMATIONS['garden lizard'] = {'walk': BASIC3}
ANIMAL_ANIMATIONS['goldfish'] = {'walk':[1, 4, 2, 3, 2, 4]}
ANIMAL_ANIMATIONS['bluefish'] = {'walk':[1, 4, 2, 3, 2, 4]}
ANIMAL_ANIMATIONS['leopard shark'] = {'walk':[1, 2, 3, 2, 1, 4, 5, 4]}
ANIMAL_ANIMATIONS['rabbit'] = {'walk':BASIC3, 'run': [2, 4, 5, 4]}
ANIMAL_ANIMATIONS['chicken'] = {'walk':BASIC3, 'run': [4, 5, 6, 5]}
ANIMAL_ANIMATIONS['pink moth'] = {'walk':BASIC3}
ANIMAL_ANIMATIONS['green moth'] = {'walk':BASIC3}
ANIMAL_ANIMATIONS['brown bird'] = {'walk':BASIC3}
ANIMAL_ANIMATIONS['giant ant'] = {'walk':[1, 2, 3, 2, 1, 4, 5, 6, 5, 4]}
ANIMAL_ANIMATIONS['queen ant'] = {'walk':[1, 2, 3, 2, 1, 4, 5, 6, 5, 4]}
ANIMAL_ANIMATIONS['butterfly ideopsis'] = {'walk':BASIC3}
ANIMAL_ANIMATIONS['sheep'] = {'walk':[1, 2, 3, 2, 1, 4, 5, 4]}
ANIMAL_ANIMATIONS['bighorn sheep'] = {'walk':[1, 2, 3, 2, 1, 4, 5, 4]}
ANIMAL_ANIMATIONS['snake'] = {'walk':[1, 2, 3, 4, 5, 6, 7, 8]}
ANIMAL_ANIMATIONS['horse'] = {'walk':[1, 2, 3, 2, 1, 5, 6, 5], 'run': [1, 2, 3, 4, 3, 2, 1, 5, 6, 7, 6, 5]}
ANIMAL_ANIMATIONS['spider'] = {'walk':BASIC3}
ANIMAL_ANIMATIONS['squid'] = {'walk':BASIC3}
ANIMAL_ANIMATIONS['flying goldfix'] = {'walk':BASIC3}
ANIMAL_ANIMATIONS['marlin'] = {'walk':BASIC3}
ANIMAL_ANIMATIONS['hawk'] = {'walk':BASIC3}
ANIMAL_ANIMATIONS['sea turtle'] = {'walk':BASIC3}
ANIMAL_ANIMATIONS['red wyvern'] = {'walk':FLY4}
ANIMAL_ANIMATIONS['blue wyvern'] = {'walk':FLY4}
ANIMAL_ANIMATIONS['dolphin'] = {'walk':[1, 2, 3, 4, 5, 6, 5, 4, 3, 2]}

ANIMALS = {}
ANIMALS['garden lizard'] = {'name': 'garden lizard', 'corpse': None, 'mountable': False, 'touch damage': False, 'protected': False, 'hit rect': SMALL_HIT_RECT, 'grabable': True, 'run speed': 300, 'walk speed': 250, 'walk animate speed': 80, 'run animate speed': 180, 'detect radius': 500, 'avoid radius': 45,'aggression': 'fwd', 'health': 10, 'damage': 0, 'knockback': 0, 'item type': 'items', 'item': 'live garden lizard', 'dropped items': ['dead garden lizard'], 'collide': ['obstacles', 'vehicles']}
ANIMALS['rabbit'] = {'name': 'rabbit', 'corpse': None, 'mountable': False, 'touch damage': False, 'protected': False, 'hit rect': SMALL_HIT_RECT, 'grabable': True, 'run speed': 400, 'walk speed': 100, 'walk animate speed': 400, 'run animate speed': 240, 'detect radius': 400, 'avoid radius': 100,'aggression': 'fwd', 'health': 25, 'damage': 0, 'knockback': 0, 'item type': 'weapons', 'item': 'live rabbit', 'dropped items': ['dead rabbit'], 'collide': ['obstacles', 'vehicles']}
ANIMALS['chicken'] = {'name': 'chicken', 'corpse': None, 'mountable': False, 'touch damage': False, 'protected': True, 'hit rect': SMALL_HIT_RECT, 'grabable': True, 'run speed': 350, 'walk speed': 50, 'walk animate speed': 400, 'run animate speed': 200, 'detect radius': 300, 'avoid radius': 80, 'aggression': 'fwd', 'health': 20, 'damage': 0, 'knockback': 0, 'item type': 'weapons', 'item': 'live chicken', 'dropped items': ['dead chicken'], 'collide': ['obstacles', 'vehicles']}
ANIMALS['bighorn sheep'] = {'name': 'bighorn sheep', 'corpse': 1, 'mountable': False, 'touch damage': True, 'protected': False, 'hit rect': LARGE_HIT_RECT, 'grabable': False, 'run speed': 480, 'walk speed': 100, 'walk animate speed': 300, 'run animate speed': 120, 'detect radius': 300, 'avoid radius': 300,'aggression': 'fup', 'health': 100, 'damage': 8, 'knockback': 25, 'item type': 'items', 'item': 'sheep meat', 'dropped items': ['sheep meat', 'sheep skin', 'sheep horn', 'sheep horn'], 'collide': ['vehicles', 'walls', 'water', 'jumpables', 'climbables']}
ANIMALS['sheep'] = {'name': 'sheep', 'corpse': 3, 'mountable': False, 'touch damage': False, 'protected': True, 'hit rect': LARGE_HIT_RECT, 'grabable': False, 'run speed': 200, 'walk speed': 100, 'walk animate speed': 300, 'run animate speed': 200, 'detect radius': 300, 'avoid radius': 300,'aggression': 'fwd', 'health': 50, 'damage': 0, 'knockback': 0, 'item type': 'items', 'item': 'sheep meat', 'dropped items': ['sheep meat', 'sheep skin'], 'collide': ['obstacles', 'vehicles']}
ANIMALS['horse'] = {'name': 'horse', 'corpse': 4, 'mountable': True, 'touch damage': False, 'protected': False, 'hit rect': LARGE_HIT_RECT, 'grabable': False, 'run speed': 480, 'walk speed': 100, 'walk animate speed': 300, 'run animate speed': 100, 'detect radius': 300, 'avoid radius': 300,'aggression': 'fwp', 'health': 280, 'damage': 8, 'knockback': 25, 'item type': 'items', 'item': 'sheep meat', 'dropped items': ['horse skin', 'horse meat'], 'collide': ['vehicles', 'walls', 'water', 'jumpables', 'climbables']}

ANIMALS['red wyvern'] = {'name': 'red wyvern', 'flying': True, 'magic': ['fireball'], 'corpse': 13, 'mountable': False, 'touch damage': False, 'protected': False, 'hit rect': MEDIUM_HIT_RECT, 'grabable': False, 'run speed': 300, 'walk speed': 180, 'walk animate speed': 80, 'run animate speed': 60, 'detect radius': 500, 'avoid radius': 200,'aggression': 'awd', 'health': 260, 'damage': 0, 'knockback': 0, 'item type': 'items', 'item': 'live brown bird', 'dropped items': ['dragon spit', 'red wyvern skin', 'wyvern meat'], 'collide': ['walls']}
ANIMALS['blue wyvern'] = {'name': 'blue wyvern', 'flying': True, 'magic': ['fireball'], 'corpse': 12, 'mountable': False, 'touch damage': False, 'protected': False, 'hit rect': MEDIUM_HIT_RECT, 'grabable': False, 'run speed': 300, 'walk speed': 180, 'walk animate speed': 80, 'run animate speed': 60, 'detect radius': 500, 'avoid radius': 200,'aggression': 'awd', 'health': 260, 'damage': 0, 'knockback': 0, 'item type': 'items', 'item': 'live brown bird', 'dropped items': ['dragon spit', 'blue wyvern skin', 'wyvern meat'], 'collide': ['walls']}
ANIMALS['brown bird'] = {'name': 'brown bird', 'flying': True, 'corpse': None, 'mountable': False, 'touch damage': False, 'protected': False, 'hit rect': SMALL_HIT_RECT, 'grabable': True, 'run speed': 400, 'walk speed': 220, 'walk animate speed': 80, 'run animate speed': 60, 'detect radius': 200, 'avoid radius': 80,'aggression': 'fwd', 'health': 6, 'damage': 0, 'knockback': 0, 'item type': 'items', 'item': 'live brown bird', 'dropped items': ['dead brown bird'], 'collide': ['walls']}
ANIMALS['hawk'] = {'name': 'hawk', 'flying': True, 'corpse': None, 'mountable': False, 'touch damage': False, 'protected': False, 'hit rect': SMALL_HIT_RECT, 'grabable': False, 'run speed': 400, 'walk speed': 350, 'walk animate speed': 180, 'run animate speed': 160, 'detect radius': 600, 'avoid radius': 80,'aggression': 'fwd', 'health': 6, 'damage': 0, 'knockback': 0, 'item type': 'items', 'item': 'live brown bird', 'dropped items': ['dead hawk'], 'collide': ['walls']}
ANIMALS['pink moth'] = {'name': 'pink moth', 'flying': True, 'corpse': None, 'mountable': False, 'touch damage': False, 'protected': False, 'hit rect': SMALL_HIT_RECT, 'grabable': True, 'run speed': 300, 'walk speed': 80, 'walk animate speed': 100, 'run animate speed': 80, 'detect radius': 200, 'avoid radius': 80,'aggression': 'fwd', 'health': 5, 'damage': 0, 'knockback': 0, 'item type': 'items', 'item': 'live pink moth', 'dropped items': ['dead pink moth'], 'collide': ['walls']}
ANIMALS['green moth'] = {'name': 'green moth', 'flying': True, 'corpse': None, 'mountable': False, 'touch damage': False, 'protected': False, 'hit rect': SMALL_HIT_RECT, 'grabable': True, 'run speed': 300, 'walk speed': 80, 'walk animate speed': 100, 'run animate speed': 80, 'detect radius': 200, 'avoid radius': 80,'aggression': 'fwd', 'health': 5, 'damage': 0, 'knockback': 0, 'item type': 'items', 'item': 'live green moth', 'dropped items': ['dead green moth'], 'collide': ['walls']}
ANIMALS['butterfly ideopsis'] = {'name': 'butterfly ideopsis', 'flying': True, 'corpse': None, 'mountable': False, 'touch damage': False, 'protected': False, 'hit rect': SMALL_HIT_RECT, 'grabable': True, 'run speed': 300, 'walk speed': 80, 'walk animate speed': 100, 'run animate speed': 80, 'detect radius': 200, 'avoid radius': 80,'aggression': 'fwd', 'health': 5, 'damage': 0, 'knockback': 0, 'item type': 'items', 'item': 'live butterfly ideopsis', 'dropped items': ['dead butterfly ideopsis'], 'collide': ['walls']}
ANIMALS['flying goldfix'] = {'name': 'flying goldfix', 'flying': True, 'corpse': None, 'mountable': False, 'touch damage': False, 'protected': False, 'hit rect': SMALL_HIT_RECT, 'grabable': True, 'run speed': 300, 'walk speed': 100, 'walk animate speed': 80, 'run animate speed': 70, 'detect radius': 200, 'avoid radius': 80,'aggression': 'fwd', 'health': 5, 'damage': 0, 'knockback': 0, 'item type': 'items', 'item': 'live goldfish', 'dropped items': ['dead goldfish'], 'collide': ['walls']}

ANIMALS['giant ant'] = {'name': 'giant ant', 'corpse': None, 'mountable': False, 'touch damage': True, 'protected': False, 'hit rect': SMALL_HIT_RECT, 'grabable': False, 'run speed': 400, 'walk speed': 100, 'walk animate speed': 150, 'run animate speed': 100, 'detect radius': 180, 'avoid radius': 60,'aggression': 'awd', 'health': 100, 'damage': 10, 'knockback': 2, 'item type': 'items', 'item': 'dead giant ant', 'dropped items': ['dead giant ant'], 'collide': ['obstacles', 'vehicles']}
ANIMALS['queen ant'] = {'name': 'queen ant', 'corpse': None, 'mountable': False, 'touch damage': True, 'protected': False, 'hit rect': MEDIUM_HIT_RECT, 'grabable': False, 'run speed': 600, 'walk speed': 200, 'walk animate speed': 150, 'run animate speed': 100, 'detect radius': 512, 'avoid radius': 150,'aggression': 'awd', 'health': 1500, 'damage': 25, 'knockback': 6, 'item type': 'items', 'item': 'dead giant ant', 'dropped items': ['ant exoskeleton shell','queen ant leg','queen ant leg','queen ant leg','queen ant leg','queen ant leg','queen ant leg', 'ant helmet', 'giant ant eggs'], 'collide': ['obstacles', 'vehicles']}
ANIMALS['snake'] = {'name': 'snake', 'corpse': None, 'mountable': False, 'touch damage': True, 'protected': False, 'hit rect': SMALL_HIT_RECT, 'grabable': False, 'run speed': 280, 'walk speed': 50, 'walk animate speed': 300, 'run animate speed': 90, 'detect radius': 140, 'avoid radius': 60,'aggression': 'fup', 'health': 100, 'damage': 10, 'knockback': 1, 'item type': 'items', 'item': 'dead snake', 'dropped items': ['dead snake'], 'collide': ['walls', 'vehicles']}
ANIMALS['spider'] = {'name': 'spider', 'corpse': 6, 'mountable': True, 'touch damage': True, 'protected': False, 'hit rect': MEDIUM_HIT_RECT, 'grabable': False, 'run speed': 300, 'walk speed': 150, 'walk animate speed': 150, 'run animate speed': 100, 'detect radius': 280, 'avoid radius': 80,'aggression': 'awp', 'health': 200, 'damage': 15, 'knockback': 10, 'item type': 'items', 'item': 'dead giant ant', 'dropped items': ['spider venom'], 'collide': ['walls', 'vehicles', 'water']}

ANIMALS['goldfish'] = {'name': 'goldfish', 'corpse': None, 'mountable': False, 'touch damage': False, 'protected': False, 'hit rect': SMALL_HIT_RECT,'grabable': True, 'run speed': 350, 'walk speed': 50, 'walk animate speed': 400, 'run animate speed': 180, 'detect radius': 400, 'avoid radius': 40, 'aggression': 'fwd', 'health': 10, 'damage': 0, 'knockback': 0, 'item type': 'weapons', 'item': 'live goldfish', 'dropped items': ['dead goldfish'], 'collide': ['walls', 'shallows', 'jumpables', 'climbables', 'lava']}
ANIMALS['bluefish'] = {'name': 'bluefish', 'corpse': None, 'mountable': False, 'touch damage': False, 'protected': False, 'hit rect': SMALL_HIT_RECT,'grabable': True, 'run speed': 400, 'walk speed': 60, 'walk animate speed': 400, 'run animate speed': 160, 'detect radius': 400, 'avoid radius': 40, 'aggression': 'fwd', 'health': 13, 'damage': 0, 'knockback': 0, 'item type': 'weapons', 'item': 'live bluefish', 'dropped items': ['dead bluefish'], 'collide': ['walls', 'shallows', 'jumpables', 'climbables', 'lava']}
ANIMALS['leopard shark'] = {'name': 'leopard shark', 'corpse': None, 'mountable': False, 'touch damage': True, 'protected': False, 'hit rect': MEDIUM_HIT_RECT,'grabable': False, 'run speed': 400, 'walk speed': 100, 'walk animate speed': 200, 'run animate speed': 100, 'detect radius': 400, 'avoid radius': 40, 'aggression': 'awd', 'health': 55, 'damage': 4, 'knockback': 1, 'item type': 'items', 'item': 'dead leopard shark', 'dropped items': ['dead leopard shark'], 'collide': ['walls', 'shallows', 'jumpables', 'climbables', 'lava']}
ANIMALS['squid'] = {'name': 'squid', 'corpse': 5, 'mountable': True, 'touch damage': True, 'protected': False, 'hit rect': MEDIUM_HIT_RECT,'grabable': False, 'run speed': 400, 'walk speed': 100, 'walk animate speed': 200, 'run animate speed': 100, 'detect radius': 400, 'avoid radius': 40, 'aggression': 'awp', 'health': 250, 'damage': 18, 'knockback': 15, 'item type': 'items', 'item': 'dead leopard shark', 'dropped items': ['squid ink', 'squid eye', 'squid tentacle'], 'collide': ['walls', 'shallows', 'jumpables', 'climbables', 'lava']}
ANIMALS['marlin'] = {'name': 'marlin', 'corpse': 7, 'mountable': False, 'touch damage': True, 'protected': False, 'hit rect': MEDIUM_HIT_RECT,'grabable': False, 'run speed': 450, 'walk speed': 250, 'walk animate speed': 200, 'run animate speed': 100, 'detect radius': 400, 'avoid radius': 40, 'aggression': 'awp', 'health': 150, 'damage': 15, 'knockback': 50, 'item type': 'items', 'item': 'dead leopard shark', 'dropped items': ['marlin meat', 'marlin meat'], 'collide': ['walls', 'shallows', 'jumpables', 'climbables', 'lava']}
ANIMALS['sea turtle'] = {'name': 'sea turtle', 'corpse': None, 'mountable': True, 'touch damage': False, 'protected': False, 'hit rect': MEDIUM_HIT_RECT,'grabable': False, 'run speed': 200, 'walk speed': 100, 'walk animate speed': 200, 'run animate speed': 100, 'detect radius': 400, 'avoid radius': 100, 'aggression': 'fwp', 'health': 350, 'damage': 18, 'knockback': 0, 'item type': 'items', 'item': 'dead leopard shark', 'dropped items': [None], 'collide': ['walls', 'vehicles', 'jumpables', 'climbables', 'lava']}
ANIMALS['dolphin'] = {'name': 'dolphin', 'corpse': 14, 'mountable': True, 'touch damage': False, 'protected': False, 'hit rect': LARGE_HIT_RECT,'grabable': False, 'run speed': 600, 'walk speed': 300, 'walk animate speed': 80, 'run animate speed': 60, 'detect radius': 400, 'avoid radius': 200, 'aggression': 'fwp', 'health': 200, 'damage': 18, 'knockback': 0, 'item type': 'items', 'item': 'dead leopard shark', 'dropped items': ['dolphin meat', 'dolphin meat', 'whale oil', 'whale oil', 'whale oil'], 'collide': ['walls', 'vehicles', 'jumpables', 'climbables', 'lava', 'shallows']}


MOUNTAIN_ANIMALS = ['blue wyvern', 'brown bird', 'goblin', 'rabbit', 'pink moth', 'green moth', 'butterfly ideopsis', 'giant ant', 'bighorn sheep', 'snake', 'garden lizard']
FOREST_ANIMALS = ['blue wyvern', 'red wyvern', 'brown bird', 'goblin', 'rabbit', 'pink moth', 'green moth', 'butterfly ideopsis', 'giant ant', 'garden lizard', 'spider', 'hawk']
GRASSLAND_ANIMALS = ['red wyvern', 'goblin', 'brown bird', 'rabbit', 'pink moth', 'green moth', 'butterfly ideopsis', 'giant ant', 'garden lizard', 'hawk']
BEACH_ANIMALS = ['brown bird', 'vadashay', 'bluefish', 'butterfly ideopsis', 'leopard shark', 'pink moth', 'garden lizard', 'flying goldfix', 'sea turtle']
OCEAN_ANIMALS = ['dolphin', 'vadashay', 'bluefish', 'leopard shark', 'squid', 'marlin', 'sea turtle']
ZOMBIELAND_ANIMALS = ['brown bird', 'immortui', 'immortui', 'immortui', 'rabbit', 'pink moth', 'green moth', 'giant ant', 'chicken', 'garden lizard']
TOWN_ANIMALS = ['brown bird', 'rabbit', 'pink moth', 'green moth', 'butterfly ideopsis', 'garden lizard']
TUNDRA_ANIMALS = ['rabbit', 'ice golem']
DESERT_ANIMALS = ['red wyvern', 'demon', 'giant ant', 'snake', 'garden lizard', 'spider', 'hawk']
