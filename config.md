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

#### R4 - R3
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
    router ospf 1
    network 1.1.1.1 0.0.0.0 area 0
    end

---
    write
---

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
    router ospf 1
    network 2.2.2.2 0.0.0.0 area 0
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

R1 R2 R3 R4 fait
## MPLS

### R1, R2, R3 et R4

    configure terminal
    mpls ip
    mpls label protocol ldp 
    interface FastEthernet0/0
    mpls ip
    exit
    interface GigabitEthernet1/0
    mpls ip
    exit  
    interface GigabitEthernet2/0
    mpls ip
    exit
    interface GigabitEthernet3/0
    mpls ip
    end

---
    write
---

Fait R5 R6 R7 R8
### R5, R6, R7 et R8

    configure terminal
    mpls ip
    mpls label protocol ldp  
    interface GigabitEthernet2/0
    mpls ip
    exit
    interface GigabitEthernet3/0
    mpls ip
    end

--- 
write
---

## BGP

---
### R1

    configure terminal
    router bgp 111
    no sync
    bgp router-id 1.1.1.1
    address-family ipv4
    neighbor 2.2.2.2 remote-as 111
    neighbor 2.2.2.2 update-source Loopback0
    neighbor 2.2.2.2 activate
    network 1.1.1.0
    neighbor 3.3.3.3 remote-as 111
    neighbor 3.3.3.3 update-source Loopback0
    neighbor 3.3.3.3 activate
    network 1.1.1.0
    neighbor 4.4.4.4 remote-as 111
    neighbor 4.4.4.4 update-source Loopback0
    neighbor 4.4.4.4 activate
    network 1.1.1.0
    neighbor 5.5.5.5 remote-as 111
    neighbor 5.5.5.5 update-source Loopback0
    neighbor 5.5.5.5 activate
    network 1.1.1.0
    neighbor 6.6.6.6 remote-as 111
    neighbor 6.6.6.6 update-source Loopback0    
    neighbor 6.6.6.6 activate
    network 1.1.1.0
    neighbor 7.7.7.7 remote-as 111 
    neighbor 7.7.7.7 update-source Loopback0
    neighbor 7.7.7.7 activate
    network 1.1.1.0
    neighbor 8.8.8.8 remote-as 111
    neighbor 8.8.8.8 update-source Loopback0
    neighbor 8.8.8.8 activate
    network 1.1.1.0
    end

--- 
    write
---

### R2 

    configure terminal
    router bgp 111
    no sync
    bgp router-id 1.1.1.2
    address-family ipv4
    neighbor 1.1.1.1 remote-as 111
    neighbor 1.1.1.1 update-source Loopback0
    neighbor 1.1.1.1 activate
    network 1.1.1.0
    neighbor 3.3.3.3 remote-as 111 
    neighbor 3.3.3.3 update-source Loopback0   
    neighbor 3.3.3.3 activate
    network 1.1.1.0
    neighbor 4.4.4.4 remote-as 111
    neighbor 4.4.4.4 update-source Loopback0
    neighbor 4.4.4.4 activate
    network 1.1.1.0
    neighbor 5.5.5.5 remote-as 111
    neighbor 5.5.5.5 update-source Loopback0
    neighbor 5.5.5.5 activate
    network 1.1.1.0
    neighbor 6.6.6.6 remote-as 111
    neighbor 6.6.6.6 update-source Loopback0
    neighbor 6.6.6.6 activate
    network 1.1.1.0
    neighbor 7.7.7.7 remote-as 111
    neighbor 7.7.7.7 update-source Loopback0
    neighbor 7.7.7.7 activate
    network 1.1.1.0
    neighbor 8.8.8.8 remote-as 111
    neighbor 8.8.8.8 update-source Loopback0
    neighbor 8.8.8.8 activate
    network 1.1.1.0
    end

--- 
    write
---

### R3

    configure terminal
    router bgp 111
    no sync
    bgp router-id 1.1.1.3
    address-family ipv4
    neighbor 1.1.1.1 remote-as 111
    neighbor 1.1.1.1 update-source Loopback0
    neighbor 1.1.1.1 activate
    network 1.1.1.0
    neighbor 2.2.2.2 remote-as 111
    neighbor 2.2.2.2 update-source Loopback0
    neighbor 2.2.2.2 activate
    network 1.1.1.0
    neighbor 4.4.4.4 remote-as 111
    neighbor 4.4.4.4 update-source Loopback0
    neighbor 4.4.4.4 activate
    network 1.1.1.0
    neighbor 5.5.5.5 remote-as 111
    neighbor 5.5.5.5 update-source Loopback0
    neighbor 5.5.5.5 activate
    network 1.1.1.0
    neighbor 6.6.6.6 remote-as 111
    neighbor 6.6.6.6 update-source Loopback0
    neighbor 6.6.6.6 activate
    network 1.1.1.0
    neighbor 7.7.7.7 remote-as 111
    neighbor 7.7.7.7 update-source Loopback0
    neighbor 7.7.7.7 activate
    network 1.1.1.0
    neighbor 8.8.8.8 remote-as 111
    neighbor 8.8.8.8 update-source Loopback0
    neighbor 8.8.8.8 activate
    network 1.1.1.0
    end

