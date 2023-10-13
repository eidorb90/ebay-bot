import random
import string
lowercase = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
uppercase = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"


def firstName():
    names=('Mosley','Alpers','Jackson','Emma','Liam','Olivia','Noah','Ava','Ethan','Isabella','Lucas','Mia','Aiden','Sophia'
           ,'Caden','Chloe','Logan','Lily','Mason','Grace','Carter','Zoe','Owen','Emily','Elijah','Abigail','Brayden','Madison'
           ,'Henry','Ella','Michael','Scarlett','James','Hannah','Benjamin','Avery','William','Addison','Alexander','Aubrey'
           ,'Sebastian','Riley','Daniel','Layla','Matthew','Natalie','David','Aria','Joseph','Sofia','Samuel','Avery','Gabriel'
           ,'Hazel','Eli','Evelyn','Jack','Victoria','Christopher','Aurora','Andrew','Luna','Nicholas','Stella','John','Skylar'
           ,'Joshua','Nora','Dylan','Paisley','Christopher','Aria','Ryan','Brooklyn','Nathan','Savannah','Christian','Claire',
           'Hunter','Leah','Isaac','Audrey','Jonathan','Penelope','Caleb','Lillian','Samuel','Grace','Luke','Bella','Isaiah',
           'Ruby','Isaiah','Ellie','Thomas','Lucy','Evan','Lyla','Connor','Scarlett','Landon','Haley','Gavin','Kennedy','Miles'
           ,'Violet','Cameron','Eleanor','Liam','Samantha','Asher','Nova','Nolan','Layla','Ezra','Aria','Elliot','Avery','Oliver'
           ,'Chloe','Carter','Grace','Henry','Zoe','Levi','Scarlett','Lucas','Hazel','Mason','Emma','Wyatt','Lily','Jackson',
           'Madison','Elijah','Aubrey','Owen','Charlotte','Benjamin','Natalie','Noah','Aurora','Matthew','Luna','Nicholas','Skylar'
           ,'Olivia','James','Penelope','Sebastian','Sophia','Logan','Hannah','Gabriel','Stella','David','Claire','Eli','Sofia',
           'Evan','Victoria','Michael','Aria','Daniel','Emily','William','Ella','Avery','Joseph','Addison','Christopher','Isabella'
           ,'Samuel','Layla','Jack','Mia','Andrew','Aubrey','Joshua','Scarlett','Nora','Ryan','Aria','Eleanor','Brooklyn','Hunter',
           'Madison','Lucy','Christian','Ruby','Cameron','Aurora','Luke','Evelyn','Isaiah','Lyla','Thomas','Paisley','Eli','Natalie'
           ,'Lucas','Leah','Miles','Audrey','Gavin','Claire','Kennedy','Lillian','Violet','Samuel','Eleanor','Isaiah','Grace','Oliver'
           ,'Chloe','Ezra','Samantha','Asher','Nova','Nolan','Layla','Ella','Elliot','Emma','Avery','Aria','Zoe','Henry','Carter',
           'Lucas','Olivia','Liam','Scarlett','Mason','Chloe','Hazel','Logan','Grace','Natalie','Levi','Madison','Elijah','Aubrey'
           ,'Owen','Charlotte','Benjamin','Stella','Luna','Nicholas','Aurora','Matthew','Sophia','Gabriel','Skylar','James','Claire'
           ,'Eli','David','Sofia','Michael','Victoria','Aria','Andrew','Christopher','Avery','Isabella','Joseph','Emily','Layla',
           'Samuel','Mia','Jack','Addison','Joshua','Nora','Ryan','Christian','Aubrey','Eleanor','Brooklyn','Lucy','Hunter','Ruby'
           ,'Cameron','Aurora','Luke','Paisley','Isaiah','Evelyn','Lyla','Thomas','Audrey','Gavin','Leah','Claire','Miles','Kennedy'
           ,'Lillian','Violet','Samuel','Isaiah','Eleanor','Grace','Oliver','Chloe','Ezra','Samantha','Asher','Nova','Nolan',
           'Layla','Ella','Elliot','Emma','Avery','Aria','Zoe','Henry','Carter','Lucas','Olivia','Liam','Scarlett','Mason','Chloe'
           ,'Hazel','Logan','Grace','Natalie','Levi','Madison','Elijah','Aubrey','Owen','Charlotte','Benjamin','Stella','Luna',
           'Nicholas','Aurora','Matthew','Sophia','Gabriel','Skylar','James','Claire','Eli','David','Sofia','Michael','Victoria',
           'Aria','Andrew','Christopher','Avery','Isabella','Joseph','Emily','Layla','Samuel','Mia','Jack','Addison','Joshua','Nora',
           'Ryan','Christian','Aubrey','Eleanor','Brooklyn','Lucy','Hunter','Ruby','Cameron','Aurora','Luke','Paisley','Isaiah','Evelyn'
           ,'Lyla','Thomas','Audrey','Gavin','Leah','Claire','Miles','Kennedy','Lillian','Violet','Samuel','Isaiah','Eleanor')
    
    firstName = random.choice(names)
    return firstName

