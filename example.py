import lastfm_user_data

# ask user to input a username
requested_username = input ("Enter a last.fm username to check the playcount of >>>  ")

# check that username
print ()
print ("Gathering data for user " + requested_username + " with URL: " + lastfm_user_data.static_data(requested_username, "url"))
print ()
print ("Scrobbles:")
print (lastfm_user_data.playcount(requested_username, "") + " ever")
print (lastfm_user_data.playcount(requested_username, "this_year") + " this year")
print (lastfm_user_data.playcount(requested_username, "this_month") + " this month")
print (lastfm_user_data.playcount(requested_username, "this_week") + " this week")
print (lastfm_user_data.playcount(requested_username, "today") + " today")
print()
print ("Last played track:")
lastplayed_track, lastplayed_artist, lastplayed_album, lastplayed_image = lastfm_user_data.lastplayed (requested_username)

print (lastplayed_track + " by " + lastplayed_artist + " from  " + lastplayed_album)
print (lastplayed_image)