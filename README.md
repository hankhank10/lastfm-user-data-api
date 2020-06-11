# Last.fm user data API

Simple python script which pulls down user data from last.fm

This information is publicly available for all users so there is no need to be logged in to last.fm. You also don't need to change the public key in the code.

## Usage

Clone the repositary.

Add the following to the start of your script

```include lastfm_user_data.py```

Then use the following command in your script to pull the data

``` lastfm_user_data.check_data (USERNAME_TO_CHECK, PARAMETER_TO_CHECK)```

## Example

There is an example (example.py) provided which calls and outputs the playcount for a specified user.

## What data can be accessed?

You can see which parameters are available by looking at the following URL which will show you the json format provided by last.fm:

http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user=test&api_key=079a7d64ea52c358ad4f0afbe2f900b3&format=json
