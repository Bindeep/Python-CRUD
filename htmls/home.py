var_html = """
<html>
	<head>
		<meta charset="UTF-8">
		<link rel="stylesheet" type="text/css" href="style.css">
		
	</head>
	<body>
			<table id="userprofile" width="80%" align="center">
					<tr>
					  <th>Full Name</th>
					  <th>Email</th>
					  <th>Phone</th>
					  <th>DOB</th>
					  <th>ACTIONS</th>
					</tr>
					<tr>
						{table_body}
					</tr>
				  </table>
		
	<body>
</html>
"""


def write_data(datas):
	table_body = ''
	for data in datas:
		body = ''
		for items in data[1:5]:
			body += f'<td> {items} </td>'
		body += f'<td> {action_fields(data[0])} </td>'
		table_body += f'<tr> {body} </tr>'
	return var_html.format(table_body=table_body)

def action_fields(id):
	view_html = f"""<a href="home/{id}"><input type="button" value="View" on></></a> """

	update_html = f"""<a href="{id}/update"><input type="button" value="update"></></a> """

	delete_html = f"""<a href="{id}/delete"><input type="button" value="delete"></></a> """

	return view_html + update_html + delete_html

	