# You can decode/encode urls and parameter using the urllib.parse module.
# But I think it's easier to just concat here because I'm always sure there's at least one parameter so I don't have to worry about there being '?' or not.
# The workflow for managing paramters with urllib is super arse by the way. Something like:
#   url = 'url_here'
#   split = parse.urlsplit(url)                    # returns named tuple, so we can access query like split.query or split['query'] but we can't edit it.
#   lst = list(split)                              # so we can change the value. Admittedly, you chain this on the above line to save space.
#   dct = dict(parse.parse_qsl(split.query))       # or lst[3] which we can also just assign to a new string from the get-go, lst[3] = 'new_params'.
#   dct['key'] = 'value'                           # adds new pair.
#   lst[3] = parse.urlencode(dct)                  # parses dict to param str.
#   url = parse.unsplit(lst)                       # this is fucking stupid.
# There's a shorter way using urljoin, so at least there's that. But you still have to split --> dict --> add pair --> join
base_url = 'https://googleapis.com/youtube/v3/'
channel_template = base_url + 'channels/list?part=contentDetails'