html_text = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Markmap</title>
    <style>
    svg.markmap {{
        width: 100%;
        height: 100vh;
    }}
    </style>
    <script src="https://cdn.jsdelivr.net/npm/markmap-autoloader@0.18"></script>
</head>
<body>
<div class="markmap">
<script type="text/template">
{mindmap_text}
</script>
</div>
</body>
</html>
"""

iframe_html = """
<!DOCTYPE html>
<html>
<head>
<title>Embedded Markmap</title>
<style>
body {{
    background-color: white;
    height: 100vh;
    width: 100%;
    margin: 0;
    padding: 0;
}}
iframe {{
    width: 100%;
    height: 100vh;
    border: none;
}}
</style>
</head>
<body>
    <iframe srcdoc='{html_text}' style="width: 100%; height: 100vh;" frameborder="0"></iframe>
</body>
</html>
"""