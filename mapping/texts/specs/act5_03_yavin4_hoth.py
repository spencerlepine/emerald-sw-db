# Yavin 4 (Mossdeep): the hidden Rebel base, the LAUNCH TOWER (Space Center), Leia's house, the Massassi Temple
# arena of Quinlan Vos & Aayla Secura (Tate & Liza: master and former Padawan, not twins), Routes 124-125 (sea),
# and Hoth's WAMPA CAVE (Shoal Cave; Emerald's tides become meltwater).
# Vader's raid on the tower: he would rather wreck Mustafar than leave it to anyone; after losing he doubts
# himself for a moment (the conflict in him).
KEEP_REST_MAPS = ("map:mossdeep-city", "map:route124", "map:route125", "map:shoal-cave")
M = "MossdeepCity_Text_"
G = "MossdeepCity_Gym_Text_"
SC1 = "MossdeepCity_SpaceCenter_1F_Text_"
SC2 = "MossdeepCity_SpaceCenter_2F_Text_"
SH = "MossdeepCity_StevensHouse_Text_"
GC = "MossdeepCity_GameCorner_1F_Text_"


def pl(*olds):
    return [(o, o.replace("CREATURE", "CREATURES")) for o in olds]


FIX = {
# --- Yavin 4 town ---
M+"WantKingsRockStevenGaveMe": [],
M+"WhatToDoWithWeirdRock": [],
M+"SpaceCenterReceivedLetter": r"The base's LAUNCH TOWER has been\nlaunching huge rockets.\pThere's been some kind of an uproar\nover a letter they received recently.$",
M+"SpaceCenterLaunchingRockets": r"The base's LAUNCH TOWER has been\nlaunching huge rockets.$",
M+"MossdeepTargetedByMagma": r"I heard from a PILOT buddy that\nthe CARTEL set up shop in CLOUD CITY.\pI also heard that someone came along\nand wiped the floor with them!\pBut YAVIN 4 here's been targeted\nby the EMPIRE.\pIf you want to know what they're up to,\ngo visit the LAUNCH TOWER.$",
M+"NiceIfWorldCoveredByFlowers": r"Wouldn't it be nice?\pIf the whole galaxy was covered in\njungle and flowers like this moon?$",
M+"SurfExhilarating": pl("crossing the sea with CREATURE"),
M+"CitySign": r"YAVIN 4\n“The jungle moon. Cherish CREATURES!”$",
M+"GymSign": r"MASSASSI TEMPLE ARENA\nLEADERS: VOS & AAYLA\p“Master and apprentice, one in\nthe Force!”$",
M+"SootopolisNewGymLeader": r"Ahh… It feels great letting the waves\nwash over my feet…\pSpeaking of water, you know that\nswamp world DAGOBAH?\pI think the ARENA there had a new\nLEADER come in.\pPeople tell me the new LEADER once\nmentored OBI-WAN.$",
M+"ScottSomethingWrongWithTown": [("this town.", "this place.")],
# --- Massassi Temple arena (Vos & Aayla) ---
G+"GymGuideAdvice": r"Yo, how's it going, ILUM-bound\n{PLAYER}?\pThe ARENA LEADERS here use\nFORCE-type CREATURES.\pIf you go up against them with\nFIGHTING- or POISON-type CREATURES,\lthey'll inflict horrible damage!\pPlus, they'll come at you with\noutstanding combination attacks.\pIf you want to win, show them how\ntight you are with your CREATURES.\lGo for it!$",
G+"VirgilPostBattle": [("If there are prodigies in the world,", "If there are prodigies in the galaxy,")],
G+"BlakeIntro": r"Fufufufu… Watch me levitate a CAPTURE\nPOD with the Force!\pWrooooooooaaaar!\n… … … … … … …\pSometimes, I'm out of sync…$",
G+"BlakePostBattle": [("too heavy to lift\npsychically.", "too heavy to lift\nwith the Force.")],
G+"NicholasIntro": pl("my super\nCREATURE hard"),
G+"TateAndLizaIntro": r"VOS: Hehehe… Were you surprised?\pAAYLA: Fufufu… Were you surprised?\pVOS: That there are two LEADERS?\nAAYLA: That there are two LEADERS?\pVOS: I was her master!\nAAYLA: I was his PADAWAN!\pVOS: We don't need to talk because…\nAAYLA: Through the Force, we sense…\pVOS: What the other is thinking…\nAAYLA: All in our minds!\pVOS: This combination of ours…\nAAYLA: Can you beat it?$",
G+"ExplainCalmMind": [("AAYLA: For FORCE PUSH CREATURE!", "AAYLA: For FORCE-type CREATURES!")],
G+"TateAndLizaPostBattle": r"VOS: Looks like the bond between you\nand your CREATURES is stronger than\lthe bond of master and apprentice.\pAAYLA: You will become even stronger!\nWe've battled you, so we know.$",
G+"TateAndLizaNeedTwoMons": [("AAYLA: That there are two ARENA LEADERS?", "AAYLA: That there are two LEADERS?")],
G+"GymStatue": r"MASSASSI TEMPLE ARENA$",
G+"GymStatueCertified": r"MASSASSI TEMPLE ARENA\pAAYLA AND VOS'S CERTIFIED TRAINERS:\n{PLAYER}$",
G+"TateAndLizaPreRematch": [("VOS: CREATURE…\nAAYLA: CREATURE…", "VOS: CREATURES…\nAAYLA: CREATURES…")],
G+"TateAndLizaRematchNeedTwoMons": [("AAYLA: Two CREATURE when you come back.", "AAYLA: Two CREATURES next time.")],
# --- Houses, mart ---
"MossdeepCity_House2_Text_SisterMailsBoyfriendInFortree": [("her boyfriend in BRIGHT TREE.", "her boyfriend on ENDOR.")],
"MossdeepCity_House2_Text_PokemonCarriesMailBackAndForth": [("Even though I can't see my friend in\nBRIGHT TREE,", "Even though I can't see my friend\non ENDOR,")],
"MossdeepCity_House3_Text_GoAfterSeafloorPokemon": r"Go after the seafloor CREATURES with\nyour SUPER ROD.$",
"MossdeepCity_House4_Text_BrotherLikesToFindBases": r"My little brother says he likes to go\nfind people's HIDEOUTS.$",
"MossdeepCity_House4_Text_BrotherLikesToVisitBasesAndBattle": r"My little brother says he likes to\nvisit people's HIDEOUTS and have\lCREATURE battles.$",
"MossdeepCity_Mart_Text_NetAndDiveBallsRare": r"The NET and DIVE PODS are rare\nCAPTURE PODS that are only made here.\pA NET POD is effective against\nBUG-type and WATER-type CREATURES.\pA DIVE POD works best on CREATURES\nat the bottom of the sea.$",
"MossdeepCity_Mart_Text_ReviveIsFantastic": r"REVIVE STIM is fantastic!\pGive it to a fainted CREATURE,\nand the CREATURE will arise.\pBut be careful, REVIVE STIM won't\nrestore the used-up PP of moves.$",
"MossdeepCity_Mart_Text_MaxRepelLastsLongest": r"REPULSOR III keeps all weak\nCREATURES away.\pOut of all the REPULSOR sprays, it lasts\nthe longest.$",
# --- Launch Tower ---
SC1+"MagmaHaveSightsOnSpaceCenter": [],
SC1+"FoundThisYouCanHaveIt": [],
SC1+"HoennFamousForMeteorShowers": r"The OUTER RIM has been famous for\nits meteor showers for a long time.$",
SC1+"MagmaCantStealFuelTakeThis": r"The EMPIRE can't be allowed to steal\nthe rocket fuel.\pOh, by the way, you can have this stone\nI found on the beach.$",
SC1+"CantStrollOnBeachWithMagma": r"With the EMPIRE around, I guess\nstrolls on the beach aren't safe.$",
SC1+"DidPokemonComeFromSpace": r"Some people claim that CREATURES came\nfrom space. Could it be true?$",
SC1+"AquaShouldBeatMagma": r"The CARTEL should take care of\nthe EMPIRE!\pBut if they did that, the CARTEL would\nbecome bold and brazen, wouldn't they?$",
SC1+"MagmaWantsToSpoilMyDream": [("But THE EMPIRE wants to spoil", "But the EMPIRE wants to spoil")],
SC1+"StevenMagmaCantBeAllowedToTakeFuel": [("THE EMPIRE is coming after the rocket\nfuel on this island.", "The EMPIRE is coming after the rocket\nfuel at this base."), ("check out the town?", "look around the base?")],
SC1+"Grunt4PostBattle": [("Ask our leader upstairs!", "Ask LORD VADER upstairs!")],
SC1+"Grunt2Intro": r"LORD VADER said no one, but no one,\ngets past me!$",
SC1+"Grunt2PostBattle": r"Please, tell LORD VADER that\nI never abandoned my post.\lThat I stayed to the bitter end…$",
SC1+"MagmaIntentToStealNotice": r"This is…\nAn intent-to-steal notice?\p“To the staff of the LAUNCH TOWER:\nThe EMPIRE will soon visit you.\p“We will take your rocket fuel.\nResistance is futile.\p“Let there be more land!\n                                          THE EMPIRE”$",
SC2+"MossdeepIdealForRockets": r"YAVIN 4 has mostly calm weather,\nand its winds are stable.\pIt's an ideal location for launching\nrockets.$",
SC2+"WhyWouldMagmaStealRocketFuel": r"Why would the EMPIRE want to steal\nour rocket fuel in the first place?$",
SC2+"MagmaCantGetAwayWithThis": r"If the EMPIRE takes the rocket fuel,\nI won't be able to go to space!\pThey can't be allowed to get away\nwith such an outrage!$",
SC2+"DoesMagmaWantToGoToSpace": r"The EMPIRE…\nDo they want to go to space, too?$",
SC2+"Grunt5PostBattle": r"Are we being useful to LORD VADER\nat all?$",
SC2+"StevenWhyStealRocketFuel": r"LEIA: The EMPIRE…\pWhat's the point of stealing rocket\nfuel?$",
SC2+"MaxieUseFuelToEruptVolcano": r"VADER: Since you are so curious,\nyou deserve an explanation.\pWe are going to jettison the entire\nload into MUSTAFAR PEAK!\pWith GREATKRAYT gone, I have no need\nfor that slag heap of a mountain!\pThe fuel's power will make the\nvolcano erupt!\pIt will be savage!$",
SC2+"MaxieWeFailedIsAquaAlsoMisguided": r"VADER: We failed to make the volcano\nerupt…\pWe failed to control GREATKRAYT after\nwe had awoken it…\pIs our goal to expand the land\nmisguided?\p… … … … … …\n… … … … … …\pIf…\nIf the EMPIRE is wrong…\l… … … … … …\pThen JABBA's plan to drown the worlds\nmust be just as misguided…$",
SC2+"MaxieWeWillGiveUp": [],
SC2+"StevenThankYouComeSeeMeAtHome": r"LEIA: Whew, that was too tense.\n{PLAYER}{KUN}, thank you.\pI have something to give you as\nthanks for your support.\pPlease come see me at home\nafter this.\pOh, yes, I don't live on TATOOINE.\nI live right here at the base.$",
# --- Leia's house ---
SH+"UnderwateCavernBetweenMossdeepSootopolis": r"LEIA: Apparently, there's an\nunderwater cavern on the way from\lYAVIN 4 to DAGOBAH.\pYou know, the one that RIC OLIé\nfound in his submarine.$",
SH+"LetterFromSteven": [("LEIA STONE", "LEIA ORGANA"), ("my favorite\nCREATURE.", "my favorite\ndroid.")],
SH+"CollectionOfRareRocks": r"It's a collection of rare stones and\ncrystals assembled by LEIA.$",
# --- Game corner (wireless minigames) ---
GC+"PokemonJumpInfo": [("CREATURE that only swim, burrow,\nor fly", "CREATURES that only swim, burrow,\nor fly"), ("Only mini CREATURE around", "Only mini CREATURES around")],
GC+"ExplainRequiredMon": pl("have any\nCREATURE that"),
GC+"ShortJumpingPokemonAllowed": pl("is open to CREATURE\naround"),
# --- Routes 124-125 ---
"Route124_DivingTreasureHuntersHouse_Text_HaveYouSeenAnyShards": r"Tell me, have you seen any CRYSTALS\nfrom ancient times?$",
"Route124_DivingTreasureHuntersHouse_Text_YouHaventGotAnyShards": r"You haven't got any treasures\nfor me…\pIf you see any CRYSTALS, like the RED\nCRYSTAL, you've got to trade it with me!$",
"Route124_DivingTreasureHuntersHouse_Text_ThatsAShardIllTradeYou": r"Oh, hey! That…\nThat's a CRYSTAL! I'm looking for those!\pOh, man, you've got to trade that\nwith me! I'll give you something good!$",
"Route124_Text_RolandPostBattle": [("I wish I could ride a CREATURES like you…", "I wish I could ride a CREATURE like you…")],
"Route124_Text_IsabellaPostBattle": [("pretty colored shards\nof things", "pretty colored crystals\nof all kinds")],
"Route125_Text_ErnestIntro": [("I've braved the world's seas!", "I've braved the galaxy's seas!")],
"Route125_Text_ErnestPostBattle": r"The meltwater rises and falls inside\nthe WAMPA CAVE.\pBy the way, it's about six hours from\nhigh water to low water. Did you know?$",
"Route125_Text_ErnestRematchPostBattle": r"The WAMPA CAVE…\pThere are places you can and can't\nget to depending on the rise and fall\lof the meltwater.\pBy the way, it's about six hours from\nhigh water to low water. Don't forget!$",
"Route125_Text_KimPostBattle": [("Let's go see him, IRIS!", "Let's go see him, ISRA!")],
"Route125_Text_IrisIntro": [("ISRA: KIM, can you", "ISRA: KAI, can you")],
"Route125_Text_IrisPostBattle": [("ISRA: KIM, are we", "ISRA: KAI, are we"), ("We'll get all wet.", "We'll freeze.")],
"Route125_Text_SharonIntro": pl("WATER-type CREATURE I raised?"),
# --- Hoth: Wampa Cave ---
"ShoalCave_LowTideLowerRoom_Text_CanOvercomeColdWithFocus": [("The penetrating cold around these\nparts", "The penetrating cold of\nHOTH")],
}
NOTES = {
G+"TateAndLizaIntro": "Vos & Aayla are master and former Padawan (Emerald's twins)",
SH+"LetterFromSteven": "Leia's surname: ORGANA (Steven Stone); R1 UNIT (Beldum) is a droid",
SC2+"MaxieWeFailedIsAquaAlsoMisguided": "Vader's doubt mirrors Maxie's; Jabba's drowned-worlds plan",
"Route125_Text_ErnestPostBattle": "Shoal Cave tides = Hoth meltwater (same timer)",
}
