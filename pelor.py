#!/usr/bin/python

import MySQLdb as mysql
import MySQLdb.cursors
import cmd, sys

# Open database connection
db = mysql.Connection(host="localhost", user="fred", passwd="beamer1833", db="srd35")
cursor = db.cursor()

# Queries the database for class information
def queryClass(_name):
    global db
    global cursor
    _table = "class"
    sql = ("SELECT "
               "name, "
               "type, "
               "hit_die, "
               "class_skills, "
               "skill_points, "
               "spell_stat, "
               "proficiencies, "
               "IFNULL(req_race, NULL) AS req_race, "
               "IFNULL(req_weapon_proficiency, NULL) AS req_weapon_proficiency, "
               "IFNULL(req_base_attack_bonus, NULL) AS req_base_attack_bonus, "
               "IFNULL(req_skill, NULL) AS req_skill, "
               "IFNULL(req_feat, NULL) AS req_feat, "
               "IFNULL(req_spells, NULL) AS req_spells, "
               "IFNULL(req_languages, NULL) AS req_languages, "
               "IFNULL(req_psionics, NULL) AS req_psionics, "
               "IFNULL(req_epic_feat, NULL) AS req_epic_feat, "
               "IFNULL(req_special, NULL) AS req_special "
           "FROM ") + _table + (" "
           "WHERE name =\"") + _name + "\";"
    columns = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            for index in range(len(row)):
                if row[index]:
                    columns.append((cursor.description[index][0],str(row[index])))
    except:
        print "Error: unable to fetch data."
    return columns

# Queries the database for domain information
def queryDomain(_name):
    global db
    global cursor
    _table = "domain"
    sql = ("SELECT "
               "name, "
               "granted_powers, "
               "spell_1, "
               "spell_2, "
               "spell_3, "
               "spell_4, "
               "spell_5, "
               "spell_6, "
               "spell_7, "
               "spell_8, "
               "spell_9 "
           "FROM ") + _table + (" "
           "WHERE name =\"") + _name + "\";"
    columns = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            for index in range(len(row)):
                if row[index]:
                    columns.append((cursor.description[index][0],str(row[index])))
    except:
        print "Error: unable to fetch data."
    return columns

# Queries the database for equipment information
def queryEquipment(_name):
    global db
    global cursor
    _table = "equipment"
    sql = ("SELECT "
               "name "
           "FROM ") + _table + (" "
           "WHERE name =\"") + _name + "\";"
    columns = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            for index in range(len(row)):
                if row[index]:
                    columns.append((cursor.description[index][0],str(row[index])))
    except:
        print "Error: unable to fetch data."
    return columns
 
# Queries the database for feat information
def queryFeat(_name):
    global db
    global cursor
    _table = "feat"
    sql = ("SELECT "
               "name "
           "FROM ") + _table + (" "
           "WHERE name =\"") + _name + "\";"
    columns = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            for index in range(len(row)):
                if row[index]:
                    columns.append((cursor.description[index][0],str(row[index])))
    except:
        print "Error: unable to fetch data."
    return columns 

# Queries the database for item information
def queryItem(_name):
    global db
    global cursor
    _table = "item"
    sql = ("SELECT "
               "name "
           "FROM ") + _table + (" "
           "WHERE name =\"") + _name + "\";"
    columns = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            for index in range(len(row)):
                if row[index]:
                    columns.append((cursor.description[index][0],str(row[index])))
    except:
        print "Error: unable to fetch data."
    return columns

# Queries the database for monster information
def queryMonster(_name):
    global db
    global cursor
    _table = "monster"
    sql = ("SELECT "
               "name, "
               "hit_dice, "
               "armor_class "
           "FROM ") + _table + (" "
           "WHERE name =\"") + _name + "\";"
    columns = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            for index in range(len(row)):
                if row[index]:
                    columns.append((cursor.description[index][0],str(row[index])))
    except:
        print "Error: unable to fetch data."
    return columns

# Queries the database for power information
def queryPower(_name):
    global db
    global cursor
    _table = "power"
    sql = ("SELECT "
               "name "
           "FROM ") + _table + (" "
           "WHERE name =\"") + _name + "\";"
    columns = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            for index in range(len(row)):
                if row[index]:
                    columns.append((cursor.description[index][0],str(row[index])))
    except:
        print "Error: unable to fetch data."
    return columns

# Queries the database for skill information
def querySkill(_name):
    global db
    global cursor
    _table = "skill"
    sql = ("SELECT "
               "name "
           "FROM ") + _table + (" "
           "WHERE name =\"") + _name + "\";"
    columns = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            for index in range(len(row)):
                if row[index]:
                    columns.append((cursor.description[index][0],str(row[index])))
    except:
        print "Error: unable to fetch data."
    return columns

# Queries the database for spell information
def querySpell(_name):
    global db
    global cursor
    _table = "spell"
    sql = ("SELECT "
               "name "
           "FROM ") + _table + (" "
           "WHERE name =\"") + _name + "\";"
    columns = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            for index in range(len(row)):
                if row[index]:
                    columns.append((cursor.description[index][0],str(row[index])))
    except:
        print "Error: unable to fetch data."
    return columns

# Queries the database for the columns of a table
def queryColumns(_table):
    global db
    global cursor
    sql = "SHOW columns FROM " + _table + ";"
    columns = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            columns.append(str(row[0]))
    except:
       print "Error: unable to fetch data."
    return columns

