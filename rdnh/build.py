import os
from pathlib import Path
import subprocess
import sys

PANDOC = 'pandoc'

def main():
	force_rebuild = len(sys.argv) > 1 and (sys.argv[1] == 'force' or sys.argv[1] == 'force-rebuild')
	count = 0
	
	src_files = [path for path in Path('./markdown/').rglob('*.md')]
	for src in src_files:
		out = Path(str(src.resolve()).replace('.md', '.html').replace('markdown', 'html'))
		
		should_build = True
		
		if not force_rebuild and out.is_file():
			should_build = os.path.getmtime(src) > os.path.getmtime(out)
		
		if should_build:
			str_src = str(src)
			options = [PANDOC, str_src, '-o', str(out)]
			options += ['--from=gfm', '--standalone', '--embed-resources', '--css', 'html/style.css', '--highlight-style', 'mana.theme', '--lua-filter=filter_title.lua']
			
			print('Converting ' + str_src)
			subprocess.check_call(options)
			count += 1
			
	if count == 0:
		print('Nothing to be done -- all html files are up to date.')
		
if __name__ == '__main__':
	main()