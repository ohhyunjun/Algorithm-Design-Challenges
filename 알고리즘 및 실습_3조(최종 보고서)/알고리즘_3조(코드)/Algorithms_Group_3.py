def can_connect_with_battery(positions, battery):
    # 왼쪽 체인
    left_pref = [None] * n
    left_pref[0] = positions[0] + battery

    for i in range(1, n):
        prev = left_pref[i-1]
        if prev is None:
            break
        cost = abs(positions[i] - prev)
        if cost > battery:
            break
        new_reach = prev + (battery - cost)
        left_pref[i] = new_reach
        if new_reach >= positions[-1]:
            return True

    # 오른쪽 체인
    right_suff = [None] * n
    right_suff[-1] = positions[-1] - battery

    for j in range(n-2, -1, -1):
        nxt = right_suff[j+1]
        if nxt is None:
            break
        cost = abs(positions[j] - nxt)
        if cost > battery:
            break
        new_reach = nxt - (battery - cost)
        right_suff[j] = new_reach
        if new_reach <= positions[0]:
            return True

    # 허브 코드
    for k in range(n):
        L = positions[0] + battery    if k == 0   else left_pref[k-1]
        R = positions[-1] - battery   if k == n-1 else right_suff[k+1]
        if L is None or R is None:
            continue

        if L >= R:
            return True

        span = R - L
        dist_to_hub = min(abs(positions[k] - L),
                          abs(positions[k] - R))
        if span + dist_to_hub <= battery:
            return True

    return False


def find_minimum_battery(positions):

    lo, hi = 0, positions[-1] - positions[0]
    
    while lo < hi:
        mid = (lo + hi) // 2
        if can_connect_with_battery(positions, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    L, n = map(int, input().split())
    positions = list(map(int, input().split()))

    print(find_minimum_battery(positions))