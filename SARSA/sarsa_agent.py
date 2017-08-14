import numpy as np
import random
from collections import defaultdict
from environment import Env


class SARSAgent:
    def __init__(self, actions):
        pass
    
    # <s, a, r, s', a'>의 샘플로부터 큐함수를 업데이트
    def learn(self, state, action, reward, next_state, next_action):
        pass
        
    # 입실론 탐욕 정책에 따라서 행동을 반환
    def get_action(self, state):
        pass

    @staticmethod
    def arg_max(state_action):
        max_index_list = []
        max_value = state_action[0]
        for index, value in enumerate(state_action):
            if value > max_value:
                max_index_list.clear()
                max_value = value
                max_index_list.append(index)
            elif value == max_value:
                max_index_list.append(index)
        return random.choice(max_index_list)

if __name__ == "__main__":
    env = Env()
    agent = SARSAgent(actions=list(range(env.n_actions)))

    for episode in range(1000):
        # 게임 환경과 상태를 초기화
        
        # 현재 상태에 대한 행동을 선택

        while True:
            env.render()

            # 행동을 위한 후 다음상태 보상 에피소드의 종료 여부를 받아옴
            

            # 다음 상태에서의 다음 행동 선택
            

            # <s,a,r,s',a'>로 큐함수를 업데이트

            
            # 모든 큐함수를 화면에 표시
            env.print_value_all(agent.q_table)

            if done:
                break

