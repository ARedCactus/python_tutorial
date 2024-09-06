# 初始化变量  
requests = [10, 22, 20, 2, 40, 6, 38]  # 请求序列  
current_track = 20  # 磁头臂当前位置  
seek_time = 0  # 总寻道时间  
  
# 模拟SSTF算法  
while requests:  
    # 找出离当前位置最近的请求  
    min_distance = float('inf')  
    next_request = None  
    for req in requests:  
        distance = abs(req - current_track)  
        if distance < min_distance:  
            min_distance = distance  
            next_request = req  
      
    # 移动磁头臂并计算寻道时间  
    seek_time += min_distance * 6  # 每个柱面移动需要6ms  
      
    # 更新当前位置和移除已服务的请求  
    current_track = next_request  
    requests.remove(next_request)  
  
# 输出结果  
print(f"采用最短寻道时间优先调度算法时的寻道时间为：{seek_time}ms")