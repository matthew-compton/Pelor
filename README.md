Pelor
=====

Command line reference tool for Dungeons and Dragons 3.5.

Pelor is a CLI python tool to easily reference Dungeons and Dragons 3.5 documents. Also, God of the Sun.

Requires Python 2.7+ and complete unyielding loyalty.


Query-able Things
-----

class, class_table, domain, equipment, feat, item, monster, power, skill, spell

Example Usage:
-----

Monsters - shows all monsters

Monsters.where(hit_die = 5) - shows all monsters with hit die 5

Monsters.find(“werewolf_lord”).attacks - lists attacks

Monsters.where(hit_die = 5).rand - returns random monster with hit die 5
