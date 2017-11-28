def read_in_trees(path_of_file):
	with open(path_of_file, "r") as file:
		list_of_trees = file.readlines()[0].split("\r")
	for i in range(len(list_of_trees)):
		make_svg(list_of_trees[i],'/Users/katiesteckles/Dropbox/ManchesterGirlGeeks/trees/tree'+ str(i) +'.svg')

test_email_string = "x42.3412074y29.374212633750002r2.82274716--x54.24967198125y49.750918695r2.82274716--x23.28766407y65.0996063775r2.82274716--x23.28766407y53.72040688875r2.82274716--x49.750918695y68.53982947875001r2.82274716--x64.83497383125y73.038582765r4.23412074--x34.66686355875y36.78392392875r4.23412074--x37.048556475y14.02552495125r4.23412074--x37.5778215675y59.8069554525r4.23412074--x8.20360893375y73.038582765r4.23412074---Test Steckles"

def make_svg(email_string,svg_filename):
	xml_header = '''<svg xmlns="http://www.w3.org/2000/svg" id="svg" width="80.66mm" height="84.53mm" viewBox="0 0 80.66 84.53">
<style type="text/css">
	.st0{{fill:#FFFFFF;stroke:#000000;stroke-miterlimit:10;stroke-width:0.1mm;}}
	.st1{{font-family:'Verdana';}}
	.st2{{font-size:1mm;}}
	.circle{{fill:#000000; cursor:pointer;}}
</style>
<polygon onclick="draw_circ(this)" class="st0" points="66.62,58.29 72.37,58.29 59.42,38.42 65.17,38.42 40.33,0.32 15.53,38.42 21.28,38.42 8.33,58.29 14.04,58.29 0.32,79.35 15.33,79.35 15.33,84.36 65.33,84.36 65.33,79.35 80.34,79.35"></polygon>

<text id="name_loc" text-anchor="end" transform="matrix(1 0 0 1 64 83)" class="st1 st2">{}</text>
'''

	bauble_line = '''<circle onmousedown="del_rect(this)" id="bauble{}" class="circle" cx="{}" cy="{}" r="{}"></circle>
'''
	
	end_line = '</svg>'
	
	treename = email_string.split('---')[1]
	baubles = email_string.split('---')[0].split('--')
	
	with open(svg_filename, 'w') as file:
		file.write(xml_header.format(treename))
		for i in range(len(baubles)):
			x_coord = baubles[i].split('y')[0][1:]
			y_coord = baubles[i].split('y')[1].split('r')[0]
			radius = baubles[i].split('r')[1]
			file.write(bauble_line.format(i,x_coord,y_coord,radius))
		file.write(end_line)
		
read_in_trees("/Users/katiesteckles/Dropbox/ManchesterGirlGeeks/trees/treelist.txt")