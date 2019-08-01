def towerHanoi(n , from_rod, to_rod, aux_rod): 
    if n == 1: 
        print ("Move disk 1 from rod",from_rod,"to rod",to_rod )
        return 
    towerHanoi(n-1, from_rod, aux_rod, to_rod) 
    print ("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    towerHanoi(n-1, aux_rod, to_rod, from_rod)

n = 4
towerHanoi(n, 'A', 'C', 'B')