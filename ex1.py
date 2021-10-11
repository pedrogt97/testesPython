class Time:
    def __init__(self, nroDePontos, golsPro, golsContra, partidasJogadas) :
       self.nroDePontos = nroDePontos
       self.golsPro = golsPro
       self.golsContra = golsContra
       self.partidasJogadas = partidasJogadas
    
    def mediaDeGolsPorPartida(self):
        return self.golsPro/self.partidasJogadas
    
    def mediaDePontosPorPartida(self):
        return self.nroDePontos/self.partidasJogadas
    
    def saldoDeGols(self):
        return self.golsPro - self.golsContra

    # resultado é uma das strings: "vitoria","empate","derrota"
    def informaPartida(self, resultado , golsPro, golsContra):
        if resultado.lower() not in ['vitoria','empate','derrota']:
            return False
        if(resultado.lower() == "vitoria"):
            self.nroDePontos += 3
        elif(resultado.lower() == "empate"):
            self.nroDePontos += 1
        self.golsPro += golsPro
        self.golsContra += golsContra
        self.partidasJogadas += 1
        return True

    def status(self):
        print(""" 
            Partidas Jogadas: {} 
            Pontos feitos: {} 
            Saldo de gols: {}  
            Media de Gols por partida: {}  
            Media de pontos por partida: {} """.format(self.partidasJogadas,self.nroDePontos,self.saldoDeGols(),self.mediaDeGolsPorPartida(),self.mediaDePontosPorPartida()))
    

############    TESTE  
# santos = Time(35,40,50,30)
# santos.status()
# f = santos.informaPartida('vitoria',1,0)
# print(f)
# santos.status()
# f = santos.informaPartida('teste',1,0)
# print(f)


             