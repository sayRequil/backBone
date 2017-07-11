import version
from mako.template import Template
def run(n):
	file = Template(filename=n)
	print(file.render(vers=version.vers)