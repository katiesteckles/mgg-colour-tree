
<!DOCTYPE html>
<head>
	<title>Tree Editor</title>
	<style>
	div {
		width: 700px;
	}
	
	div p {
		width:600px;
	}
	
	div.inline {
		display: inline;
	}
	</style>

</head>

<body>
<?php $photcred = "This gadget was made by <a href=\"http://twitter.com/minigirlgeek\">Amy Mather</a>."; ?>
<div class="inline">
	<div width="100%">
	<h1>MGG IoFT Workshop - Customise Your Tree</h1>
	</div>
<div>
<svg xmlns="http://www.w3.org/2000/svg" id='svg' width='80.66mm' height='84.53mm'
	 viewBox="0 0 80.66 84.53">
<style type="text/css">
	.st0{fill:#FFFFFF;stroke:#000000;stroke-miterlimit:10;stroke-width:0.1mm;}
	.st1{font-family:'Verdana';}
	.st2{font-size:1mm;}
	.circle{fill:#000000; cursor:pointer;}
</style>
<polygon onclick="draw_circ(this)" class="st0" points="66.62,58.29 72.37,58.29 59.42,38.42 65.17,38.42 40.33,0.32 15.53,38.42 21.28,38.42 8.33,58.29 14.04,58.29 0.32,79.35 15.33,79.35 15.33,84.36 65.33,84.36 65.33,79.35 80.34,79.35"/>
<!--<polygon onclick="draw_circ(this)" class="st0" points="66.62,58.29 72.37,58.29 59.42,38.42 65.17,38.42 40.33,0.32 15.53,38.42 21.28,38.42 8.33,58.29 14.04,58.29 0.32,79.35 7.83,79.35 7.83,84.36 15.31,84.36 65.35,84.36 72.83,84.36 72.83,79.35 80.34,79.35"/>-->

<text id="name_loc" text-anchor="end" transform="matrix(1 0 0 1 64 83)" class="st1 st2">Your name here</text>
</svg>
</div>
<br>
<form>
	<input type="text" id='abc'/>
	<button type="button" onclick="update_name()">Update Name</button>   
	<input onchange="update_circle(this.value)" type="range" min="1" max="15" value="8" class="slider" id="radius" />
	<svg name='svg' xmlns="http://www.w3.org/2000/svg" id='svg' width='30px' height='30px'>
		<circle id="circlesize" cx=15 cy =15 r=8></circle>
	</svg>
	<br><br>
		<button type="button" onclick="send_treemail()">Send my tree!</button>
	<button type="button" onclick="clear_circs()">Clear baubles</button>
</form>
</div>
<div id='svgtext'>
</div>
<div>
<p><img src="/mggtree/tree.jpg" align="right" height=300 hspace=20>For our workshop on 10th December, you can design a custom tree using this gadget.</p>
	<p>Click on the tree to place a bauble. Click on a bauble to delete it. Use the slider below to edit the bauble's size before you place it. Make sure you have plenty of baubles!</p>
	<p>Input your name in the box so we can identify whose tree it is - this should match the name you've registered with on Eventbrite. It will be engraved onto the bottom edge of the tree, but won't be visible when it's assembled. Then click <b>Send my tree</b> to email us your design.</p>
	<p>If you submit more than one design before the workshop, we'll use the most recently submitted version. If you don't send us a design in advance of the workshop (deadline Friday 8th), we'll cut a generic tree design.</p>
</div>
</body>
<script>
var svg = document.getElementById("svg");
var svgNS = svg.namespaceURI;
var rectcount = 0;
var treedata = [];
function update_circle(value) {
	document.getElementById("circlesize").setAttribute('r', value);
}
function draw_circ(self) {
	var rect = document.createElementNS(svgNS, 'circle');
	var ev = window.event;
	var posX = (ev.clientX - self.parentNode.parentNode.offsetLeft) * 0.75;
	var posY = (ev.clientY - self.parentNode.parentNode.offsetTop + window.scrollY) * 0.75;
	rectcount = rectcount + 1;
	var radius = document.getElementById('radius').value;
	rect.setAttribute('onmousedown', 'del_rect(this)');
	rect.setAttribute('id', rectcount);
	rect.setAttribute('class', 'circle');
	rect.setAttribute('cx', posX * 0.352843395);
	rect.setAttribute('cy', posY * 0.352843395);
	rect.setAttribute('r', radius * 0.352843395);
	svg.appendChild(rect);
	treedata.push('x'+rect.getAttribute('cx')+'y'+rect.getAttribute('cy')+'r'+rect.getAttribute('r'));
	console.log(treedata);
	console.log(window.scrollY);

};
function send_treemail() {
treename = document.getElementById('abc').value;
if(treename===""){
	alert("Please enter your name and click 'Update name' before submitting your tree.")
	} else {	
	treestr = treedata.join('--');
	treestr = 'Please do not change any of the content of this email! Just hit send :)%0D%0A%0D%0A' + treestr + '---' + treename;
	window.open('mailto:manchestergirlgeeks+tree@gmail.com?subject=' + treename +'%27s%20Tree&body=' + treestr); 
	}
};

function del_rect(element){
	baubledata = 'x'+element.getAttribute('cx')+'y'+element.getAttribute('cy')+'r'+element.getAttribute('r');
	baubleindex = treedata.indexOf(baubledata);
	treedata.splice(baubleindex,1);
	element.parentNode.removeChild(element);
};
function clear_circs() {
	var paras = document.getElementsByClassName('circle');
	var len = paras.length;
	console.log(paras)
	for (var i = 0; i < len; i++) {
		console.log('bloop');
		element = paras[0];
		element.parentNode.removeChild(element);
	}
	
	treedata = [];
};
function update_name() {
	name = document.getElementById('abc').value;
	loc = document.getElementById('name_loc');
	loc.textContent = name;
};
/*function outputSVG() {
	var svg = document.getElementById("svg");
	var form = document.createElement("form2");
	form.setAttribute("method", "post");
	form.setAttribute("action", "<?=$_SERVER['PHP_SELF'];?>");
	var dataField = document.createElement("input");
	dataField.setAttribute("type", "hidden");
	dataField.setAttribute("name", "data");
	dataField.setAttribute("value", svg.outerHTML);
	form.appendChild(dataField);
	form.submit();
	console.log('success?');
};*/
</script>