# Queries the database for the names of a table
def queryList(_table):
    global db
    global cursor
    sql = "SELECT name FROM " + _table + ";"
    names = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            names.append(str(row[0]))
    except:
       print "Error: unable to fetch data."
    return names

# class for command-line interpreter
class PelorShell(cmd.Cmd):

    intro = "\nHail Pelor!\nType 'help' or '?' to list commands.\nType 'quit' or 'exit' to escape.\n"
    prompt = "pelor ~ $ "
    ruler = "-"
        
    # ----- Commands -----
    #| class           |
    #| class_table     |
    #| domain          |
    #| equipment       |
    #| feat            |
    #| item            |
    #| monster         |
    #| power           |
    #| skill           |
    #| spell           |

    # class
    def do_class(self, arg):
        if arg == "":
            print "\n".join(queryList("class"))
        else:
            for attribute in queryClass(str(arg)):
                print "> " + attribute[0].replace("_", " ").capitalize() + ": " + attribute[1]
    def help_class(self):
        print "Queries for information about classes."
    def complete_class(self, text, line, begidx, endidx):
        options = queryList("class")
        if text:
            return [i for i in options if i.startswith(text)]
        else:
            return options

    # domain
    def do_domain(self, arg):
        if arg == "":
            print "\n".join(queryList("domain"))
        else:
             for attribute in queryDomain(str(arg)):
                print "> " + attribute[0].replace("_", " ").capitalize() + ": " + attribute[1]
    def help_domain(self):
        print "Queries for information about domains."
    def complete_domain(self, text, line, begidx, endidx):
        options = queryList("domain")
        if text:
            return [i for i in options if i.startswith(text)]
        else:
            return options

    # equipment
    def do_equipment(self, arg):
        if arg == "":
            print "\n".join(queryList("equipment"))
        else:
             for attribute in queryEquipment(str(arg)):
                print "> " + attribute[0].replace("_", " ").capitalize() + ": " + attribute[1]
    def help_equipment(self):
        print "Queries for information about equipments."
    def complete_equipment(self, text, line, begidx, endidx):
        options = queryList("equipment")
        if text:
            return [i for i in options if i.startswith(text)]
        else:
            return options

    # feat
    def do_feat(self, arg):
        if arg == "":
            print "\n".join(queryList("feat"))
        else:
             for attribute in queryFeat(str(arg)):
                print "> " + attribute[0].replace("_", " ").capitalize() + ": " + attribute[1]
    def help_feat(self):
        print "Queries for information about feats."
    def complete_feat(self, text, line, begidx, endidx):
        options = queryList("feat")
        if text:
            return [i for i in options if i.startswith(text)]
        else:
            return options

    # item
    def do_item(self, arg):
        if arg == "":
            print "\n".join(queryList("item"))
        else:
             for attribute in queryItem(str(arg)):
                print "> " + attribute[0].replace("_", " ").capitalize() + ": " + attribute[1]
    def help_item(self):
        print "Queries for information about items."
    def complete_item(self, text, line, begidx, endidx):
        options = queryList("item")
        if text:
            return [i for i in options if i.startswith(text)]
        else:
            return options

    # monster
    def do_monster(self, arg):
        if arg == "":
            print "\n".join(queryList("monster"))
        else:
             for attribute in queryMonster(str(arg)):
                print "> " + attribute[0].replace("_", " ").capitalize() + ": " + attribute[1]
    def help_monster(self):
        print "Queries for information about monsters."
    def complete_monster(self, text, line, begidx, endidx):
        options = queryList("monster")
        if text:
            return [i for i in options if i.startswith(text)]
        else:
            return options

    # power
    def do_power(self, arg):
        if arg == "":
            print "\n".join(queryList("power"))
        else:
             for attribute in queryPower(str(arg)):
                print "> " + attribute[0].replace("_", " ").capitalize() + ": " + attribute[1]
    def help_power(self):
        print "Queries for information about powers."
    def complete_power(self, text, line, begidx, endidx):
        options = queryList("power")
        if text:
            return [i for i in options if i.startswith(text)]
        else:
            return options

    # skill
    def do_skill(self, arg):
        if arg == "":
            print "\n".join(queryList("skill"))
        else:
             for attribute in querySkill(str(arg)):
                print "> " + attribute[0].replace("_", " ").capitalize() + ": " + attribute[1]
    def help_skill(self):
        print "Queries for information about skills."
    def complete_skill(self, text, line, begidx, endidx):
        options = queryList("skill")
        if text:
            return [i for i in options if i.startswith(text)]
        else:
            return options

    # spell
    def do_spell(self, arg):
        if arg == "":
            print "\n".join(queryList("spell"))
        else:
             for attribute in querySpell(str(arg)):
                print "> " + attribute[0].replace("_", " ").capitalize() + ": " + attribute[1]
    def help_spell(self):
        print "Queries for information about spells."
    def complete_spell(self, text, line, begidx, endidx):
        options = queryList("spell")
        if text:
            return [i for i in options if i.startswith(text)]
        else:
            return options

    # exit
    def do_exit(self, s):
        return True
    def help_exit(self):
        print "Quit the interpreter."
        
    # quit
    do_quit = do_exit
    help_quit= help_exit

    # ----- Properties -----
    
    # If empty line is entered just ignore it
    def emptyline(self):
        pass
        
    # Allows exiting from shell
    def can_exit(self):
        # disconnect from server
        db.close()
        return True

if __name__ == "__main__":
    shell = PelorShell()
    shell.cmdloop()
