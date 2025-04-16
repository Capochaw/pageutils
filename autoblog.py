import os

def ghtml(f):
    files = sorted(os.listdir(f))
    
    html = """
    <html lang="en">
    	<head>
    		<meta charset="utf-8"/>
    		<title>Blog - Capocha!!!!</title>
    		<link rel="icon" type="image/x-icon" href="img/icon.png">
    
    		<link rel="stylesheet" href="styles.css">
    	</head>
    
    	<body>
    		<script src="script.js"></script>
    		<div class="background"></div>
    		<div class="homeclass">
    			<a href="index.html"><img class="imagecenter" href="index.html" src="themes/serious/bg.png" style="align: center"></a>
    			<hr>
    			<div class="titlelist">
    				<a href ="blog.html">Blog</a>
    				<a href ="aboutme.html">About Me</a> 
    				<a href ="interestinglinks.html">Interesting Links</a>
    				<a href ="mat/index.html">Math</a>
    				<a href ="mus/1.html">Music</a>
    				<a href ="programs.html">Programs</a>
    			<hr>
    			</div>
    		</div>
    
    		<div class="bodyclass">
    			<div class="mdtext">
    """.format(f)

    last = """
	        </div>
		</div>
		<img class="roll" src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2xjNWNmbjg5cmR3MWd5Y3o1aWVvODR0ejU3NGRzajc0aXFnbTdxOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/ABn9FYVUMnOD0gKX8h/giphy.gif" onclick="roll()">
	</body>
</html>
    """
    
    na = 0
    nb = 0
    for i in files:
        # if is a folder, do the same logic that this for with the difference
        # that it will generate another index html using the previous given
        # format.
        nb = (int)(i[:4])
        if(nb > na):
            html+= f"<h1># {nb}</h1>"
        html += f"<li><span style=\"font-size: 1.2em\">[{i[5:10]}]</span> <a href=\"blog/{i}\">{i[11:-5]}</a></li>\n"
        na = nb
    
    html += last
    
    with open("/home/capocha/doc/code/page/blog.html", "w") as file:
        file.write(html)

ghtml("/home/capocha/doc/code/page/blog") 
