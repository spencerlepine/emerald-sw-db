# Shared UI strings (C3i part 2): src/strings.c, the menus, bag, party, storage, shops, decorations, link play
# and Mystery Gift. PC -> TERMINAL, BIKE -> SPEEDER BIKE where it means the bike in general, Wireless Adapter
# and Game Link cable -> COMLINK. ¥ stays as the money glyph (Step 5 redraws it as credits).
KEEP_REST_FILES = ("src/strings.c",)
# no REFLOW: UI windows do not scroll, overflow is fixed by hand

FIX = {
"gText_WirelessNotConnected": r"The COMLINK is not\nconnected.",
"gText_MysteryGiftCantUse": r"MYSTERY GIFT can't be used while\nthe COMLINK is attached.",
"gText_MysteryEventsCantUse": r"MYSTERY EVENTS can't be used while\nthe COMLINK is attached.",
"gText_WirelessCommStatus": r"COMLINK Status",
"gText_VarietyOfEventsImportedWireless": r"A variety of events will be imported\nover the COMLINK.",
"gText_DontRemoveCableTurnOff": r"Don't remove the COMLINK cable.\nDon't turn off the power.",
"gText_HOFDexRating": r"Spotted CREATURES: {STR_VAR_1}!\nOwned CREATURES: {STR_VAR_2}!\pPROF. KORR's DATAPAD rating!\pPROF. KORR: Let's see…\p",
"gText_LeagueChamp": r"ILUM CHAMPION!\nCONGRATULATIONS!",
"gText_CantDismountBike": r"You can't get off your bike here.{PAUSE_UNTIL_PRESS}",
"gText_CantStoreImportantItems": r"Important items\ncan't be stored in\nthe TERMINAL!",
"gText_ThePC": r"the TERMINAL",
"gText_ThankYouIllSendItHome": r"Thank you!\nI'll send it to your home TERMINAL.",
"gText_ThanksIllSendItHome": r"Thanks!\nI'll send it to your TERMINAL at home.",
"gText_SendMailToPC": r"Send the removed MAIL to\nyour TERMINAL?",
"gText_MailSentToPC": r"The MAIL was sent to your TERMINAL.{PAUSE_UNTIL_PRESS}",
"gText_PCMailboxFull": r"Your TERMINAL's MAILBOX is full.{PAUSE_UNTIL_PRESS}",
"gText_StoreChosenDecorInPC": r"Store the chosen decoration in the\nTERMINAL.",
"gText_ReturnDecorationToPC": r"Return this decoration to the\nTERMINAL?",
"gText_DecorationReturnedToPC": r"The decoration was returned to the\nTERMINAL.",
"gText_StoreItemsInPC": r"Store items in the TERMINAL.",
"gText_TakeOutItemsFromPC": r"Take out items from the TERMINAL.",
"gText_ThrowAwayItemsInPC": r"Throw away items stored in the\nTERMINAL.",
"gText_SomeonesPC": r"SOMEONE'S TERMINAL",
"gText_LanettesPC": r"TESS'S TERMINAL",
"gText_PlayersPC": r"{PLAYER}'s TERMINAL",
"gText_NotPkmnOtherTrainerWants": r"That isn't the kind of CREATURE\nthat the other TRAINER wants.",
"gText_MarkYourPkmn": r"Mark your CREATURE.",
"gEasyChatGroupName_Pokemon2": r"CREATURES2",
"gText_ProfBirchMatchCallDesc": r"CREATURE PROF.",
"gText_NothingToCut": r"There's nothing to slice here.",
}
NOTES = {
"gText_SomeonesPC": "PC -> TERMINAL; the PC menu window sizes to its longest entry",
"gText_ProfBirchMatchCallDesc": "{PKMN} glyph token -> plain word (glossary)",
"gEasyChatGroupName_Pokemon2": "Easy Chat group name; second CREATURE word list",
}
