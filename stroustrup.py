import urllib.request;print("\n".join([x.split("\"")[1] for x in urllib.request.urlopen(input()).read().decode("UTF-8").split("\r\n") if x.startswith("<a href") and (x.split("\"")[1].startswith("https") or x.split("\"")[1].startswith("http"))]))