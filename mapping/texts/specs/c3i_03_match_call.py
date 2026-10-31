# Match call (C3i part 3): the COMLINK calls from trainers, rivals, Mom, Korr, Leia and Lando, plus the
# trainer profile blurbs. Ocean worlds keep their seas and beaches (Kamino, Yavin 4, Dagobah's swamps).
# Han is a pilot, not a sailor, and Chewie is his co-pilot, not a pet.
KEEP_REST_FILES = ("data/text/match_call.inc", "src/data/text/match_call_messages.h")
REFLOW = True


def pl(*olds):
    return [(o, o.replace("CREATURE", "CREATURES")) for o in olds]


FIX = {
"MatchCall_NegativeBattleText8": pl("How are your CREATURE doing?"),
"MatchCall_NegativeBattleText11": pl("How are your CREATURE?"),
"MatchCall_PositiveBattleText9": pl("How are your CREATURE holding up?"),
"MatchCall_SameRouteBattleRequestText6": pl("How are your CREATURE keeping?"),
"MatchCall_DifferentRouteBattleRequestText3": pl("with your CREATURE"),
"MatchCall_DifferentRouteBattleRequestText7": pl("Are your CREATURE growing?"),
"MatchCall_DifferentRouteBattleRequestText9": pl("How are your CREATURE doing?", "My CREATURE keep"),
"MatchCall_DifferentRouteBattleRequestText11": pl("seeing your CREATURE,"),
"MatchCall_DifferentRouteBattleRequestText13": pl("Are your CREATURE keeping well?"),
"MatchCall_PersonalizedText30": pl("help of CREATURE can"),
"MatchCall_PersonalizedText41": pl("How are your CREATURE doing?"),
"MatchCall_PersonalizedText54": pl("Are your CREATURE fit"),
"MatchCall_PersonalizedText60": pl("enjoy CREATURE whatever"),
"MatchCall_Text_Mom1": pl("captivated by CREATURE.", "charm of CREATURE?"),
"MatchCall_Text_Scott1": pl("how CREATURE can be found"),
"MatchCall_Text_May1": r"MIRA: Hi, {PLAYER}{KUN}!\pHAN says he's retired from smuggling,\nbut I still see him flying around\lwith CHEWIE sometimes.\pHe must love flying still.$",
"MatchCall_Text_Brendan1": r"KAEL: Hey, {PLAYER}!\pHAN says he's retired from smuggling,\nbut I still see him flying around\lwith CHEWIE sometimes.\pI guess he must love\nflying still.$",
"MatchCall_Text_Steven1": [("visit the BIKE SHOP\nand get a SWOOP BIKE.", "visit the bike shop\nand get a SWOOP BIKE."), ("GRANITE\nCAVE", "SHADOWLANDS\nof KASHYYYK")],
"gText_MatchCallSchoolKid_Karen_Pokemon": r"I love any kind of CREATURES!",
"gText_MatchCallPokefan_Miguel_Intro2": pl("trust with your CREATURE."),
"gText_MatchCallSwimmer_Jenny_Intro2": r"I was interviewed on the HOLONET.",
}
NOTES = {
"MatchCall_Text_May1": "Han (Briney) is a retired smuggler; Chewie (Peeko) is his co-pilot, not a pet",
}
