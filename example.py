import lastfm_user_data

# ask user to input a username
requested_username = input ("Enter a last.fm username to check the playcount of >>>  ")

# check that username
playcount = lastfm_user_data.check_data(requested_username, "playcount")
print ("Last.fm user " + requested_username + " has played " + playcount + " tracks")
