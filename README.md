Pelor
=====

Command line reference tool for Dungeons and Dragons 3.5.

Pelor is a CLI python tool to easily reference Dungeons and Dragons 3.5 documents. Also, God of the Sun.

Requires Python, MySQL, and complete unyielding loyalty.


Query-able Things
-----

class, class_table, domain, equipment, feat, item, monster, power, skill, spell

Example Usage:
-----

monsters - shows all monsters

monsters.where(hit_die = 5) - shows all monsters with hit die 5

monsters.find(“werewolf_lord”).attacks - lists attacks

monsters.where(hit_die = 5).rand - returns random monster with hit die 5
