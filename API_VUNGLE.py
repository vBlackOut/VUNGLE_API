import requests

class API_VUNGLE():

    def __init__(self, **kwargs):
        self.URL = "https://report.api.vungle.com/ext/pub/reports/performance"
        self.API = requests.Session()
        self.API.keep_alive = False
        self.headers = {'Authorization': 'Bearer {}'.format(kwargs['api_key']), 'Vungle-Version': '{}'.format(kwargs['version']), 'Accept': '{}'.format(kwargs['result'])}
         
    def generate_url(self, elements):
        generate_url = ""
        disable_options = ["_print"]
        for key, value in elements.items():
            for a in disable_options:
                if a != key:
                    if type(value) == list:
                        generate_url += "&" + key + "=" + ','.join(value)
                    else:
                        generate_url += "&" + key + "=" + value
                else:
                    print(" NOTICE: Disable options '{}' API for python".format(a))

        return generate_url

    def get(self, **kwargs):
        generate_url = self.generate_url(kwargs)
        resultAPI = self.API.get('{0}?{1}'.format(self.URL,generate_url), headers=self.headers)
        self.Close()
        if kwargs["_print"] == True:
            print(resultAPI.text, resultAPI.headers)
        return resultAPI.text


    def find_object(self, all_value, key):
        '''
        function for find element in dict python
        '''
        country_revenue_key = {}
        for i in enumerate(all_value.items()):
            if str(i[1][1][2]) == str(key):
               if i[1][1][0] in country_revenue_key.keys():
                    country_revenue_key[i[1][1][0]] = country_revenue_key[i[1][1][0]] + i[1][1][1]
               else:
                    country_revenue_key[i[1][1][0]] = i[1][1][1]

        return country_revenue_key

    def calcule_table(self, table1, table2):
        '''
        Function for calcule two dict sum one
        '''
        dict_value = {}
        for i, a in zip(table1.items(), table2.items()):
            if i[0] not in dict_value.values():
                dict_value[i[0]] = i[1] + a[1]

        return dict_value

    def Close(self):
        self.API.close()

    def generate_html(self, platform, platformT, platform_revenu, platform_revenu_total, country):
        html = """
        <!doctype html>
        <html lang="fr">
          <head>
          <meta charset="UTF-8">
          <style>
            td {
                height: 5px; 
                width: 75px;
              }

            table td {  
                text-align:right; 
                vertical-align:middle;
                font-size:14px;
              }
          </style>
          </head>
          <body>
            <h2>API VUNGLE</h2>
            <table>
            <theader>
               <th>Device</th>
        """

        platform_revenu = platform_revenu.items()
        platform_revenu_total = platform_revenu_total.items()

        for lens, i in enumerate(platform_revenu):
            for a, d in zip(i[1].values(), i[1].keys()):
                html += "       <th>{}</th> \n".format(d)
            if lens <= len(country):
                break
        html += "       <th>{}</th> \n".format(country[-1])
        html += "       <th>{}</th> \n".format("Total Summary")

        html += """
            </theader>
            <tbody>"""
        total_sum = []
        for i in platform_revenu:
            total_line = []
            html += """       <tr><td>{:>5s}</td>\n""".format(i[0])

            for a, d in zip(i[1].values(), i[1].keys()):
                #print(platform[i[0]][d])
                html += """           <td>{0:.{digits}f} €</td>\n""".format(platform[i[0]][d], digits=2)
                total_line.append(platform[i[0]][d])
            html += """           <td>{0:.{digits}f} €</td>\n""".format(platform[i[0]][d], digits=2)
            html += """           <td bgcolor="#D3D3D3"><b>{0:.{digits}f} €</b></td>\n""".format(sum(map(float, total_line)), digits=2)
            total_sum.append(sum(map(float, total_line)))
            html += """       </tr>\n"""
        for b, c in zip(platform_revenu_total,  platform_revenu):
            html += """       <tr><td><b>{:>5s}</b></td>\n""".format(b[0])
            for a, d in zip(b[1].values(), b[1].keys()):
                html += """           <td bgcolor="#D3D3D3">{0:.{digits}f} €</td>\n""".format(platformT[b[0]][d], digits=2)
            html += """           <td bgcolor="#D3D3D3">{0:.{digits}f} €</td>\n""".format(platformT[b[0]][d], digits=2)
            html += """           <td bgcolor="#D3D3D3"><font color='blue'><b>{0:.{digits}f} €</b></font></td>\n""".format(sum(map(float, total_sum)), digits=2)
            html += """       </tr>\n"""
        html += """</tbody>
            </table>
          </body>
        </html>
        """
        return html
    
    def save(self, filename, data):
        file = open(filename,"w+") 
        file.write(data) 
        file.close() 