def lastName():
    names=('Johnson','Smith','Brown','Davis','Wilson','Anderson','Garcia','Martinez','Jones','Williams','Rodriguez','Lopez','Gonzalez'
           ,'Hernandez','Walker','Perez','Hall','Young','King','Wright','Scott','Green','Evans','Turner','Reed','Harris','Lee','White'
           ,'Clark','Lewis','Lewis','Adams','Baker','Roberts','Bell','Ross','Watson','Carter','Cruz','Edwards','Collins','Morgan','Murphy'
           ,'Murphy','Gomez','Perry','Powell','Cook','Jenkins','Gray','Russell','Stewart','Sullivan','Smith','Cox','Campbell','Richards',
           'Russell','Bennett','Coleman','Mason','Washington','Kennedy','Bailey','Shaw','Diaz','Barnes','Griffin','Hayes','Nguyen','Russell'
           ,'Rogers','Butler','Ross','Harrison','Foster','Scott','Perez','Peterson','Brooks','Ward','Simmons','Bryant','Griffin','Hayes',
           'Russell','Alexander','Reyes','Long','Patterson','Flores','Reed','Johnson','Hughes','Phillips','Ramirez','Williams','Hill',
           'Mitchell','Bennett','Turner','Morgan','Harris','Cook','James','Bell','Gonzalez','Parker','Howard','Morales','Rivera','Scott'
           ,'Jackson','Wright','Adams','Cruz','Roberts','Rogers','Mendoza','Murray','Hughes','Nguyen','Gomez','Torres','Scott','Bryant',
           'Murphy','Garcia','Price','Watson','Perry','Thomas','Russell','Foster','Nelson','Hernandez','Brooks','Green','Ward','Wood',
           'Collins','King','Phillips','Lee','Sanders','Ramirez','Reyes','Sanders','Smith','Patterson','Long','Williams','Anderson',
           'Carter','Davis','Hall','Brown','Perez','Evans','Gonzalez','Johnson','Wilson','Martinez','Turner','Adams','Jones','Scott',
           'Cook','Bell','White','Harris','Roberts','Thompson','Parker','Hernandez','Thomas','Davis','Lee','Morgan','Jackson','Baker',
           'Stewart','Murphy','Gray','Collins','Murray','Bryant','Smith','Kennedy','Kennedy','King','Reed','Wood','Wright','Howard',
           'Harrison','Jenkins','Reyes','Mendoza','Mendoza','Nguyen','Peterson','Mitchell','Johnson','Hall','Wilson','Smith','Young',
           'Turner','King','Garcia','Martinez','Jones','Williams','Rodriguez','Lopez','Gonzalez','Hernandez','Walker','Perez','Hall',
           'Young','King','Wright','Scott','Green','Evans','Turner','Reed','Harris','Lee','White','Clark','Lewis','Lewis','Adams','Baker',
           'Roberts','Bell','Ross','Watson','Carter','Cruz','Edwards','Collins','Morgan','Murphy','Murphy','Gomez','Perry','Powell','Cook',
           'Jenkins','Gray','Russell','Stewart','Sullivan','Smith','Cox','Campbell','Richards','Russell','Bennett','Coleman','Mason',
           'Washington','Kennedy','Bailey','Shaw','Diaz','Barnes','Griffin','Hayes','Nguyen','Russell','Rogers','Butler','Ross','Harrison',
           'Foster','Scott','Perez','Peterson','Brooks','Ward','Simmons','Bryant','Griffin','Hayes','Russell','Alexander','Reyes','Long',
           'Patterson','Flores','Reed','Johnson','Hughes','Phillips','Ramirez','Williams','Hill','Mitchell','Bennett','Turner','Morgan',
           'Harris','Cook','James','Bell','Gonzalez','Parker','Howard','Morales','Rivera','Scott','Jackson','Wright','Adams','Cruz','Roberts'
           ,'Rogers','Mendoza','Murray','Hughes','Nguyen','Gomez','Torres','Scott','Bryant','Murphy','Garcia','Price','Watson','Perry','Thomas'
           ,'Russell','Foster','Nelson','Hernandez','Brooks','Green','Ward','Wood','Collins','King','Phillips','Lee','Sanders','Ramirez','Reyes'
           ,'Sanders','Smith','Patterson','Long','Williams','Anderson','Carter','Davis','Hall','Brown','Perez','Evans','Gonzalez','Johnson',
           'Wilson','Martinez','Turner','Adams','Jones','Scott','Cook','Bell','White','Harris','Roberts','Thompson','Parker','Hernandez','Thomas'
           ,'Davis','Lee','Morgan','Jackson','Baker','Stewart','Murphy','Gray','Collins','Murray','Bryant','Smith','Kennedy','Kennedy','King',
           'Reed','Wood','Wright','Howard','Harrison','Jenkins','Reyes','Mendoza','Mendoza','Nguyen','Peterson','Mitchell')

    lastName = random.choice(names)
    return lastName

def address():
    lowercase = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
    uppercase = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    return

def password():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(12, 16)
    password = (''.join(random.choice(chars) for x in range(size)))
    return password


        
