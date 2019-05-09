import http.server
import socketserver
import requests



# -- IP and the port of the server
IP = "127.0.0.1"  # Localhost means "I": your local machine
PORT = 8000



# HTTPRequestHandler class
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):       #Sobrescritura porque mi padre tiene otro metodo do_GET. Este metodo hace un get.

        self.send_response(200)     #Mostrando que esta bien
        self.send_header('Content-type', 'text/html')      #La cabecera que pasamos
        self.end_headers()


        #MEDICAMENTOS
        def Medicamento():
            if self.path == '/':
                message = """
                <!DOCTYPE html>
                <html>
                <body>
                <h2>Farmacos</h2>
                <form action="searchDrug" method="get">
                    Ingrediente activo:<br>
                    <input type="text" name="active_ingredient" value=""><br>
                    Limite:<br>
                    <input type="text" name="limit" value=""><br>
                    <input type="submit" value="Submit">
                </form>
                </body>
                </html>
                """

                self.wfile.write(bytes(message, "utf8"))


            elif self.path.startswith("/searchDrug?"):
                path = self.path.split('&')
                medicamento = path[0].lstrip(self.path[:29])
                #print(medicamento)
                try:
                    limite= int(path[1].lstrip(path[1][:6]))

                except (ValueError, IndexError):
                    limite=10


                #print(limite)
                #print(self.path)
                med ="https://api.fda.gov/drug/label.json?search=active_ingredient:"+medicamento+"&limit="+str(limite)
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
                for i in range(limite):
                    try:
                        resultado=contenido["results"][i]["openfda"]["generic_name"]
                        #print(resultado)
                        for item in resultado:
                            lista.append('<li>'+str(item)+'</li>')
                    except KeyError:
                        lista.append('<li>'+'Nombre no encontrado'+'</li>')
                    for elem in lista:
                        element=str(elem)
                        fin= primero+element+ultimo
                    self.wfile.write(bytes(fin, "utf8"))
            return




        #COMPAÑIAS
        def Empresas():
            if self.path == '/':
                message = """
                <!DOCTYPE html>
                <html>
                <body>
                <h2>Empresas</h2>
                <form action="searchCompany" method="get">
                    Empresa:<br>
                    <input type="text" name="company" value=""><br>
                    Limite:<br>
                    <input type="text" name="limit" value=""><br>
                    <input type="submit" value="Submit">
                </form>
                </body>
                </html>
                """
                self.wfile.write(bytes(message, "utf8"))

            elif self.path.startswith("/searchCompany?"):
                path = self.path.split('&')
                company = path[0].lstrip(self.path[:20])
                #print(company)
                try:
                    limite= int(path[1].lstrip(path[1][:6]))

                except (ValueError, IndexError):
                    limite=10

                comp ="https://api.fda.gov/drug/label.json?search=active_ingredient:"+company+"&limit="+str(limite)
                enlace = requests.get(comp)
                contenido = enlace.json()

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
                for i in range(limite):
                    try:
                        resultado = contenido["results"][i]["openfda"]["manufacturer_name"]
                        print(resultado)

                        for item in resultado:
                            lista.append('<li>'+str(item)+'</li>')
                    except KeyError:
                        lista.append('<li>'+'Empresa no encontrada'+'</li>')
                    for elem in lista:
                        element=str(elem)
                        fin= primero+element+ultimo
                    self.wfile.write(bytes(fin, "utf8"))
            return


        #LISTA DE MEDICAMENTOS
        def Lista_Medicamentos(limite=10):
            if self.path=='/':
                message = """
                <!DOCTYPE html>
                <html>
                <body>
                <h2>Lista de Medicamentos</h2>
                <form action="listDrugs" method="get">
                    Lista de Medicamentos:<br>
                    Limite:<br>
                    <input type="text" name="limit" value=""><br>
                    <input type="submit" value="Submit">
                </form>
                </body>
                </html>
                """
                self.wfile.write(bytes(message, "utf8"))

            elif self.path.startswith("/listDrugs?"):
                path = self.path.split('?')
                try:
                    limite= int(path[1].lstrip(path[1][:6]))

                except (ValueError, IndexError):
                    limite=10

                DRUG ="https://api.fda.gov/drug/ndc.json?count=generic_name.exact&limit="+str(limite)
                enlace = requests.get(DRUG)
                contenido = enlace.json()

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
                for i in range(limite):
                    try:
                        resultado = contenido['results'][i]["term"]
                        print(resultado)
                        lista.append('<li>'+str(resultado)+'</li>')
                    except KeyError:
                        lista.append('<li>'+'Medicamento no encontrado'+'</li>')
                    for elem in lista:
                        element=str(elem)
                        fin= primero+element+ultimo
                    self.wfile.write(bytes(fin, "utf8"))
            return


        #LISTA DE COMPAÑIAS
        def Lista_Empresas():
            if self.path=='/':
                message = """
                <!DOCTYPE html>
                <html>
                <body>
                <h2>Lista de Empresas</h2>
                <form action="listCompanies" method="get">
                    Lista de Empresas:<br>
                    Limite:<br>
                    <input type="text" name="limit" value=""><br>
                    <input type="submit" value="Submit">
                </form>
                </body>
                </html>
                """
                self.wfile.write(bytes(message, "utf8"))

            elif self.path.startswith("/listCompanies?"):
                path = self.path.split('?')
                try:
                    limite= int(path[1].lstrip(path[1][:6]))

                except (ValueError, IndexError):
                    limite=10

                empres ="https://api.fda.gov/drug/ndc.json?count=openfda.manufacturer_name.exact&limit="+str(limite)
                enlace = requests.get(empres)
                contenido = enlace.json()

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
                for i in range(limite):
                    try:
                        resultado = contenido['results'][i]["term"]
                        lista.append('<li>'+str(resultado)+'</li>')
                    except KeyError:
                        lista.append('<li>'+'Empresa no encontrada'+'</li>')
                    for elem in lista:
                        element=str(elem)
                        fin= primero+element+ultimo
                    self.wfile.write(bytes(fin, "utf8"))
            return


        def Warnings():
            if self.path == '/':
                message = """
                <!DOCTYPE html>
                <html>
                <body>
                <h2>Precauciones</h2>
                <form action="listWarnings" method="get">
                    Precauciones:<br>
                    Limite:<br>
                    <input type="text" name="limit" value=""><br>
                    <input type="submit" value="Submit">
                </form>
                </body>
                </html>
                """
                self.wfile.write(bytes(message, "utf8"))

            elif self.path.startswith("/listWarnings?"):
                path = self.path.split('?')
                try:
                    limite= int(path[1].lstrip(path[1][:6]))

                except (ValueError, IndexError):
                    limite=10

                warn ="https://api.fda.gov/drug/label.json?search=warnings&limit="+str(limite)
                enlace = requests.get(warn)
                contenido = enlace.json()

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

                for i in range(limite):
                    try:
                        resultado = contenido['results'][i]["warnings"]
                        for item in resultado:
                            lista.append('<li>'+str(item)+'</li>')
                    except KeyError:
                        lista.append('<li>'+'Precaucion no encontrada'+'</li>')
                    for elem in lista:
                        element=str(elem)
                        fin= primero+element+ultimo
                    self.wfile.write(bytes(fin, "utf8"))
            return

        Medicamento()
        Empresas()
        Lista_Medicamentos()
        Lista_Empresas()
        Warnings()




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

socketserver.TCPServer.allow_reuse_address = True

# https://github.com/joshmaker/simple-python-webserver/blob/master/server.py
