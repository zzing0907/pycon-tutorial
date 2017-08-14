import sys
import gym
import pylab
import random
import numpy as np
from collections import deque
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import Sequential

EPISODES = 300


# 카트폴 예제에서의 DQN 에이전트
class DQNAgent:
    def __init__(self, state_size, action_size):        
        # 상태와 행동의 크기 정의
        

        # DQN 하이퍼파라미터
        

        # 리플레이 메모리, 최대 크기 2000
        

        # 모델과 타깃 모델 생성
        

        # 타깃 모델 초기화
        pass
        
    # 상태가 입력, 큐함수가 출력인 인공신경망 생성
    def build_model(self):
        pass
    
    # 타깃 모델을 모델의 가중치로 업데이트
    def update_target_model(self):
        pass
    
    # 입실론 탐욕 정책으로 행동 선택
    def get_action(self, state):
        pass
    
    # 샘플 <s, a, r, s'>을 리플레이 메모리에 저장
    def append_sample(self, state, action, reward, next_state, done):
        pass
    
    # 리플레이 메모리에서 무작위로 추출한 배치로 모델 학습
    def train_model(self):
        pass

if __name__ == "__main__":
    # CartPole-v1 환경, 최대 타임스텝 수가 500
    env = gym.make('CartPole-v1')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n

    # DQN 에이전트 생성
    agent = DQNAgent(state_size, action_size)

    
    for e in range(EPISODES):
        # env 초기화
        
        while not done:
            env.render()
            # 현재 상태로 행동을 선택


            # 선택한 행동으로 환경에서 한 타임스텝 진행


            # 에피소드가 중간에 끝나면 -100 보상

            
            # 리플레이 메모리에 샘플 <s, a, r, s'> 저장


            # 매 타임스텝마다 학습
            

            if done:
                # 각 에피소드마다 타깃 모델을 모델의 가중치로 업데이트
                

                # 에피소드마다 학습 결과 출력


                # 이전 10개 에피소드의 점수 평균이 490보다 크면 학습 중단
                
