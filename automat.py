import os

def ghtml(f):

    first ="""
    <html lang="en">
    	<head>
    		<meta charset="utf-8"/>
    		<title>Math - Capocha!!!</title>
    		<link rel="icon" type="image/x-icon" href="../img/icon.png">
    
    		<link rel="stylesheet" href="styles.css">
    	</head>
    
    	<body>
    		<script src="script.js"></script>
    		<div class="background"></div>
    		<div class="homeclass">
    			<a href="../index.html"><img class="imagecenter" href="../index.html" src="../themes/serious/bg.png" style="align: center"></a>
    			<hr>
    			<div class="titlelist">
    				<a href ="../blog.html">Blog</a>
    				<a href ="../aboutme.html">About Me</a> 
    				<a href ="../interestinglinks.html">Interesting Links</a>
    				<a href ="../mat/index.html">Math</a>
    				<a href ="../mus/1.html">Music</a>
    				<a href ="../programs.html">Programs</a>
    			<hr>
    			</div>
    		</div>
    
    		<div class="bodyclass">
    """
    first2 ="""
    <html lang="en">
    	<head>
    		<meta charset="utf-8"/>
    		<title>Math - Capocha!!!</title>
    		<link rel="icon" type="image/x-icon" href="../../../img/icon.png">
    
    		<link rel="stylesheet" href="../../styles.css">
    	</head>
    
    	<body>
    		<script src="../../script.js"></script>
    		<div class="background"></div>
    		<div class="homeclass">
    			<a href="../../../index.html"><img class="imagecenter" href="../../../index.html" src="../../../themes/serious/bg.png" style="align: center"></a>
    			<hr>
    			<div class="titlelist">
    				<a href ="../../../blog.html">Blog</a>
    				<a href ="../../../aboutme.html">About Me</a> 
    				<a href ="../../../interestinglinks.html">Interesting Links</a>
    				<a href ="../../../mat/index.html">Math</a>
    				<a href ="../../../mus/1.html">Music</a>
    				<a href ="../../../programs.html">Programs</a>
    			<hr>
    			</div>
    		</div>
    
    		<div class="bodyclass">
    """
    last = """
    		</div>
    
    		<img class="roll" src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2xjNWNmbjg5cmR3MWd5Y3o1aWVvODR0ejU3NGRzajc0aXFnbTdxOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/ABn9FYVUMnOD0gKX8h/giphy.gif" onclick="roll()">
    	</body>
    </html>
    """
    files = sorted(os.listdir(f))
    folds = []
    fields = []
    for i in files:
        if(os.path.isdir(os.path.join(f,i))):
           folds.append(i)
        else:
           fields.append(i)

    html = first

    for i in folds:
        html += f"<li><a href=\"post/{i}/index.html\">{i}</a>)</li>"

    for i in fields:
        html += f"<li><span style=\"font-size: 1.2em\">[{i[:5]}]</span> <a href=\"post/{i}\">{i[6:-5]}</a></li>"

    html += last

    with open("/home/capocha/doc/code/page/mat/index.html", "w") as file:
        file.write(html)

    for i in folds:
        html = first2
        files = sorted(os.listdir(f"{f}/{i}"))
        folds = []
        fields = []

        for q in files:
            if(not os.path.isdir(os.path.join(f,q))):
                fields.append(q)

        fields.remove("index.html")
        for q in fields:
            html += f"<li><span style=\"font-size: 1.2em\">[{q[:5]}]</span> <a href=\"post/{i}/{q}\">{q[6:-5]}</a></li>"

        html += last

        with open(f"/home/capocha/doc/code/page/mat/post/{i}/index.html", "w") as file:
            file.write(html)

ghtml("/home/capocha/doc/code/page/mat/post") 
