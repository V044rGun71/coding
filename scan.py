import nmap as n
import sys

print('','%'*41,'\n',' ','SCANNER DE PORTAS EM CONEXÕES TCP/UDP\n','%'*41)

#github.com/V044rGun71 ||| Coleta de argumentos ||| argv[1]:endereço argv[2]:porta

a=n.PortScanner()
a.scan(sys.argv[1],sys.argv[2])

for host in a.all_hosts():
    print('************************')
    print(f'[*] Endereço:{host} : {a[host].hostname()}')
    print(f'[*] Status:{a[host].state()}')
    
    for con in a[host].all_protocols():
        print('************************')
        print(f'[*] Protocolo : {con}')
        n_port=a[host][con].keys()
        n_port=list(n_port)
        n_port.sort()
        
        for port in n_port:
            print(f'[*] Porta: {port}')
            
            if a[host][con][port]["state"]=='open':
                print('[*] Estado: aberta')
            else:
                print('[*] Estado: fechada')
