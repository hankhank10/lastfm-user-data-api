import lastfm_user_data
import sys

# check if a command line argument has been passed
if len(sys.argv) == 2:
    # if it has then set the requested username to that
    requested_username = str(sys.argv[1])
else:
    #if not then ask the user to input a username
    requested_username = input ("Enter a last.fm username to check the playcount of >>>  ")

# use the function to gather and print data for that username
print ()
print ("Gathering data for user " + requested_username + " with URL: " + lastfm_user_data.static_data(requested_username, "url"))
print ()
print ("Scrobbles:")
print (lastfm_user_data.playcount(requested_username, "") + " ever")
print (lastfm_user_data.playcount(requested_username, "this_year") + " so far this year")
print (lastfm_user_data.playcount(requested_username, "this_month") + " so far this month")
print (lastfm_user_data.playcount(requested_username, "this_week") + " so far this week")
print (lastfm_user_data.playcount(requested_username, "today") + " so far today")
print()
print (lastfm_user_data.playcount(requested_username, "last30days") + " in last 30 days")
print (lastfm_user_data.playcount(requested_username, "last7days") + " in last 7 days")
print (lastfm_user_data.playcount(requested_username, "last24hours") + " in last 24 hours")
print (lastfm_user_data.playcount(requested_username, "last_hour") + " in last hour")
print()
print ("Last played track:")
lastplayed_track, lastplayed_artist, lastplayed_album, lastplayed_image = lastfm_user_data.lastplayed (requested_username)

print (lastplayed_track + " by " + lastplayed_artist + " from the album " + lastplayed_album)
print (lastplayed_image)
print ()