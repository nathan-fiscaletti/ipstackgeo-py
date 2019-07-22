import os
import requests

log = open("./tests/latest.stylelog", "w")
results = os.popen("pycodestyle ./ipstack/*.py").read()
lines = results.strip().splitlines()

url = None
url_failed = "https://img.shields.io/badge/pycodestyle-failed-red.svg"
url_success = "https://img.shields.io/badge/pycodestyle-success-brightgreen.svg"

if len(lines) > 0:
    print("Style Failed")
    log.write("Style Failed" + os.linesep)
    log.write(results + os.linesep)
    url = url_failed
else:
    print("Style Passed")
    log.write("Style Passed" + os.linesep)
    url = url_success

print("Updating ./stylebadge.svg with: " + url)
log.write("Updating ./stylebadge.svg with: " + url + os.linesep)
open("./stylebadge.svg", "wb").write(requests.get(url).content)

print("Updating git commit with new stylebadge.svg")
log.write("Updating git commit with new stylebadge.svg" + os.linesep)
git_add = os.popen("git add ./stylebadge.svg").read()
print(git_add)
log.write(git_add + os.linesep)
log.close()
os.popen("git add ./tests/latest.stylelog")
