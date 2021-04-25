"""A file containing all of the data to be used with the PCSG server"""
import json
from os import path
from time import ctime 

guild_id = 693608235835326464

all_roles = {
    "CAPE": 764214191782756392,
    "CSEC": 764214207192760401,
    "PENDING_MEMBER": 830907979301388368,
    "FAMILY": 755633133600112651,
    "NEWBIE": 762190942316134400,
    "SEASONED": 762192895477415966,
    "EXPERIENCED": 762192810924441610,
    "ADVANCED": 762870198481977375,
    "ELITIST": 762193027979542581,
    "MUTED": 701972373053636649,
    "STAGE_0": 834837579433115709,
    "STAGE_1": 785341063984316476, 
    "STAGE_2": 834837741937098823,
    "STAGE_3": 834838252670025769,
    "STAGE_4_CSEC": 834838264581587055,
    "STAGE_4_CAPE": 834838268150415370
}

register_channels = {
    700174264782815232: "COUNTRIES",
    762068609278410752: "GROUPS",
    762068938686595152: "PROFICIENCY",
    718473529452003329: "CAPE",
    755875615587958814: "CSEC",
    831265040434331649: "VERIFY"
}

progression_role_ids = {
    785341063984316476: "Stage 1",
    834837741937098823: "Stage 2",
    834838252670025769: "Stage 3",
    834838268150415370: "Stage 4 CAPE",
    834838264581587055: "Stage 4 CSEC",
    830907979301388368: "Unverified Student"
}

proficiency_to_stage = {
    764214191782756392: 834838268150415370,
    764214207192760401: 834838264581587055
}

# Links the respective registration channel to the role needed to view it
register_channels_to_progression_roles = dict(zip(list(register_channels.keys()), list(progression_role_ids.keys())))

progression_roles = {
    834837579433115709: 785341063984316476,
    785341063984316476: 834837741937098823,
    834837741937098823: 834838252670025769,
    834838252670025769: 0,
    834838268150415370: 830907979301388368,
    834838264581587055: 830907979301388368,
    830907979301388368: [755633133600112651, 762190942316134400]
}

group_roles = {
    "🕑": "duo",
    "🕒": "trio",
    "🕓": "quartet",
    "🕔": "qunitet",
    "✅": "Confirm"
}

group_roles_ids = {
    "duo": 765011328532086805,
    "trio": 765011376976166942,
    "quartet": 765011399524614169,
    "qunitet": 765011419598815233,
    "decuplet": 765011478775463947,
    "vigintet": 765011552007880736,
}

channels = {
    "CSEC":755875615587958814,
    "CAPE": 718473529452003329,
    "REP_FLAG": 700174264782815232,
    "PERSONALIZE_CHANNEL": 830914205078782072,
    "VERIFY": 831265040434331649,
    "NAME_CHANGES": 785986850736963675,
    "ROLE_CHANGES": 785986876531015711,
    "MESSAGE_LOGS": 785993210522107925,
    "BULK_DELETES": 786003742813192233,
    "JOIN_LEAVES": 786016910668070952,
    "ERROR_ROOM": 828638567236108308,
    "WELCOME_CHANNEL": 700214669003980801,
    "MEMBER_COUNT_CHANNEL": 764418047246729227,
    "MEMBERS_IN_VC_COUNT_CHANNEL": 764427421876748298,
    "BOT_ROOM": 831275896429477980,
    "PROFICIENCY": 762068938686595152,
    "INTRO_VIDEO": 832043773973364747
}

