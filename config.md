# Liste des configs GNS3

## Configuration des interfaces

---

### R1

#### R1 - R4
    configure terminal
    interface FastEthernet0/0
    ip address 1.0.1.1 255.255.255.0
    no shutdown
    end 

#### R1 - R2
    configure terminal
    interface GigabitEthernet1/0
    ip address 1.0.2.1 255.255.255.0
    no shutdown 
    end 

#### R1 - R5 
    configure terminal
    interface GigabitEthernet3/0
    ip address 1.0.9.1 255.255.255.0
    no shutdown
    end 

#### R1 - R6
    configure terminal
    interface GigabitEthernet2/0
    ip address 1.0.6.1 255.255.255.0
    no shutdown 
    end 

#### Loopback
    configure terminal
    interface Loopback0
    ip address 1.1.1.1 255.255.255.255
    no shutdown
    end

---
    write
---

### R2

#### R2 - R3
    configure terminal
    interface FastEthernet0/0
    ip address 1.0.3.1 255.255.255.0
    no shutdown 
    end

#### R2 - R1
    configure terminal
    interface GigabitEthernet1/0
    ip address 1.0.2.2 255.255.255.0
    no shutdown
    end

#### R2 - R5
    configure terminal 
    interface GigabitEthernet2/0
    ip address 1.0.5.1 255.255.255.0
    no shutdown
    end 

#### R2 - R6
    configure terminal 
    interface GigabitEthernet3/0
    ip address 1.0.10.1 255.255.255.0
    no shutdown
    end 

#### Loopback
    configure terminal
    interface Loopback0
    ip address 2.2.2.2 255.255.255.255
    no shutdown
    end

---
    write
---

### R3

#### R3 - R2
    configure terminal
    interface FastEthernet0/0
    ip address 1.0.3.2 255.255.255.0
    no shutdown 
    end

#### R3 - R4
    configure terminal
    interface GigabitEthernet1/0
    ip address 1.0.4.1 255.255.255.0
    no shutdown 
    end

#### R3 - R7
    configure terminal
    interface GigabitEthernet2/0
    ip address 1.0.7.1 255.255.255.0
    no shutdown 
    end

#### R3 - R8
    configure terminal
    interface GigabitEthernet3/0
    ip address 1.0.11.1 255.255.255.0
    no shutdown 
    end

#### Loopback
    configure terminal
    interface Loopback0
    ip address 3.3.3.3 255.255.255.255
    no shutdown
    end

---
    write
---

### R4

#### R4 - R1
    configure terminal
    interface FastEthernet0/0
    ip address 1.0.1.2 255.255.255.0
    no shutdown 
    end

#### R4 - R3
    configure terminal
    interface GigabitEthernet1/0
    ip address 1.0.4.2 255.255.255.0
    no shutdown 
    end

#### R4 - R8
    configure terminal
    interface GigabitEthernet2/0
    ip address 1.0.8.1 255.255.255.0
    no shutdown 
    end

#### R4 - R7
    configure terminal
    interface GigabitEthernet3/0
    ip address 1.0.12.1 255.255.255.0
    no shutdown 
    end

#### Loopback
    configure terminal
    interface Loopback0
    ip address 4.4.4.4 255.255.255.255
    no shutdown
    end

--- 
    write
---

### R5

#### R5 - R2
    configure terminal
    interface GigabitEthernet2/0
    ip address 1.0.5.2 255.255.255.0
    no shutdown 
    end

#### R5 - R1
    configure terminal
    interface GigabitEthernet3/0
    ip address 1.0.9.2 255.255.255.0
    no shutdown 
    end

#### R5 - Client 1
    configure terminal 
    interface FastEthernet0/0
    ip address 1.1.0.1 255.255.255.252
    no shutdown
    end

#### Loopback
    configure terminal
    interface Loopback0
    ip address 5.5.5.5 255.255.255.255
    no shutdown
    end

---
    write
---

### R6

#### R6 - R1
    configure terminal
    interface GigabitEthernet2/0
    ip address 1.0.6.2 255.255.255.0
    no shutdown 
    end

#### R6 - R2
    configure terminal
    interface GigabitEthernet3/0
    ip address 1.0.10.2 255.255.255.0
    no shutdown 
    end

#### R6 - Client 2
    configure terminal 
    interface FastEthernet0/0
    ip address 1.2.0.1 255.255.255.252
    no shutdown
    end

#### Loopback
    configure terminal
    interface Loopback0
    ip address 6.6.6.6 255.255.255.255
    no shutdown
    end

---
    write
---
### R7

#### R7 - R3
    configure terminal    neighbor 1.1.1.1 remote-as 111
    interface GigabitEthernet2/0
    ip address 1.0.7.2 255.255.255.0
    no shutdown 
    end

#### R7 - R4
    configure terminal
    interface GigabitEthernet3/0
    ip address 1.0.12.2 255.255.255.0
    no shutdown 
    end

#### R7 - Client 3
    configure terminal 
    interface FastEthernet0/0
    ip address 1.3.0.1 255.255.255.252
    no shutdown
    end

#### Loopback
    configure terminal
    interface Loopback0
    ip address 7.7.7.7 255.255.255.255
    no shutdown
    end

---
    write
---
### R8

#### R8 - R4
    configure terminal
    interface GigabitEthernet2/0
    ip address 1.0.8.2 255.255.255.0
    no shutdown 
    end

#### R8 - R3
    configure terminal
    interface GigabitEthernet3/0
    ip address 1.0.11.2 255.255.255.0
    no shutdown 
    end

