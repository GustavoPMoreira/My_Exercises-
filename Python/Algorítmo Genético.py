def Radomizer(vet_Popl):            #para fazer as gerações
def Fitness():                      #para selecionar as melhores
def Elite():                        #para guardar as melhores
    elite=[0]*elite_Size
def Mutations():                    #para realizar as permutas/crossover e testar os elites
def Distance():                     #calular dist com base nas coordenadas geográficas
if __name__=="__main__":
    n_Popl=8                        #num da população
    crossover_Rate=60               #razão de cruzamento em %
    max_Time=5                      #tempo de execução em s
    elite_Size= (n_Pop/4)           #num de indivíduos sobreviventes p/ a prox geração
    
    #Preencher o vetor de população com os indivíduos
    vet_Popl=[]
    vet_Popl[0]=[{"Nome: ", "Ramon"},lat=-19.875440126097473,long= -43.99395889404765]
    vet_Popl[1]=[{"Nome: ", "Thiago"},lat=-19.9112642220262,long=-43.9665747166668]
    vet_Popl[2]=[{"Nome: ", "Maria"},lat=-19.8889260414279,long=-43.9121776369095]
    vet_Popl[3]=[{"Nome: ", "José"},lat=-19.890883425917300,long=-44.00176811846610]
    vet_Popl[4]=[{"Nome: ", "Willian"},lat=-19.8414043223245,long=-43.9628168644166]
    vet_Popl[5]=[{"Nome: ", "Vagner"},lat=-19.9269539892564,long=-43.9905188489782]
    vet_Popl[6]=[{"Nome: ", "Augusto"},lat=-19.9433084034906,long=-44.0206586079846]
    vet_Popl[7]=[{"Nome: ", "Fernanda"},lat=-19.9448708383017,long=-44.0442606989504]
    vet_Popl[8]=[{"Nome: ", "Lucas"},lat=-19.9753873003267,long=-44.0127912446961]
    vet_Popl[9]=[{"Nome: ", "Marcos"},lat=-19.960919132597,long=-43.9738817918832]
    vet_Popl[10]=[{"Nome: ", "Daniel"},lat=-19.9552215904093,long=-43.9355356781923]

#inicialização
#Randomizar as gerações