# Dictionary containing all emojis and their links to their roles.
reactions = {
    "PROFICIENCY": {
        "📘": "csec",
        "📖": "cape",
        },
    "CSEC": {
        "📈":"csec add maths",
        "🌾":"csec agricultural science",
        "🧬":"csec biology",
        "🏗":"csec building tech",
        "🌋":"csec caribbean history",
        "🧪":"csec certificate in business studies",
        "🏛":"csec chemistry",
        "🧵":"csec clothing and textiles",
        "💳":"csec economics",
        "⌨":"csec edpm",
        "🔌":"csec electrical engineering",
        "📕":"csec english a",
        "📗":"csec english b",
        "🍽":"csec food and nutrition",
        "🇨":"csec french",
        "🗺":"csec geography",
        "🧠":"csec hsb",
        "🖥":"csec information technology",
        "⚗":"csec integrated science",
        "📉":"csec maths",
        "⚙":"csec mechanical engineering",
        "🎶":"csec music",
        "⚽📠":"csec office admin",
        "⚽":"csec physical education",
        "🧲":"csec physics",
        "💵":"csec poa",
        "💷":"csec pob",
        "🙏":"csec religious education",
        "🏡":"csec resources and family management",
        "🎎":"csec social studies",
        "🇪":"csec spanish",
        "✏":"csec technical drawing",
        "🎭":"csec theatre arts",
        "🎨":"csec visual arts",
    },
    "CAPE": {
        "💲":"cape accounting",
        "🥬":"cape agricultural science",
        "🎮":"cape animation and game design",
        "📊":"cape applied maths",
        "🌌":"cape arts and design",
        "🦠":"cape biology",
        "🛠":"cape building and mechanical engineering drawing",
        "📙":"cape caribbean studies",
        "🌡":"cape chemistry",
        "📘":"cape communication studies",
        "💻":"cape computer science",
        "🎥":"cape digital media",
        "💱":"cape economics",
        "💡":"cape electrical electronic engineering tech",
        "💰":"cape entrepreneurship",
        "🏞":"cape environmental science",
        "🗂":"cape financial services studies",
        "🍔":"cape food and nutrition",
        "🇨":"cape french",
        "🏝️": "cape geography",
        "🌍":"cape geography",
        "♻":"cape green engineering",
        "🗾":"cape history",
        "💾":"cape information tech",
        "🔢":"cape integrated maths",
        "⚖":"cape law",
        "📖":"cape literature in english",
        "🏧":"cape logistics and supplies chain oppositions",
        "💼":"cape management of business",
        "💃":"cape performing arts",
        "🏀":"cape physical education",
        "🔋":"cape physics",
        "📐":"cape pure maths",
        "🗿":"cape sociology",
        "🇻":"cape spanish",
        "🏖":"cape tourism",
    },
    "GROUPS": {
        "🕑": "duo",
        "🕒": "trio",
        "🕓": "quartet",
        "🕔": "quintet",
    },
    "COUNTRIES": {
        "\U0001f1f2\U0001f1f8" : "Montserrat",
        "\U0001f1e6\U0001f1ec" : "Antigua and Barbuda",
        "\U0001f1e7\U0001f1f8": "Bahamas",
        "\U0001f1e7\U0001f1ff" : "Belize",
        "\U0001f1e9\U0001f1f2" : "Dominica",
        "\U0001f1ec\U0001f1e9" : "Grenada",
        "\U0001f1ec\U0001f1fe" : "Guyana",
        "\U0001f1ed\U0001f1f9" : "Haiti",
        "\U0001f1f1\U0001f1e8" : "St.Lucia",
        "\U0001f1f0\U0001f1f3" : "St.Kitts and Nevis",
        "\U0001f1f8\U0001f1f7" : "Suriname",
        "\U0001f1ef\U0001f1f2" : "Jamaica",
        "\U0001f1f9\U0001f1f9" : "Trinidad and Tobago",
        "\U0001f1e7\U0001f1e7" : "Barbados",
        "\U0001f1fb\U0001f1e8" : "St.Vincent and the Grenadines",
    },
    "VERIFY": {
        "✅": [all_roles["FAMILY"], all_roles["NEWBIE"]]
        }
}

country_dict = {
    "\U0001f1f2\U0001f1f8" : "Montserrat",
    "\U0001f1e6\U0001f1ec" : "Antigua and Barbuda",
    "\U0001f1e7\U0001f1f8": "Bahamas",
    "\U0001f1e7\U0001f1ff" : "Belize",
    "\U0001f1e9\U0001f1f2" : "Dominica",
    "\U0001f1ec\U0001f1e9" : "Grenada",
    "\U0001f1ec\U0001f1fe" : "Guyana",
    "\U0001f1ed\U0001f1f9" : "Haiti",
    "\U0001f1f1\U0001f1e8" : "St.Lucia",
    "\U0001f1f0\U0001f1f3" : "St.Kitts and Nevis",
    "\U0001f1f8\U0001f1f7" : "Suriname",
    "\U0001f1ef\U0001f1f2" : "Jamaica",
    "\U0001f1f9\U0001f1f9" : "Trinidad and Tobago",
    "\U0001f1e7\U0001f1e7" : "Barbados",
    "\U0001f1fb\U0001f1e8" : "St.Vincent and the Grenadines"
}


logs = []

if path.exists("logs.json"):
    with open("logs.json") as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            pass

async def log(self, modcmd, action, culprit, reason):
    """Function used to save logs"""
    mydict = {"Command":modcmd, "Action":action, "Done By":culprit, "Reason": reason, "Time": ctime()}
    
    self.logs.append(mydict)

    with open("logs.json", "w") as f:
        json.dump(self.logs, f, indent=4)