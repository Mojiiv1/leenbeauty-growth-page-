from pathlib import Path
import base64
root=Path(__file__).resolve().parent.parent
html=(root/'index.html').read_text()
css=(root/'styles.css').read_text()
js=(root/'script.js').read_text()
html=html.replace('<link rel="stylesheet" href="styles.css">','<style>\n'+css+'\n</style>')
html=html.replace('<script defer src="script.js"></script>','')
html=html.replace('</body>','<script>\n'+js+'\n</script>\n</body>')
for path in (root/'assets').iterdir():
 mime='image/png' if path.suffix.lower()=='.png' else 'image/webp'
 data='data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()
 html=html.replace('assets/'+path.name,data)
(root/'qa'/'preview_inlined.html').write_text(html)
Path('/mnt/data/Leen_Growth_Page_Preview.html').write_text(html)
print('Preview ready:',len(html),'bytes')