--- 
    write
---

### R4

    configure terminal
    router bgp 111
    no sync
    bgp router-id 1.1.1.4
    address-family ipv4
    neighbor 1.1.1.1 remote-as 111
    neighbor 1.1.1.1 update-source Loopback0
    neighbor 1.1.1.1 activate
    network 1.1.1.0
    neighbor 2.2.2.2 remote-as 111
    neighbor 2.2.2.2 update-source Loopback0
    neighbor 2.2.2.2 activate
    network 1.1.1.0
    neighbor 3.3.3.3 remote-as 111
    neighbor 3.3.3.3 update-source Loopback0
    neighbor 3.3.3.3 activate
    network 1.1.1.0
    neighbor 5.5.5.5 remote-as 111
    neighbor 5.5.5.5 update-source Loopback0
    neighbor 5.5.5.5 activate
    network 1.1.1.0
    neighbor 6.6.6.6 remote-as 111
    neighbor 6.6.6.6 update-source Loopback0
    neighbor 6.6.6.6 activate
    network 1.1.1.0
    neighbor 7.7.7.7 remote-as 111
    neighbor 7.7.7.7 update-source Loopback0
    neighbor 7.7.7.7 activate
    network 1.1.1.0
    neighbor 8.8.8.8 remote-as 111
    neighbor 8.8.8.8 update-source Loopback0
    neighbor 8.8.8.8 activate
    network 1.1.1.0
    end

--- 
    write
---

### R5

    configure terminal
    router bgp 111
    no sync
    bgp router-id 1.1.1.5
    address-family ipv4
    neighbor 1.1.0.2 remote-as 211
    neighbor 1.1.0.2 activate
    neighbor 1.1.1.1 remote-as 111
    neighbor 1.1.1.1 update-source Loopback0
    neighbor 1.1.1.1 activate
    network 1.1.1.0
    neighbor 2.2.2.2 remote-as 111
    neighbor 2.2.2.2 update-source Loopback0
    neighbor 2.2.2.2 activate
    network 1.1.1.0
    neighbor 3.3.3.3 remote-as 111
    neighbor 3.3.3.3 update-source Loopback0
    neighbor 3.3.3.3 activate
    network 1.1.1.0
    neighbor 4.4.4.4 remote-as 111
    neighbor 4.4.4.4 update-source Loopback0
    neighbor 4.4.4.4 activate
    network 1.1.1.0
    neighbor 6.6.6.6 remote-as 111
    neighbor 6.6.6.6 update-source Loopback0
    neighbor 6.6.6.6 activate
    network 1.1.1.0
    neighbor 7.7.7.7 remote-as 111
    neighbor 7.7.7.7 update-source Loopback0
    neighbor 7.7.7.7 activate
    network 1.1.1.0
    neighbor 8.8.8.8 remote-as 111
    neighbor 8.8.8.8 update-source Loopback0
    neighbor 8.8.8.8 activate
    network 1.1.1.0
    end

--- 
    write
---

### R6

    configure terminal
    router bgp 111
    no sync
    bgp router-id 1.1.1.6
    address-family ipv4
    neighbor 1.2.0.2 remote-as 212
    neighbor 1.2.0.2 activate
    neighbor 1.1.1.1 remote-as 111
    neighbor 1.1.1.1 update-source Loopback0
    neighbor 1.1.1.1 activate
    network 1.1.1.0
    neighbor 2.2.2.2 remote-as 111
    neighbor 2.2.2.2 update-source Loopback0
    neighbor 2.2.2.2 activate
    network 1.1.1.0
    neighbor 3.3.3.3 remote-as 111
    neighbor 3.3.3.3 update-source Loopback0
    neighbor 3.3.3.3 activate
    network 1.1.1.0
    neighbor 4.4.4.4 remote-as 111
    neighbor 4.4.4.4 update-source Loopback0
    neighbor 4.4.4.4 activate
    network 1.1.1.0
    neighbor 5.5.5.5 remote-as 111
    neighbor 5.5.5.5 update-source Loopback0
    neighbor 5.5.5.5 activate
    network 1.1.1.0
    neighbor 7.7.7.7 remote-as 111
    neighbor 7.7.7.7 update-source Loopback0
    neighbor 7.7.7.7 activate
    network 1.1.1.0
    neighbor 8.8.8.8 remote-as 111
    neighbor 8.8.8.8 update-source Loopback0
    neighbor 8.8.8.8 activate
    network 1.1.1.0
    end

