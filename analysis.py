# just pseudocode bullshit because it's late and i need to get stuff down
# anyone who actually knows any cs is probably cringing so hard right now

''' goals '''

### on first startup ###
# save current date in rsinfo.txt
# save current name in rsinfo.txt
# add "con_logtext rslog.txt" to autoexec.cfg if not already there

### on every game load ###
# get current name

### after exiting a game ###
# open and read rslog.txt
# iterate through each line of rslog.txt
# when string is in format %s killed %s with %s:
#    save each string as array entries
#    OPT: save new entry to csv "rslog.csv"
#    OPT: so would look like:
#    OPT: YYYY-MM-DD | cherazul | The Entire Population of Texas | scattergun
#    or otherwise, just add how many times user has been killed with X weapon
#    save value in rsinfo.txt
# after rslog.txt is analyzed, it is closed and deleted

### when user runs analysis ###
# all weapon names are translated to in game names (eg healgun to Medi-Gun)
# simpleReturn() returns a numbered list by order of number of times killed, with each weapon name

# integrated with current HUD?

''' possible features '''

### reverse strange tracker ###
## options ##
# track self only
# track self only with crits
# track self and friends
# track number of times a specific person kills you (only works if they don't change their name)
# track everyone, in every game you've ever played
# track yourself only when you wear your lucky hat (OR track how many kills you get while you wear a certain hat)
# same for above, but lucky weapon
# same for above, but specific map

# track number of times the person you just killed uses profanity in chat (amount of raging caused)
# track number of times the person you just killed disconnects (number of ragequits caused)

# track that, but for yourself (number of ragequits caused)

# save all console logs
# save csv summary (parsed versions of logs, essentially)

### 

''' problems '''
# will parse incorrectly if killer/victim has "killed" or "with" in name
