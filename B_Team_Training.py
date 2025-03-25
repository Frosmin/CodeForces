
def quitar_fuertes(a, x):
    fuertes = []
    debiles = []
    for num in a:
        if num >= x:
            fuertes.append(num)
        else:
            debiles.append(num)
    return len(fuertes), debiles

#una lista de debiles
def max_strong_teams(skills, x):
    skills.sort(reverse=True)  
    strong_teams = 0
    team = []
    for skill in skills:
        team.append(skill)
        team_size = len(team)
        team_min = min(team)
        team_strength = team_size * team_min 
        if team_strength >= x:
            strong_teams += 1
            team = []  
    return strong_teams
        
        
    
    
    


s = int(input())
for _ in range(s):
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    cont = 0
    p , lista = quitar_fuertes(a, x)
    cont += p
    cont += max_strong_teams(lista, x)
    print(cont)