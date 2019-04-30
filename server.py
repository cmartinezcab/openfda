import http.server
import socketserver
import requests

# -- IP and the port of the server
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8009


# HTTPRequestHandler class
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):       #Sobrescritura porque mi padre tiene otro metodo do_GET. Este metodo hace un get.

        self.send_response(200)     #Mostrando que esta bien
        self.send_header('Content-type', 'text/html')      #La cabecera que pasamos
        self.end_headers()


        #MEDICAMENTOS
        if self.path == '/':

            message = """
            <!DOCTYPE html>
            <html>
            <body>
            <h2>Farmacos</h2>
            <form action="searchDrug" method="get">
                Ingrediente activo:<br>
                <input type="text" name="active_ingredient" value=""><br>
                <input type="submit" value="Submit">
            </form>
            </body>
            </html>
            """
            #print(message)
            self.wfile.write(bytes(message, "utf8"))
        elif self.path.startswith("/searchDrug?"):
            #print(self.path)
            medicamento = self.path.lstrip(self.path[:28]).strip('=')
            #print(medicamento)
            med =str("https://api.fda.gov/drug/label.json?search=active_ingredient:"+medicamento+"&limit=5")
            enlace = requests.get(med)
            contenido = enlace.json()
            #print(contenido)

            primero= """
            <!DOCTYPE html>
            <html>
            <body>

            <ul style="list-style-type:square;">
            """
            ultimo= """
            </ul>
            </body>
            </html>
            """

            lista=[]
            try:
                for result in contenido['results']:

                    resultado = result["openfda"]["generic_name"]
                    #print(resultado)
                    for i in resultado:
                        lista.append('<li>'+str(i)+'</li>')

                    for elem in lista:
                        element=str(elem)
                        fin= primero+element+ultimo
                    #print(fin)
                    self.wfile.write(bytes(fin, "utf8"))
            except KeyError:
                print('No esta disponible esa informacion')
            #print(lista)


        #COMPAÑIAS
        if self.path == '/':

            message = """
            <!DOCTYPE html>
            <html>
            <body>
            <h2>Empresas</h2>
            <form action="searchCompany" method="get">
                Empresa:<br>
                <input type="text" name="company" value=""><br>
                <input type="submit" value="Submit">
            </form>
            </body>
            </html>
            """
            self.wfile.write(bytes(message, "utf8"))

        elif self.path.startswith("/searchCompany?"):
            company = self.path.lstrip(self.path[:19]).strip('=')
            #print(company)
            comp =str("https://api.fda.gov/drug/label.json?search=company="+company+"&limit=5")
            enlace2 = requests.get(comp)
            contenido2 = enlace2.json()
            #print(contenido2)
            primero= """
            <!DOCTYPE html>
            <html>
            <body>

            <ul style="list-style-type:square;">
            """
            ultimo= """
            </ul>
            </body>
            </html>
            """
            lista2=[]
            try:
                for result2 in contenido2['results']:
                    resultado2 = result2["openfda"]["manufacturer_name"]
                    for it in resultado2:
                        lista2.append('<li>'+str(it)+'</li>')
                    for item in lista2:
                        itemi=str(item)
                        final= primero+itemi+ultimo
                    self.wfile.write(bytes(final, "utf8"))
            except KeyError:
                print('No esta disponible esa informacion')



        #LISTA DE MEDICAMENTOS
        if self.path=='/':
            message = """
            <!DOCTYPE html>
            <html>
            <body>
            <h2>Lista de Medicamentos</h2>
            <form action="listDrugs" method="get">
                Lista de Medicamentos:<br>
                <input type="submit" value="Submit">
            </form>
            </body>
            </html>
            """
            self.wfile.write(bytes(message, "utf8"))

        elif self.path.startswith("/listDrugs"):
            #print(self.path)
            #print(company)
            DRUG =str("https://api.fda.gov/drug/label.json?search=openfda.product_type:ANIMAL COMPUNDED DRUG LABEL&limit=10")
            enlace3 = requests.get(DRUG)
            contenido3 = enlace3.json()
            #print(contenido2)
            primero= """
            <!DOCTYPE html>
            <html>
            <body>

            <ul style="list-style-type:square;">
            """
            ultimo= """
            </ul>
            </body>
            </html>
            """
            lista3=[]
            for result3 in contenido3['results']:
                try:
                    resultado3 = result3["openfda"]["generic_name"]
                    for i in resultado3:
                        lista3.append('<li>'+str(i)+'</li>')
                    for elem in lista3:
                        element=str(elem)
                        fin= primero+element+ultimo
                    self.wfile.write(bytes(fin, "utf8"))
                except KeyError:
                    print('No esta disponible esa informacion')



        #LISTA DE COMPAÑIAS
        if self.path=='/':
            message = """
            <!DOCTYPE html>
            <html>
            <body>
            <h2>Lista de Empresas</h2>
            <form action="listCompanies" method="get">
                Lista de Empresas:<br>
                <input type="submit" value="Submit">
            </form>
            </body>
            </html>
            """
            self.wfile.write(bytes(message, "utf8"))

        elif self.path.startswith("/listCompanies"):
            #print(self.path)
            #print(company)
            DRUG =str("https://api.fda.gov/drug/label.json?search=openfda.product_type:ANIMAL COMPUNDED DRUG LABEL&limit=10")
            enlace3 = requests.get(DRUG)
            contenido3 = enlace3.json()
            #print(contenido2)
            primero= """
            <!DOCTYPE html>
            <html>
            <body>

            <ul style="list-style-type:square;">
            """
            ultimo= """
            </ul>
            </body>
            </html>
            """
            lista3=[]
            for result3 in contenido3['results']:
                try:
                    resultado3 = result3["openfda"]["manufacturer_name"]
                    for i in resultado3:
                        lista3.append('<li>'+str(i)+'</li>')
                    for elem in lista3:
                        element=str(elem)
                        fin= primero+element+ultimo
                    self.wfile.write(bytes(fin, "utf8"))
                except KeyError:
                    print('No esta disponible esa informacion')


        #elif self.path.startswith("searchDrug?"):
        #    comp = str("https://api.fda.gov/drug/label.json?search=company:"+company+"&limit=5")
        #    for result in comp['results']:
        #        campo1= result["openfda"]
        #        compania= campo1["manufacter_name"]
#Company:<br>
#<input type="text" name="company" value=""><br><br>
#+"&company="+"<company_name>"
#company = "<company_name>"

        print("File served!")
        return

Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("serving at port", PORT)
try:
    httpd.serve_forever()        #Bucle sockets que tenia el otro servidor
except KeyboardInterrupt:
        pass

httpd.server_close()
print("")
print("Server stopped!")


# https://github.com/joshmaker/simple-python-webserver/blob/master/server.py