--- 
    write
---

### R7

    configure terminal
    router bgp 111
    no sync
    bgp router-id 1.1.1.7
    address-family ipv4
    neighbor 1.3.0.2 remote-as 213
    neighbor 1.3.0.2 activate
    neighbor 1.1.1.1 remote-as 111
    neighbor 1.1.1.1 update-source Loopback0
    neighbor 1.1.1.1 activate
    network 1.1.1.0
    neighbor 2.2.2.2 remote-as 111
    neighbor 2.2.2.2 update-source Loopback0
    neighbor 2.2.2.2 activate
    network 1.1.1.0
    neighbor 3.3.3.3 remote-as 111
    neighbor 3.3.3.3 update-source Loopback0
    neighbor 3.3.3.3 activate
    network 1.1.1.0
    neighbor 4.4.4.4 remote-as 111
    neighbor 4.4.4.4 update-source Loopback0
    neighbor 4.4.4.4 activate
    network 1.1.1.0
    neighbor 5.5.5.5 remote-as 111
    neighbor 5.5.5.5 update-source Loopback0
    neighbor 5.5.5.5 activate
    network 1.1.1.0
    neighbor 6.6.6.6 remote-as 111
    neighbor 6.6.6.6 update-source Loopback0
    neighbor 6.6.6.6 activate
    network 1.1.1.0
    neighbor 8.8.8.8 remote-as 111
    neighbor 8.8.8.8 update-source Loopback0
    neighbor 8.8.8.8 activate
    network 1.1.1.0
    end

--- 
    write
---
là
### R8

    configure terminal
    router bgp 111
    no sync
    bgp router-id 1.1.1.8
    address-family ipv4
    neighbor 1.4.0.2 remote-as 214
    neighbor 1.4.0.2 activate
    neighbor 1.1.1.1 remote-as 111
    neighbor 1.1.1.1 update-source Loopback0
    neighbor 1.1.1.1 activate
    network 1.1.1.0
    neighbor 2.2.2.2 remote-as 111
    neighbor 2.2.2.2 update-source Loopback0
    neighbor 2.2.2.2 activate
    network 1.1.1.0
    neighbor 3.3.3.3 remote-as 111
    neighbor 3.3.3.3 update-source Loopback0
    neighbor 3.3.3.3 activate
    network 1.1.1.0
    neighbor 4.4.4.4 remote-as 111
    neighbor 4.4.4.4 update-source Loopback0
    neighbor 4.4.4.4 activate
    network 1.1.1.0
    neighbor 5.5.5.5 remote-as 111
    neighbor 5.5.5.5 update-source Loopback0
    neighbor 5.5.5.5 activate
    network 1.1.1.0
    neighbor 6.6.6.6 remote-as 111
    neighbor 6.6.6.6 update-source Loopback0
    neighbor 6.6.6.6 activate
    network 1.1.1.0
    neighbor 7.7.7.7 remote-as 111
    neighbor 7.7.7.7 update-source Loopback0
    neighbor 7.7.7.7 activate
    network 1.1.1.0
    end

--- 
    write
---

---

## Client

---

### Client 1 - R9 

    configure terminal
    interface FastEthernet0/0
    ip address 1.1.0.2 255.255.255.252
    no shutdown
    end 

    configure terminal
    router bgp 211
    no sync 
    bgp router-id 1.2.1.1
    address-family ipv4
    neighbor 1.1.0.1 remote-as 111
    neighbor 1.1.0.1 activate
    network 1.1.0.0
    end 

---
    write
---

### Client 2 - R10 

    configure terminal
    interface FastEthernet0/0
    ip address 1.2.0.2 255.255.255.252
    no shutdown
    end 

    configure terminal
    router bgp 212
    no sync 
    bgp router-id 1.2.1.2
    address-family ipv4
    neighbor 1.2.0.1 remote-as 111
    neighbor 1.2.0.1 activate
    network 1.2.0.0
    end 

---
    write
---

### Client 3 - R11 

    configure terminal
    interface FastEthernet0/0
    ip address 1.3.0.2 255.255.255.252
    no shutdown
    end 

    configure terminal
    router bgp 213
    no sync 
    bgp router-id 1.2.1.3
    address-family ipv4
    neighbor 1.3.0.1 remote-as 111
    neighbor 1.3.0.1 activate
    network 1.3.0.0
    end 

---
    write
---

### Client 4 - R12

    configure terminal
    interface FastEthernet0/0
    ip address 1.4.0.2 255.255.255.252
    no shutdown
    end 

    configure terminal
    router bgp 214
    no sync 
    bgp router-id 1.2.1.4
    address-family ipv4
    neighbor 1.4.0.1 remote-as 111
    neighbor 1.4.0.1 activate
    network 1.4.0.0
    end 

---
    write
---