#### R8 - Client 4
    configure terminal 
    interface FastEthernet0/0
    ip address 1.4.0.1 255.255.255.252
    no shutdown
    end

#### Loopback
    configure terminal
    interface Loopback0
    ip address 8.8.8.8 255.255.255.255
    no shutdown
    end

---
    write
---

### R9 - client1
#### R9-R5
    configure terminal
    interface f0/0
    ip address 1.1.0.1 255.255.255.252
    no shut
    end

#### R9-PC
    config term
    inter g1/0
    ip addr 192.168.1.1 255.255.255.0
    no shut
    end

#### R9-loop
    config term
    inter lo
    ip addr 9.9.9.9 255.255.255.255
    no sh
    end

Faire de meme pour R10/11/12

## OSPF

---

### R1

    configure terminal
    router ospf 1
    router-id 1.1.1.1
    end 
    configure terminal
    interface FastEthernet0/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet1/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet2/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet3/0
    ip ospf 1 area 0
    end
    configure terminal 
    inter l0
    ip ospf 1 area 0
    end

---
    write
---
changer le loopback comme l'exemple sur tous les routeurs du coeur (jsp si ça change qqchose mais mon tuto était fait comme ça)
### R2

    configure terminal
    router ospf 1
    router-id 2.2.2.2
    end 
    configure terminal
    interface FastEthernet0/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet1/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet2/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet3/0
    ip ospf 1 area 0
    end
    configure terminal 
    interface l0
    ip ospf 1 area 0
    end

---
    write
---

### R3

    configure terminal
    router ospf 1
    router-id 3.3.3.3
    end 
    configure terminal
    interface FastEthernet0/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet1/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet2/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet3/0
    ip ospf 1 area 0
    end
    configure terminal 
    router ospf 1
    network 3.3.3.3 0.0.0.0 area 0
    end

---
    write
---

### R4

    configure terminal
    router ospf 1
    router-id 4.4.4.4
    end 
    configure terminal
    interface FastEthernet0/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet1/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet2/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet3/0
    ip ospf 1 area 0
    end
    configure terminal 
    router ospf 1
    network 4.4.4.4 0.0.0.0 area 0
    end

---
    write
---

### R5

    configure terminal
    router ospf 1
    router-id 5.5.5.5
    end 
    configure terminal
    interface GigabitEthernet2/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet3/0
    ip ospf 1 area 0
    end
    configure terminal
    router ospf 1
    passive-interface FastEthernet0/0
    end
    configure terminal 
    router ospf 1
    network 5.5.5.5 0.0.0.0 area 0
    end

---
    write
---

### R6

    configure terminal
    router ospf 1
    router-id 6.6.6.6
    end 
    configure terminal
    interface GigabitEthernet2/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet3/0
    ip ospf 1 area 0
    endaddress-family ipv4
    configure terminal
    router ospf 1
    passive-interface FastEthernet0/0
    end
    configure terminal 
    router ospf 1
    network 6.6.6.6 0.0.0.0 area 0
    end

---
    write
---

### R7

    configure terminal
    router ospf 1
    router-id 7.7.7.7
    end 
    configure terminal
    interface GigabitEthernet2/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet3/0
    ip ospf 1 area 0
    end
    configure terminal
    router ospf 1
    passive-interface FastEthernet0/0
    end
    configure terminal 
    router ospf 1
    network 7.7.7.7 0.0.0.0 area 0
    end

---
    write
---

### R8

    configure terminal
    router ospf 1
    router-id 8.8.8.8
    end 
    configure terminal
    interface GigabitEthernet2/0
    ip ospf 1 area 0
    end
    configure terminal
    interface GigabitEthernet3/0
    ip ospf 1 area 0
    end
    configure terminal
    router ospf 1
    passive-interface FastEthernet0/0
    end
    configure terminal 
    router ospf 1
    network 8.8.8.8 0.0.0.0 area 0
    end

---
    write
---

Configurer OSPF area 2 sur tout les routeurs R9/10/11/12
sur les loopback, les interfaces vers le pc et l'interface vers le coeur
ATTENTION pas mettre de passive-interface ici

## MPLS

### R1, R2, R3, R4, R5, R6, R7, R8

    configure terminal
    router ospf 1
    mpls ldp autoconfig

---
    write
---


## BGP
Le faire que sur les routeurs de bordure suivant l'ex de R5 ci dessous
### R5

    configure terminal
    router bgp 111
    no sync
    bgp router-id 1.1.1.1
    neighbor 6.6.6.6 remote-as 111
    neighbor 6.6.6.6 update-source Loopback0
    neighbor 7.7.7.7 remote-as 111
    neighbor 7.7.7.7 update-source Loopback0
    neighbor 8.8.8.8 remote-as 111
    neighbor 8.8.8.8 update-source Loopback0
    no auto-summary
    address-family vpnv4
    neighbor 6.6.6.6 activate
    neighbor 7.7.7.7 activate
    neighbor 8.8.8.8 activate
    end

--- 
    write
---

## VRF
Le faire sur tous les routeurs de bordure avec les bons numéros en fonction des clients
### R5 - Client 1
    config t
    ip vrf client1
    rd 111:1
    route-target both 111:1
    exit
    inter f0/0
    ip vrf forwarding client1
    ip add 1.1.0.1 255.255.255.252 remettre l'adresse car elle est perdue par la vrf
    ip ospf 2 area 2
    router bgp 111
    address-family ipv4 vrf client1
    redistribute ospf 2
    exit
    exit
    router ospf 2
    redistribute bgp 111 subnets
    end

___
    write
___