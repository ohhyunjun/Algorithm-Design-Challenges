# 알고리즘 설계 팀 프로젝트

## 1. 문제: 2024 아시아-서울지역대회 Problem J (Street Development)

대규모 개발이 예정된 거리에 **N개의 중요 지점**이 있으며,  
N대의 **원격 조종 로봇**을 통해 각 지점의 정보를 수집해야 합니다.  
각 로봇은 하나의 중요 지점에서만 정보를 수집하며,  
**목표는 수집된 모든 정보를 단일 로봇에 통합하여 가장 효율적인 개발 방식을 찾는 것**입니다.

---

### 조건

- 개발 예정 거리는 **0부터 L까지의 1차원 구간**이며, 양 끝점도 포함합니다.
- N개의 중요 지점에 각각 로봇 한 대씩 배치하며, 초기에는 해당 지점의 정보만 보유합니다.
- 로봇은 좌우로 이동할 수 있으며, **이동 거리 1당 배터리 1만큼 소모**합니다.
- 모든 로봇은 **동일한 배터리 용량**을 가집니다.
- 로봇들이 만나면 정보를 서로 교환할 수 있습니다.
- **방향 전환 및 정보 교환은 배터리를 소모하지 않습니다.**
- 최종적으로 **최소 1대의 로봇이 모든 지점의 정보를 보유**해야 합니다.
<img width="453" height="251" alt="Image" src="https://github.com/user-attachments/assets/21f1c523-59fb-4a50-a84b-383713fe82f8" />

---

### 목표

- **모든 정보를 하나의 로봇에 통합**하는 데 필요한 **최소 배터리 용량(P)**을 구합니다.

---

### Input

- 첫째 줄에 두 정수 L (거리 구간의 끝 위치)와 N (중요 지점(로봇) 개수)가 주어집니다.  
  *(1 ≤ L ≤ 10^6, 2 ≤ N ≤ L+1)*
- 둘째 줄에는 N개의 정수가 **오름차순**으로 주어지며,  
  각 정수는 로봇이 시작한 중요 지점의 위치입니다.

---

### Output

- **최소한 하나의 로봇이 모든 중요한 지점의 정보를 얻기 위해 필요한 최소 배터리 용량 P**를 한 줄에 출력합니다.
<img width="747" height="233" alt="image" src="https://github.com/user-attachments/assets/09f23fed-6ea3-42aa-a1a7-494c1300fa35" />


---

## 2. 사용할 언어

- **파이썬**

---

## 3. 해결방안

- **이분탐색 + 그리디**
    - 배터리 비용을 이분 탐색으로 정합니다.
    - 각 구간에 대해 해당 비용으로 인접한 두 로봇이 합칠 수 있는지 **그리디**로 판정합니다.
    - 판정이 가능한 것으로 나오면 비용을 낮추고, 아니라면 비용을 올려 이 과정을 반복합니다.
    - 이를 통해 온전한 하나가 될 수 있는 **최소 배터리 비용**을 출력합니다.
