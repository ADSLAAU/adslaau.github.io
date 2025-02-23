#!/usr/bin/python3

from os import listdir;
from os.path import isfile, isdir, join;
from textwrap import indent;

def walk(folder: str) -> str:
    output: str = "";
    output += "<ul>\n";
    entries = listdir(folder);
    entries.sort(reverse=True);
    for entry in entries:
        path = join(folder, entry);
        if isfile(path):
            output += f"\t<li><a href=\"{path}\">{entry}</a></li>\n";
        elif isdir(path):
            output += f"\t<li><details>"
            output += f"\t<summary>{entry}</summary>\n";
            output += indent(walk(path), '\t\t');
            output += f"\t</details></li>\n";
        else:
            raise ValueError(f"Entry \"{entry}\" at \"{path}\" is neither a file nor directory");
    output += "</ul>\n";
    return output;
            
        

print('''
<!DOCTYPE html>
<html lang="da">
	<head>
		<link rel="stylesheet" href="../base.css"/>
		<link rel="icon" href="../logo.png"/>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta charset="UTF-8">
		<title>ADSLs referater</title>
	</head>
	<body>
		<nav>
			<ul>
				<li><a href=".."><img class="logo" src="../logo.png"></a></li>
				<li><a href="../regnskab">Regnskab</a></li>
				<li><a href="../vedtægter">Vedtægter</a></li>
				<li><a href="../referat">Referater</a></li>
				<li><p>lasaga</p></li>
				<li><a href="../ADSL_Ansøgningsskema.docx">Pengeformular</a></li>
			</ul>
		</nav>
		<main>
			<h1>ADSLs Referater</h1>
''');

print("\t\t\t<h2>Referater fra generalforsamlinger:</h2>");
print(indent(walk("generalforsamlinger"), '\t'*3));

print("\t\t\t<h2>Referater fra bestyrelsesmøder:</h2>");
print(indent(walk("bestyrelsesmøder"), '\t'*3));

print("\t\t\t<h2>Referater fra aktiv over møder:</h2>");
print(indent(walk("Aktiv over møder"), '\t'*3));

print('''
		</main>
	</body>
</html>
''');
