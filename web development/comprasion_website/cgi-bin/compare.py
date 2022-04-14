import model
import cgi

form = cgi.FieldStorage()
prod_1 = form.getvalue("prod_1")
prod_2 = form.getvalue("prod_2")

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Compare</title>
</head>
<body style="background-color: whitesmoke;">
<h1> {prod_1} </h1>
<h1> {prod_2} </h1>
</body>
</html>
""")