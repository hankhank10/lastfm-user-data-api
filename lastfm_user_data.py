import urllib.request
import json

def check_data(lastfm_username, json_field):
    # build URL
    lastfm_public_key = "079a7d64ea52c358ad4f0afbe2f900b3"
    
    #lastfm_username = "markhank"
    url = "http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user=" + lastfm_username + "&api_key=" + lastfm_public_key + "&format=json"
    #print (url)

    # download the raw json object
    data = urllib.request.urlopen(url).read().decode()

    # parse json object
    obj = json.loads(data)

    # extract relevant data
    output = obj['user'][json_field]

    return output

# ask user to input a username
requested_username = input ("Enter a last.fm username to check the playcount of >>>  ")

# check that username
playcount = check_data(requested_username, "playcount")
print ("Last.fm user " + requested_username + " has played " + playcount + " tracks")