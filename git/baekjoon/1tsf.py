import math
# hole 좌표 (y, x)
hole = [[0, 0], [0, 127], [0, 254], [127, 0], [127, 127], [127, 254]]

r = 5.73 # 지름 5.73cm
# ball 좌표 (y, x)
b0 = [63, 63]     # 흰공
b1 = [100, 200]   # 목적구

for i in range(6):
    # 홀과 목적구 사이 거리 구하기
    x = hole[i][1] - b1[1]
    y = hole[i][0] - b1[0]
    length = (x**2 + y**2)**0.5
    # 홀을 기준으로 목적구에서 공 지름만큼 멀리 떨어져야함
    position = [b1[0] - y*r/length, b1[1] - x*r/length]
    # 그 좌표에 흰공이 가면 목적구는 각 홀로 이동 가능

    # 흰공-좌표 길이보다 흰공-목적구 길이가 더 길어야 각이 나옴
    b0_to_p = ((position[0]-b1[0])**2 + (position[1]-b1[1])**2)**0.5
    b0_to_b = ((b1[0]-b0[0])**2 + (b1[1]-b0[1])**2)**0.5
    if b0_to_p > b0_to_b: # 각이 나오면
        # 흰공이 가는길에 장애물 있는지
        for j in range(): # 흰공, 목적구 외 모든 공 개수 만큼
            # 흰공->목적구 + 6 < 흰공->장애물 + 장애물->목적구
            # 만족하면 장애물 없음
            pass
        for j in range(): # 흰공, 목적구 외 모든 공 개수 만큼
            # 목적구->홀 + 6 < 목적구->장애물 + 장애물->홀
            # 만족하면 장애물 없음
            pass
        # 우선순위 append
        pass
# 우선순위가 가장 높은거로 계산