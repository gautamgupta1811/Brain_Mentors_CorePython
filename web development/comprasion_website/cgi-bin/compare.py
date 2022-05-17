import model
import cgi

form = cgi.FieldStorage()
prod_1 = form.getvalue("prod_1")
prod_2 = form.getvalue("prod_2")
prod_1_data = model.data_reterival(prod_1)
prod_2_data = model.data_reterival(prod_2)
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
    <table style="border-spacing: 15px; border-collapse: seperate;">
        <tr style="padding: 15px; margin: 45px;">
            <th>
                Name
            </th>
            <th>
                {prod_1_data[0].upper()}
            </th>
            <th>
                {prod_2_data[0].upper()}
            </th>
        </tr>
        <tr style="padding: 15px; margin: 45px;">
            <td>
                Price
            </td>
            <td>
                {prod_1_data[1]}
            </td>
            <td>
                {prod_2_data[1]}
            </td>
        </tr>
        <tr style="padding: 15px; margin: 45px;">
            <td>
                Other Features
            </td>
            <td>
                {"<br>".join(prod_1_data[2])}
            </td>
            <td>
                {"<br>".join(prod_2_data[2])}
            </td>
        </tr>

    </table>
</body>
</html>
""")