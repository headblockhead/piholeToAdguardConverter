import urllib2

lineno = 0
formatedlines = []

for line in urllib2.urlopen("https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt"):
    lineno = lineno + 1
    if line.startswith("0.0.0.0 ") and line.endswith("\n") and not line.endswith("0.0.0.0"):
        print("level1: " + line)
        formatedlines.append(
            "||" + (line.split("0.0.0.0 ")[1]).split("\n")[0] + "^\n"
        )
    elif line.endswith("\n") and not line.startswith("#") and not line.endswith("localhost") and not line == "\n":
        print("level2: " + line)
        if "#" in line:
            line = line.split("#")[0]
        else:
            line = line.split("\n")[0]

        formatedlines.append(
            "||" + line + "^\n"
        )


f = open("out.txt", "w")
f.writelines(formatedlines)
f.close
