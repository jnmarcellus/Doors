#+------------------------------------------------------------+
# | Module Name:        Create HTML                            |
# | Module Purpose:     Create HTML Files                      |
# | Module Modifier:    John Marcellus                         |
# | Module Date:        8/31/2017                              |
# +------------------------------------------------------------

# Import modules

# Definitions

#------------------------------------------------------------------------------------------------------------------------------------------------------#
html_str = """
<table border=1>
     <tr>
       <th>Number</th>
       <th>Square</th>
     </tr>
     <indent>
     <% for i in range(10): %>
       <tr>
         <td><%= i %></td>
         <td><%= i**2 %></td>
       </tr>
     </indent>
</table>
"""

Html_file=open("filename.html","w")
Html_file.write(html_str)
Html_file.close()